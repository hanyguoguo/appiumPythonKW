#coding=utf-8

import ConfigParser
import os

class OperaIni:
    def __init__(self,file_path=None):
        if file_path==None:
            self.file_path='E:\\pyAppium\\appiumPythonKW\\config\\LocalElement.ini'
        else:
            self.filepath=file_path
        self.data = self.read_ini()

    def read_ini(self):
        cf = ConfigParser.ConfigParser()
        cf.read(self.file_path)
        return cf

    def get_value(self,option,section=None):
        if section==None:
            section='hospital_login'
        try:
            value = self.data.get(section,option)
        except:
            # print u"没有找到元素定位信息"
            value=None
        return value


if __name__=="__main__":
    read_ini = OperaIni()
    print read_ini.file_path
    print read_ini.get_value("username")
    print read_ini.get_value('pwd')
    # print "E:\\pyAppium\\appiumPythonPO\\config\\LocalElement.ini"