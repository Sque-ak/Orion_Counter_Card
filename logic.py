__author__ = 'Novotorzhin V.'
__company__ = 'AsiaAgroFood JSC'


from array import array
from PyQt5 import QtCore, QtWidgets, QtGui
import sys, os
import numpy as np


_translate = QtCore.QCoreApplication.translate


def PixmapToRound(self, src:QtGui.QPixmap, radius:int, w:int, h:int):
    """ The Simple Photo ---> The Circule Photo.

            @param QPixmap src: This is url to photo user;
            @param int  radius: This is like border radius;
            @param int       W: Width the new image;
            @param int       H: Height the new image;
    """

    if src.isNull(): 
            return QtGui.QPixmap

    __target = QtGui.QPixmap(w, h)
    __target.fill(QtCore.Qt.GlobalColor.transparent)
    __painter = QtGui.QPainter(__target)
    __circule = QtGui.QPainterPath()

    __painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
    __painter.setRenderHint(QtGui.QPainter.RenderHint.SmoothPixmapTransform)
    __painter.setRenderHint(QtGui.QPainter.RenderHint.HighQualityAntialiasing)
    __circule.addRoundedRect(0, 0, w, h, radius, radius)
    __painter.setClipPath(__circule)
    __painter.drawPixmap(0, 0, src)

    return __target

    

def getStatus(self) -> int:
    """ Get status from label;
    """
    return self.status

def setStatus(self, new_status:str) -> None:
    """ This is function show the status app.
    Status can be three type:
    1. Online - Alright, all work. MySQL been connected, we can will get proxy cards.
    3. Error (text error) - Something wrong.

        @param str new_status: New status value;
    """
    self.status = new_status
    pass
    

def statusShow(self, s_status:str, Error:str="") -> None:
    """ This is function show the status app.
        Status can be three type:
        1. Online - Alright, all work. MySQL been connected, we can will get proxy cards.
        3. Error (text error) - Something wrong. 
         
            @param str s_status: This is object label will be show the status;
    """

    if getStatus(self) == 1:
        s_status.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600; color:#11ff4c;\">Online</p></body></html>"))
    else:
        s_status.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600; color:#11ff4c;\">Error:"+ str(Error) +"</p></body></html>"))
    pass


def getResult(self) -> int: 
    return self.result

def setResult(self, new_result:str) -> None:
    """ This is function show the result when user to swipe his card.
    Result can be two type:
    1. "Карта принята приятного аппетита." - Alright.
    2. "Что-то пошло не так, отказано." - Something wrong. 

        @param str new_result: Parameter to new result on label;
    """
    self.result = new_result
    pass
    

def resultShow(self, s_result:str) -> None:
    """ This is function show the result when user to swipe his card.
        Result can be two type:
        1. "Карта принята приятного аппетита." - Alright.
        2. "Что-то пошло не так, отказано." - Something wrong. 

            @param str s_result:  This is object label will be show the result.
    """

    if getResult(self) == 1:                        
        s_result.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#11ff4c;\">Карта принята приятного аппетита.</span></p></body></html>"))
    else:
        s_result.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#cd5c5c;\">Что-то пошло не так, отказано.</span></p></body></html>"))

    pass


def timeShow(self, s_time) -> None:
    """ Time 
    """
    __display_time = QtCore.QTime.currentTime().toString(QtCore.Qt.DefaultLocaleLongDate)
    s_time.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">" + __display_time + "</span></p></body></html>"))
    pass


def counterUserShow(self, s_counterUser:int) -> None: 
    """ Counter user show on label;

            @param int s_counterUser: Number of users who received lunch;
    """
    s_counterUser.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Сегодня посетителей: " + str(self.counterUsers) + "</span></p></body></html>"))
    pass

def getName(self) -> str:
    """ Get name from label name;
    """
    return self.name

def setName(self, new_name:str) -> None:
    """ Set new name to label name;

            @param str new_name: New name user;
    """
    self.name = new_name
    pass

def nameShow(self, s_name:str) -> None:
    """ Show name user on label name;
        
            @param str s_name:  Name user;
    """                                     
    s_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">" + getName(self) + "</span></p></body></html>"))
    pass

def inputLogic(self, l_history, l_input, l_result, l_name, l_counterUser, l_data, l_picture):
    """ After we got proxy card id, we must get for the id - name, time now and to give this all to application.
        This is function must be dispose in event like Key Press.

        l_history and l_input, l_result - this is GUI textedit, label and list fields.
    """
    __time_now = QtCore.QTime.currentTime().toString(QtCore.Qt.DefaultLocaleLongDate)

    if len(l_input.text()) == 10 and l_data[0] != 'ERROR 404': #050010b417
        __name_item = np.array([l_data[1] + ' ' + l_data[2] + ' ' +l_data[3], __time_now, l_input.text()], np.object_)

        l_history.insertRow(0)
        item = QtWidgets.QTableWidgetItem(__name_item[0])
        item.setData(QtCore.Qt.ItemDataRole.DecorationRole, l_picture.scaled(30,30))
        item.sizeHint
        l_history.setItem(0, 0, item)
        l_history.setItem(0, 1, QtWidgets.QTableWidgetItem(__name_item[1]))
        l_history.setItem(0, 2, QtWidgets.QTableWidgetItem(__name_item[2]))
        l_history.item(0,0).setBackground(QtGui.QColor(124,210,24))
        l_history.item(0,1).setBackground(QtGui.QColor(124,210,24))
        l_history.item(0,2).setBackground(QtGui.QColor(124,210,24))
        #winsound.MessageBeep()
        print('\a')


        setResult(self, 1)
        self.counterUsers += 1
    elif l_input.text() == "exit":
        sys.exit(0)
    elif l_input.text() == "reboot":
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 
    else:  
        __name_item = ["Неизвестный", __time_now, l_input.text()] # if input equals nothing then ERROR
        
        l_history.insertRow(0)
        l_history.setItem(0, 0, QtWidgets.QTableWidgetItem(__name_item[0]))
        l_history.setItem(0, 1, QtWidgets.QTableWidgetItem(__name_item[1]))
        l_history.setItem(0, 2, QtWidgets.QTableWidgetItem(__name_item[2]))
        l_history.item(0,0).setBackground(QtGui.QColor(120,0,0))
        l_history.item(0,1).setBackground(QtGui.QColor(120,0,0))
        l_history.item(0,2).setBackground(QtGui.QColor(120,0,0))
        l_history.item(0,0).setForeground(QtGui.QColor(255,255,255))
        l_history.item(0,1).setForeground(QtGui.QColor(255,255,255))
        l_history.item(0,2).setForeground(QtGui.QColor(255,255,255))
        
        setResult(self, 2)

    setName(self, __name_item[0])
    counterUserShow(self, l_counterUser)
    nameShow(self, l_name)
    resultShow(self, l_result)
    l_input.clear()
    pass