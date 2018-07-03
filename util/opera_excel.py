# coding=utf-8

import xlrd
from xlutils.copy import copy


class OperaExcel:
    def __init__(self, file_path=None, sheet_index=None):
        if file_path == None:
            self.file_path = 'E:/pyAppium/appiumPythonKW/config/case.xls'
        else:
            self.file_path = file_path
        if sheet_index == None:
            sheet_index = 0

        self.excel = self.get_excel()
        self.data = self.get_sheets(sheet_index)

    def get_excel(self):
        # 获取excel
        excel = xlrd.open_workbook(self.file_path)
        return excel

    def get_sheets(self,sheet_index):
        # 获取某个sheet的内容
        tables = self.excel.sheets()[sheet_index]
        return tables

    def get_lines(self):
        # 获取行数
        lines = self.data.nrows
        return lines

    def get_cell(self, row, col):
        value = self.data.cell(row, col).value
        return value

    def write_value(self, row, value):
        rbook = self.get_excel()      #读取excel文件，只能读取内容无法读取excel格式信息
        wbook = copy(rbook)                    #复制excel
        wsheet = wbook.get_sheet(0)            #通过get_sheet()获取的sheet有write()方法
        wsheet.write(row, 8, value)         #在sheet 0的第row行第9列写入value
        wbook.save(self.file_path)

if __name__ == "__main__":
    oe=OperaExcel()
    oe.write_value(4,'world')
