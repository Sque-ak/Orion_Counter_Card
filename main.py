#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.15.4


__author__ = 'Novotorzhin V.'
__company__ = 'AsiaAgroFood JSC'



from datetime import datetime
from multiprocessing.sharedctypes import Value
from xml.etree.ElementTree import XML
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, resources, logic, config
import pyodbc, binascii
from io import BytesIO
from PIL import Image
import database
import numpy as np



class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.setEnabled(True)
                MainWindow.resize(config.size_window_w, config.size_window_h)
                MainWindow.setStyleSheet("border-radius: 10px;")
                MainWindow.setWindowIcon(QtGui.QIcon('icon.ico'))
                MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
                MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    
                # Colors:
                self.palette_white = QtGui.QPalette()
                self.palette_white.setColor(QtGui.QPalette.Text, QtCore.Qt.white)

                # Objects:
                self.MainApps = QtWidgets.QWidget(MainWindow)
                self.MainApps.setObjectName("MainApps")
                self.MainWindow_2 = QtWidgets.QVBoxLayout(self.MainApps)
                self.MainWindow_2.setObjectName("MainWindow_2")
                self.Main = QtWidgets.QWidget(self.MainApps)
                self.Main.setObjectName("Main")
                self.Main_2 = QtWidgets.QVBoxLayout(self.Main)
                self.Main_2.setSpacing(0)
                self.Main_2.setObjectName("Main_2")

                self.Header = QtWidgets.QWidget(self.Main)
                self.Header.setObjectName("Header")
                self.Header.setStyleSheet("border-image: url(:/background_header/background_forest.jpg) 0 0 0 0 stretch stretch;\n" "border-top-left-radius:50px;"
                                          "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,0,0,80), stop:1 rgba(40,40,40,80));\n")
                self.gridLayout = QtWidgets.QGridLayout(self.Header)
                self.gridLayout.setContentsMargins(20, 20, 20, 20)
                self.gridLayout.setObjectName("gridLayout")


                self.Layout_Profile = QtWidgets.QWidget(self.Header)
                self.Layout_Profile.setObjectName("Layout_Profile")
                self.Layout_Profile.setStyleSheet("background: None;\n" "border-bottom-left-radius: 60px;\n" "border-image: None;"
                                                  "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 180), stop:1 rgba(0, 0, 0, 60));\n")
                self.Layout_Profile_2 = QtWidgets.QHBoxLayout(self.Layout_Profile)
                self.Layout_Profile_2.setObjectName("Layout_Profile_2")
                self.gridLayout.addWidget(self.Layout_Profile, 0, 0, 1, 1)

                self.Img_Profile = QtWidgets.QLabel(self.Layout_Profile)
                self.Img_Profile.setLayoutDirection(QtCore.Qt.LeftToRight)
                
                self.Img_Profile.setPixmap(logic.PixmapToRound(self, QtGui.QPixmap(':/none_avatar/avatar_none.jpg').scaled(200,200), 100, 200, 200))
                
                self.Img_Profile.setObjectName("Img_Profile") 

                self.Layout_Name = QtWidgets.QVBoxLayout()
                self.Layout_Name.setContentsMargins(10, 10, 10, 10)
                self.Layout_Name.setObjectName("Layout_Name")
                spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.Layout_Name.addItem(spacerItem)
                self.l_Name = QtWidgets.QLabel(self.Layout_Profile)
                self.l_Name.setStyleSheet("Background: None;")
                self.l_Name.setObjectName("l_Name")
                self.Layout_Name.addWidget(self.l_Name)
                self.l_Result = QtWidgets.QLabel(self.Layout_Profile)
                self.l_Result.setStyleSheet("Background: None;")
                self.l_Result.setObjectName("l_Result")
                self.Layout_Name.addWidget(self.l_Result)
                spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.Layout_Name.addItem(spacerItem1)

                self.Layout_Profile_2.addWidget(self.Img_Profile)
                self.Layout_Profile_2.addLayout(self.Layout_Name)
                self.Layout_Profile_2.setStretch(0, 5)
                self.Layout_Profile_2.setStretch(1, 20)

                self.Layout_CounterUser = QtWidgets.QWidget(self.Header)
                self.Layout_CounterUser.setStyleSheet("background: None;\n" "border-radius: 0;\n" "border-image: None;"
                                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 60), stop:1 rgba(0, 0, 0, 180));\n")
                self.Layout_CounterUser.setObjectName("Layout_CounterUser")
                self.Layout_CounterUser_2 = QtWidgets.QGridLayout(self.Layout_CounterUser)
                self.Layout_CounterUser_2.setContentsMargins(-1, 10, 10, -1)
                self.Layout_CounterUser_2.setObjectName("Layout_CounterUser_2")
                self.l_Title = QtWidgets.QLabel(self.Layout_CounterUser)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHeightForWidth(self.l_Title.sizePolicy().hasHeightForWidth())
                self.l_Title.setSizePolicy(sizePolicy)
                self.l_Title.setMinimumSize(QtCore.QSize(20, 20))
                self.l_Title.setStyleSheet("Background: none")
                self.l_Title.setObjectName("l_Title")
                self.Layout_CounterUser_2.addWidget(self.l_Title, 0, 0, 1, 1)
                self.l_CounterUsers = QtWidgets.QLabel(self.Layout_CounterUser)
                self.l_CounterUsers.setMinimumSize(QtCore.QSize(20, 20))
                self.l_CounterUsers.setStyleSheet("Background: None;")
                self.l_CounterUsers.setObjectName("l_CounterUsers")
                self.Layout_CounterUser_2.addWidget(self.l_CounterUsers, 2, 0, 1, 1)
                self.l_Status = QtWidgets.QLabel(self.Layout_CounterUser)
                self.l_Status.setMinimumSize(QtCore.QSize(20, 20))
                self.l_Status.setStyleSheet("Background: None")
                self.l_Status.setObjectName("l_Status")
                self.Layout_CounterUser_2.addWidget(self.l_Status, 3, 0, 1, 1)
                spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.Layout_CounterUser_2.addItem(spacerItem2, 4, 0, 1, 1)
                self.gridLayout.addWidget(self.Layout_CounterUser, 0, 1, 1, 1)
                self.Layout_Description = QtWidgets.QWidget(self.Header)
                self.Layout_Description.setStyleSheet("background: None;\n" "border-bottom-left-radius: 60px;\n" "border-top-left-radius: 40px;\n" "border-image: None;"
                                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 180), stop:1 rgba(0, 0, 0, 60));\n")
                self.Layout_Description.setObjectName("Layout_Description")
                self.Layout_Description_2 = QtWidgets.QGridLayout(self.Layout_Description)
                self.Layout_Description_2.setContentsMargins(10, 10, 10, 10)
                self.Layout_Description_2.setObjectName("Layout_Description_2")
                self.l_Icon_Description = QtWidgets.QLabel(self.Layout_Description)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHeightForWidth(self.l_Icon_Description.sizePolicy().hasHeightForWidth())
                self.l_Icon_Description.setSizePolicy(sizePolicy)
                self.l_Icon_Description.setMinimumSize(QtCore.QSize(160, 120))
                self.l_Icon_Description.setStyleSheet("border-image: url(:/proxy_step/proxy step.png);\n" "border-radius: 20px;\n" "background: None;")
                self.l_Icon_Description.setObjectName("l_Icon_Description")
                self.Layout_Description_2.addWidget(self.l_Icon_Description, 0, 0, 1, 1)
                self.l_Time = QtWidgets.QLabel(self.Layout_Description)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(10)
                sizePolicy.setHeightForWidth(self.l_Time.sizePolicy().hasHeightForWidth())
                self.l_Time.setSizePolicy(sizePolicy)
                self.l_Time.setStyleSheet("background: None;")
                self.l_Time.setObjectName("l_Time")
                self.Layout_Description_2.addWidget(self.l_Time, 0, 3, 1, 1)
                self.l_Description = QtWidgets.QLabel(self.Layout_Description)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(30)
                sizePolicy.setHeightForWidth(self.l_Description.sizePolicy().hasHeightForWidth())
                self.l_Description.setSizePolicy(sizePolicy)
                self.l_Description.setStyleSheet("background: None;")
                self.l_Description.setObjectName("l_Description")
                self.Layout_Description_2.addWidget(self.l_Description, 0, 1, 1, 1)
                spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.Layout_Description_2.addItem(spacerItem3, 0, 2, 1, 1)
                self.gridLayout.addWidget(self.Layout_Description, 2, 0, 1, 2)
                self.Main_2.addWidget(self.Header)
                self.Footer = QtWidgets.QWidget(self.Main)
                self.Footer.setStyleSheet("background: rgb(43,42,41);\n""border-bottom-right-radius: 60px;")
                self.Footer.setObjectName("Footer")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.Footer)
                self.verticalLayout.setContentsMargins(20, 20, 20, 20)
                self.verticalLayout.setObjectName("verticalLayout")
                self.l_History = QtWidgets.QTableWidget(self.Footer)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setVerticalStretch(200)
                sizePolicy.setHeightForWidth(self.l_History.sizePolicy().hasHeightForWidth())
                self.l_History.setSizePolicy(sizePolicy)
                self.l_History.setMinimumSize(QtCore.QSize(0, 200))
                self.l_History.setStyleSheet("background-color: rgb(23, 22, 21);\n""border-radius: 20px;")
                self.l_History.setObjectName("l_History")
                self.l_History.setColumnCount(3)
                self.l_History.setRowCount(0)
                self.l_History.setShowGrid(True)
                self.l_History.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                self.l_History.verticalHeader().hide()
                self.l_History.horizontalHeader().hide()
                self.l_History.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
                self.l_History.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
                self.l_History.setFocusPolicy(QtCore.Qt.NoFocus)
                self.verticalLayout.addWidget(self.l_History)
                self.l_Input_ID = QtWidgets.QLineEdit(self.Footer)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setVerticalStretch(20)
                sizePolicy.setHeightForWidth(self.l_Input_ID.sizePolicy().hasHeightForWidth())
                self.l_Input_ID.setSizePolicy(sizePolicy)
                self.l_Input_ID.setMinimumSize(QtCore.QSize(0, 40))
                self.l_Input_ID.setStyleSheet("background-color: rgb(23, 22, 21);\n""border-bottom:2px solid rgba(255, 255, 255, 100);\n""border-radius: 10px;")
                self.l_Input_ID.setObjectName("l_Input_ID")
                self.l_Input_ID.setPalette(self.palette_white)
                self.l_Input_ID.setFont(QtGui.QFont('MS Shell Dlg 2', 16))
                self.l_Input_ID.setAlignment(QtCore.Qt.AlignCenter)
                self.l_Input_ID.setMaxLength(16)
                self.verticalLayout.addWidget(self.l_Input_ID)
                self.Main_2.addWidget(self.Footer)
                self.MainWindow_2.addWidget(self.Main)
                MainWindow.setCentralWidget(self.MainApps)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)


                logic.setStatus(self, 2)
                logic.setResult(self, 2)
                logic.setName(self, "Добрый день")
                self.counterUsers = 0

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)


        def retranslateUi(self, MainWindow) -> None:
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Counter Cards"))
                self.l_Title.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#ffffff;\">Столовая <br/></span><span style=\" font-size:12pt; font-weight:600; text-decoration: underline; color:#ffffff;\">" + config.company_name + "</span></p></body></html>"))
                logic.counterUserShow(self, self.l_CounterUsers)
                logic.nameShow(self, self.l_Name)
                logic.statusShow(self, self.l_Status)
                logic.resultShow(self, self.l_Result)
                self.l_Description.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Поднесите свой рабочий пропуск к считывателю.</span><span style=\" font-size:12pt; color:#ffffff;\"><br/>После писка, будет выписан один обед в столовой.</span></p></body></html>"))

class Sql(Ui_MainWindow):
        """ SQL Connection
        Server Microsoft SQL Server 2012
        All config in file config.py
        In floder drivers have the sqlncli 64x this is SQL Server Native Client 11.0 driver

                :param str database: Name by database;
                :param str server: Host by database;
                :param str user: User administrator by database;
                :param str password: Password user by database;
                :param str port: Port by database;
        """
        def __init__(self, database:str=config.name_db, server:str=config.host_db, user:str=config.user_db, password:str=config.password_db, port:str=config.port_db):
                try:
                        self.cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                        "Server="+server+";"
                                        "Database="+database+";"
                                        "UID="+user+";"
                                        "PWD="+password+";"
                                        "PORT="+port+";")
                        self.status = 1
                except pyodbc.Error as ex:
                        self.status = ex
                        print(ex)

        def getDataUID(self, code:str):
                """ Get Data by the code.

                        :param str code: The Input code by we'll get data from orion.
                """
                cursor = self.cnxn.cursor()

                data = self.encryptionCard(self.WiegandToDallas(code))
                sql = ("""SELECT 
                                TabNumber
                                ,Name
                                ,FirstName
                                ,MidName
                                ,CodeP
                                ,Picture
                                FROM pList INNER JOIN pMark 
                                ON pList.ID = pMark.Owner
                                WHERE pMark.CodeP IN ( ? ) """)

                cursor.execute(sql, data)
                __result = np.array(cursor.fetchone(), np.object_)
                return __result

        def checkElementCode(self, element:str) -> str:
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

        def decodingCard(self, code:str) -> str:
                """Decoding proxy card in base ORION PRO
  
                        :param str code: proxy card code;
                """
                __result = code.encode("CP1251")
                __result = binascii.hexlify(__result[::-1])
                __result = __result[::-1].decode()
                __result = __result[::-1].replace('01fe','00')
                #__result = __result[::-1].replace('01fe','fe')
                #__result = __result[::-1].replace('02fe','fe')
                __result = __result[::-1].replace('03fe','20')
                __result = __result[::-1].replace('04fe','5c')
                __result = __result[::-1].replace('05fe','0a')
                __result = __result[::-1].replace('00fe','0001FE')
                return __result[0:16]

        def encryptionCard(self, code:str) -> str:
                """Encryption proxy card for base ORION PRO

                        :param str code: proxy card code
                """
                __result = "80" + code[::-1].upper()
                __result = np.array([__result[i:i+2] for i in range(0, len(__result), 2)], np.object_) #Division into hex of 2 char, we will got 8 hex.

                for i in range(9):
                        __result[i] = self.checkElementCode(__result[i])

                __result = ''.join(map(str,__result))[::-1]
                __result = str.encode(__result, encoding='utf-8')
                __result = binascii.unhexlify(__result)
                __result = __result[::-1].decode("ansi").replace('\n', '')
                
                return str(__result)

        # CRC-8 DALLAS 
        def WiegandToDallas(self, UID:str) -> str:
                """ This is def to received to proxy card code size is 10 hex
                like this 0000000000 we must get this 3d00000000000001. This's 16 hex code.
                Checksum is calculated by the algorithm CRC-8 DALLAS.

                        :param str UID: Proxy code 10 hex.
                """ 
                CRCTable = np.array((0, 94, 188, 226, 97, 63, 221, 131, 194, 156, 126, 32, 163, 253, 31, 65,
                        157, 195, 33, 127, 252, 162, 64, 30, 95, 1, 227, 189, 62, 96, 130, 220,
                        35, 125, 159, 193, 66, 28, 254, 160, 225, 191, 93, 3, 128, 222, 60, 98,
                        190, 224, 2, 92, 223, 129, 99, 61, 124, 34, 192, 158, 29, 67, 161, 255,
                        70, 24, 250, 164, 39, 121, 155, 197, 132, 218, 56, 102, 229, 187, 89, 7,
                        219, 133, 103, 57, 186, 228, 6, 88, 25, 71, 165, 251, 120, 38, 196, 154,
                        101, 59, 217, 135, 4, 90, 184, 230, 167, 249, 27, 69, 198, 152, 122, 36,
                        248, 166, 68, 26, 153, 199, 37, 123, 58, 100, 134, 216, 91, 5, 231, 185,
                        140, 210, 48, 110, 237, 179, 81, 15, 78, 16, 242, 172, 47, 113, 147, 205,
                        17, 79, 173, 243, 112, 46, 204, 146, 211, 141, 111, 49, 178, 236, 14, 80,
                        175, 241, 19, 77, 206, 144, 114, 44, 109, 51, 209, 143, 12, 82, 176, 238,
                        50, 108, 142, 208, 83, 13, 239, 177, 240, 174, 76, 18, 145, 207, 45, 115,
                        202, 148, 118, 40, 171, 245, 23, 73, 8, 86, 180, 234, 105, 55, 213, 139,
                        87, 9, 235, 181, 54, 104, 138, 212, 149, 203, 41, 119, 244, 170, 72, 22,
                        233, 183, 85, 11, 136, 214, 52, 106, 43, 117, 151, 201, 74, 20, 246, 168,
                        116, 42, 200, 150, 21, 75, 169, 247, 182, 232, 10, 84, 215, 137, 107, 53), np.ubyte)

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

class Runtime(QtWidgets.QMainWindow, Ui_MainWindow):
        def __init__(self):
                super().__init__()
                self.setupUi(self)

                self.timer = QtCore.QTimer(self)
                self.timer.setInterval(1000)
                self.timer.timeout.connect(self.displayTime)
                self.timer.start()
                self.l_Input_ID.installEventFilter(self)
                self.centerWindow()
                self.changeStatus()

        # Display time for loop for get current time.
        def displayTime(self) -> None:
                logic.timeShow(self, self.l_Time)
                pass
        
        # if Enter will be pressed then move the proxy code to the List and get data from Mysql
        def eventFilter(self, source, event):
                """ This is Hell. :c
                """
                if source == self.l_Input_ID and event.type() == QtCore.QEvent.KeyPress \
                                             and event.key() == QtCore.Qt.Key_Return:
                        try:
                                __l_image = QtGui.QPixmap(':/none_avatar/avatar_none.jpg').scaled(200,250)
                                if len(self.l_Input_ID.text()) == 10:
                                                __l_data_user = sql.getDataUID(self.l_Input_ID.text())
                                                
                                                if __l_data_user[5] != None:
                                                        __l_image = Image.open(BytesIO(__l_data_user[5])).convert("RGBA")
                                                        __l_image = QtGui.QImage(__l_image.tobytes("raw","RGBA"), __l_image.size[0], __l_image.size[1], QtGui.QImage.Format.Format_RGBA8888)
                                                        __l_image = QtGui.QPixmap.fromImage(__l_image)
                                                        self.Img_Profile.setPixmap(logic.PixmapToRound(self,__l_image.scaled(200,200), 100, 200, 200))
                                                else:
                                                        self.Img_Profile.setPixmap(logic.PixmapToRound(self, QtGui.QPixmap(':/none_avatar/avatar_none.jpg').scaled(200,200), 100, 200, 200))

                                                XMLDataBase.add_user(data=[__l_data_user[1],__l_data_user[2],__l_data_user[3], str(datetime.now().strftime('%H:%M:%S')), self.l_Input_ID.text(), __l_data_user[0]])
                                                XMLDataBase.save()    
                                else:
                                        __time_now = QtCore.QTime.currentTime().toString(QtCore.Qt.DefaultLocaleLongDate)
                                        __l_data_user = np.array(('','Unknown','',__time_now, self.l_Input_ID.text()), np.object_)

                                logic.inputLogic(self, self.l_History, self.l_Input_ID, self.l_Result, self.l_Name, self.l_CounterUsers, __l_data_user, __l_image)

                        except Exception as error:
                                print("Error: " + str(error))
                                __time_now = QtCore.QTime.currentTime().toString(QtCore.Qt.DefaultLocaleLongDate)
                                __l_data_user = np.array(('ERROR 404','Не рабочая карта','',__time_now, self.l_Input_ID.text()), np.object_) 
                                self.Img_Profile.setPixmap(logic.PixmapToRound(self, QtGui.QPixmap(':/none_avatar/avatar_none.jpg').scaled(200,200), 100, 200, 200))
                                logic.inputLogic(self, self.l_History, self.l_Input_ID, self.l_Result, self.l_Name, self.l_CounterUsers, __l_data_user, __l_image)
                                

                return super().eventFilter(source, event)


        # Check SQL
        def changeStatus(self) -> None:
                if sql.status == 1:
                        logic.setStatus(self, 1)
                        logic.statusShow(self, self.l_Status)
                else:
                        logic.setStatus(self, 2)
                        logic.statusShow(self, self.l_Status, sql.status)
                pass

        # Center the window in the screen.
        def centerWindow(self) -> None:
                """ Window in the center of your screen.
                """
                qr = self.frameGeometry()
                cp = QtWidgets.QDesktopWidget().availableGeometry().center()
                qr.moveCenter(cp)
                self.move(qr.topLeft())
                

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        sql = Sql()
        XMLDataBase = database.DataBase()
        ui = Runtime()
        ui.show()
        sys.exit(app.exec_())
