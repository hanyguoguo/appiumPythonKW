#coding=utf-8
from opera_ini import OperaIni
from base.base_driver import BaseDriver
class GetByLocal:
    def __init__(self,driver):
        self.driver=driver

    def get_element(self,opetion):
        '''
        通过读取ini文件获取到的元素id>com.hospital.localtest:id/mClinicName，需要拆分出定位方式和定位值
        并根据定位方式获取元素
        '''
        opera_ini=OperaIni()
        local = opera_ini.get_value(opetion)
        if local !=None:
            by = local.split('>')[0]
            local_by = local.split('>')[1]
            try:
                if by == 'id':
                    element=self.driver.find_element_by_id(local_by)
                elif by =='className':
                    element=self.driver.find_element_by_class_name(local_by)
                else:
                    element=self.driver.find_element_by_xpath(local_by)
            except:
                element=None
        else:
            element=None
        return element


if __name__=="__main__":
    driver=BaseDriver()
    driver=driver.get_driver()
    gbl=GetByLocal()
    print gbl.get_element('pwd')