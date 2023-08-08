# -*- coding: utf-8 -*-
# XML logic for create data base users.

__author__ = 'Novotorzhin V.'
__company__ = 'AsiaAgroFood JSC'

import xml.etree.ElementTree as xml
from datetime import datetime
import os, config



class DataBase():

    def __init__(self):
        self.__current_time = datetime.now().strftime('%d-%m-%Y')
        if os.path.isfile(str(config.path_db_local) + self.__current_time + ".xml"):
            __file = xml.parse(str(config.path_db_local) + self.__current_time + ".xml")
            self.__root = __file.getroot()
        else:
            self.__root = xml.Element('data')

    def add_user(self, data) -> None:
        """Add in root Tree, data about user;
            
                @param list data: data about user, data must be [firstname='', midname='', lastname='', time='', proxycode='', tabnumber=''];
        """
        __user = xml.SubElement(self.__root, 'user')
        __firstname = xml.SubElement(__user, 'firstname')
        __firstname.text = data[0]
        __midname = xml.SubElement(__user, "midname")
        __midname.text = data[1]
        __lastname = xml.SubElement(__user, "lastname")
        __lastname.text = data[2]
        __time = xml.SubElement(__user,"time")
        __time.text = data[3]
        __proxycode = xml.SubElement(__user, "proxycode")
        __proxycode.text = data[4]
        __tabnumber = xml.SubElement(__user, "tabnumber")
        __tabnumber.text = data[5]
        
        pass

    def save(self):
        self.indent(self.__root)
        __database = xml.tostring(self.__root)
        file = open(str(config.path_db_local) + self.__current_time + ".xml","wb")
        file.write(__database)

    def indent(self, elem, level=0):
        """ by gil9red
        """
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.indent(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i