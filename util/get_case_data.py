# coding=utf-8
from opera_excel import OperaExcel
from get_by_local import GetByLocal
from base.base_driver import BaseDriver
class GetCaseData:
    def __init__(self,i):
        # base_driver=BaseDriver()
        # self.driver=base_driver.get_driver()
        self.opera_excel = OperaExcel()
        self.get_by_local=GetByLocal(i)

    def get_case_lines(self):
        # 获取用例行数
        lines = self.opera_excel.get_lines()
        print u"用例行数为: " + str(lines)
        return lines

    def get_handle_step(self, row):
        # 获取操作步骤
        res = self.opera_excel.get_cell(row, 3)
        print u"操作步骤：" + res
        return res

    def get_element_key(self, row):
        # 获取操作元素的key,并非真正的页面元素
        res = self.opera_excel.get_cell(row, 4)
        if res == ' ':
            res= None
        print u"操作元素: "+res
        return res

    def get_handle_value(self, row):
        # 获取操作值
        res = self.opera_excel.get_cell(row, 5)
        if res == ' ':
            res= None
        print u"操作值: "+res
        return res

    def get_except_element(self, row):
        # 获取预期元素
        res = self.opera_excel.get_cell(row, 6)
        if res == ' ':
            res= None
        print u"预期元素: "+res
        return res

    def get_except_step(self, row):
        # 获取预期步骤
        res = self.opera_excel.get_cell(row, 7)
        if res == ' ':
            res = None
        print u"预期步骤: "+res
        return res

    def write_value(self,row,value):
        #写入数据
        self.opera_excel.write_value(row,value)

if __name__ == "__main__":
    gcd = GetCaseData()
    gcd.get_case_lines()
    gcd.get_handle_step(2)
    gcd.get_element_key(2)
    gcd.get_handle_value(2)
    gcd.get_except_element(2)
    gcd.get_except_step(2)
