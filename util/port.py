# coding=utf-8
from dos_cmd import DosCmd


class Port:
    def __init__(self):
        self.dos = DosCmd()

    def port_is_usrd(self, port_num):
        '''
        判断端口是否被占用
        '''
        flag = None
        command = 'netstat -ano|findstr ' + str(port_num)
        result = self.dos.excute_cmd_result(command)
        if len(result) > 0:
            flag = True
        else:
            flag = False
        return flag

    def create_port_list(self, start_port, count):
        '''
        生成可用端口，参数起始端口号和端口个数
        '''
        port_list = []
        if count > 0:
            while len(port_list) < count:
                if self.port_is_usrd(start_port) != True:
                    port_list.append(start_port)
                start_port = start_port + 1
            return port_list
        else:
            print u"生成可用端口失败"
            return None


if __name__ == '__main__':
    port = Port()
    print port.create_port_list(4720, 5)
