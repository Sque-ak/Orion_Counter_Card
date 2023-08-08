# CRC-8 DALLAS 
import binascii
import numpy as np

def WiegandToDallas(UID:str) -> str:
        """ This is def to received to proxy card code size is 10 hex
        like this 0000000000 we must get this 3d00000000000001. This's 16 hex code.
        Checksum is calculated by the algorithm CRC-8 DALLAS.
        """ 
        CRCTable = np.array((0,94,188,226,97,63,221,131,194,156,126,32,163,253,31,65,
                157,195,33,127,252,162,64,30,95,1,227,189,62,96,130,220,
                35,125,159,193,66,28,254,160,225,191,93,3,128,222,60,98,
                190,224,2,92,223,129,99,61,124,34,192,158,29,67,161,255,
                70,24,250,164,39,121,155,197,132,218,56,102,229,187,89,7,
                219,133,103,57,186,228,6,88,25,71,165,251,120,38,196,154,
                101,59,217,135,4,90,184,230,167,249,27,69,198,152,122,36,
                248,166,68,26,153,199,37,123,58,100,134,216,91,5,231,185,
                140,210,48,110,237,179,81,15,78,16,242,172,47,113,147,205,
                17,79,173,243,112,46,204,146,211,141,111,49,178,236,14,80,
                175,241,19,77,206,144,114,44,109,51,209,143,12,82,176,238,
                50,108,142,208,83,13,239,177,240,174,76,18,145,207,45,115,
                202,148,118,40,171,245,23,73,8,86,180,234,105,55,213,139,
                87,9,235,181,54,104,138,212,149,203,41,119,244,170,72,22,
                233,183,85,11,136,214,52,106,43,117,151,201,74,20,246,168,
                116,42,200,150,21,75,169,247,182,232,10,84,215,137,107,53), np.ubyte)

        __UID = "00" + UID + "01"
        __UID = np.array([__UID[i:i+2] for i in range(0, len(__UID), 2)], np.object_) #Division into hex of 2 char, we will got 8 hex.
        __code_dec = np.zeros(9, np.ubyte)
        __UID = __UID[::-1] #reverse

        for i in range(7):
          __code_dec[i] = int(__UID[i], 16)
          __code_dec[8] = CRCTable[np.bitwise_xor(__code_dec[8], __code_dec[i])]

        if len(str(hex(__code_dec[8])[2:]))>1:
                return str(hex(__code_dec[8])[2:]) + "00" + UID + "01"
        else:
                return "0" + str(hex(__code_dec[8])[2:]) + "00" + UID + "01"

def checkElementCode(element:str) -> str:
        """ Function for get code ProxyCard
                :param str element:  Have to be one element from code proxy card with 2 char.
        Example:
        We have list with 9 elements like ['00','EF','00' and etc];
        Each element check with the list in the fucntion as a result we get the encryption value; """

        if element == '00':
                return 'EF10'
        elif element == 'EF':
                return 'EF20'
        elif element == '02':
                return 'EF30'
        elif element == 'C5':
                return 'EF40'
        elif element == 'A0':
                return 'EF50'
        elif element == '0001FE':
                return 'EF00'
        else:
                return element # if value haven't in the list then we send the element back.

        #__result[i] = __result[i].replace('FA','EF20')    # i don't know what it. it doesn't work but leave it here just in case.
        #__result[i] = __result[i].replace('CC','EF60')


def encryptionCard(code:str) -> str:
        """Encryption proxy card for base ORION PRO

                :param str code: proxy card code
        """
        __result = "80" + code[::-1].upper()
        __result = np.array([__result[i:i+2] for i in range(0, len(__result), 2)], np.object_) #Division into hex of 2 char, we will got 8 hex.
        print("\nEncrypting...")
        print("(E) We have: " + str(__result))
        for i in range(9):
                __result[i] = checkElementCode(__result[i])

        print("(E) We got:  " + str(__result))
        __result = ''.join(map(str,__result))[::-1]
        __result = str.encode(__result, encoding='utf-8')
        __result = binascii.unhexlify(__result)
        print("(E) Bytes: " + str(__result))
        __result = __result[::-1].decode("ansi").replace('\n', '')
        
        return str(__result)

def decodingCard(code:str) -> str:
                """Decoding proxy card in base ORION PRO
  
                        :param str code: proxy card code;
                """
                __result = code.encode("CP1251")
                print("\nDecrypting...")
                print("(D) Bytes: " + str(__result[::-1]))
                __result = binascii.hexlify(__result[::-1])
                __result = __result[::-1].decode()
                print("(D) We Have: " + str(__result))
                __result = __result[::-1].replace('01fe','00')
                __result = __result[::-1].replace('02fe','fe')
                __result = __result[::-1].replace('03fe','20')
                __result = __result[::-1].replace('04fe','5c')
                __result = __result[::-1].replace('05fe','0a')
                __result = __result[::-1].replace('00fe','0001FE')

                #__result = __result[::-1].replace('04fe','cc') # This is don't work.
                #__result = __result[::-1].replace('01fe','fe')

                print("(D) We Got: " + str(__result))
                return __result[0:16]

def analyticsCards(code:str, mode:bool) -> None:
        """ Simply disassembles the encryption and decryption of the card in stages

                :param str code: proxy card code
                :param bool mode: if true then encryption else decryption.
                
                #Exmaple cards codes: "0100B25A67", "050010B417", "1600295C05",
                "2500B3EF29", "2500B427C0", "5800870A8B", "160028AFB6";

                #Exmaple decryption codes: "А'ґю%юЄ", "‹ю‡юXюМ", "¶Ї(ююю";
        """
        if mode:
                print("(E) Result:  " + encryptionCard(WiegandToDallas(code)) + "\n")
        else:
                print("(D) Result:  " + decodingCard(code) + "\n")  

if __name__ == "__main__":
        # Input your data
        analyticsCards("58008720FA", 1)
        analyticsCards("ъю‡юXю&", 0)
