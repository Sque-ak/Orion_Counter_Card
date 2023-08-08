# Counter Cards
![icon](https://github.com/Sque-ak/orion-counter-card/blob/master/icon.ico) Cards reader and get the user name from orion data base. <br />
This is project have: <br /> <br />
```diff
+ 1. Decryption cards;
+ 2. Enecryption cards;
+ 3. CRC-8 Dallas;
+ 4. Simple integration with 1C;
+ 5. Simple integration with Orion Data Base (i mean just connect to the microsoft SQL server);
+ 6. XML with data;
```
<br /> <br />
CheckSum.py have only function Crc-8, Decryption and Enecryption for cheack the cards;<br />
Driver/ПосетителиСтоловой.erf for 1C;<br />
***
<br /> <br />
Install:<br />
For work app need the microsoft sql server, and ethernet.<br />
1. install from drivers the sqlincli 64x.msi;<br />
2. Project have to compile for exmaple: pyinstaller --onefile .\main.py;<br />
3. Then open exe file it will make the config.ini;<br />
4. Set the required parameters in config.ini;<br />
5. Open again the exe with new parameters;<br />
6. You're done. Congratulation.<br />


<br /> <br />
You're can install the app on monoblock:<br />
<img src="https://github.com/Sque-ak/orion-counter-card/blob/main/monoglock.jpg" width="250" height="250"><br />
and proxy-usb-ma :<br />
<img src="https://github.com/Sque-ak/orion-counter-card/blob/main/proxyusbma.png" width="250" height="250"><br />

