#coding=utf-8
from port import Port
from dos_cmd import DosCmd
from opera_yaml import OperaYaml
import threading
import time

class Server:
    def __init__(self):
        self.dos=DosCmd()
        self.device_list=self.get_device_list()
        self.opera_yaml=OperaYaml()



    def get_device_list(self):
        #获取设备列表
        print 'start get devices...'
        device_list=[]
        result_list=self.dos.excute_cmd_result('adb devices')
        if len(result_list)>=2:
            for i in result_list:
                if 'List' in i:
                    continue
                device_info = i.split('\t')
                if device_info[1]=='device':
                    device_list.append(device_info[0])
            return device_list
        else:
            return None

    def create_port_list(self,start_port):
        #创建可用端口列表
        port = Port()
        port_list=port.create_port_list(start_port,len(self.device_list))
        return port_list

    def create_command_i(self,i):
        #生成命令，非命令列表
        #appium -p 4700 -bp 4900 -U deviceName
        appium_port_list=self.create_port_list(4700)
        bootstrap_port_list=self.create_port_list(4900)
        device_list=self.device_list
        command_i = 'appium -p '+str(appium_port_list[i])+' -bp '+str(bootstrap_port_list[i])+' -U '+device_list[i]+' --no-reset --session-override'
        print command_i
        self.opera_yaml.write_data(i,bootstrap_port_list[i],device_list[i],appium_port_list[i])
        return command_i

    def start_server(self,i):
        #启动服务
        self.start_command = self.create_command_i(i)
        print "start server..."
        self.dos.excute_cmd(self.start_command)

    def kill_server(self):
        print 'start kill server...'
        #停止服务
        server_list = self.dos.excute_cmd_result('tasklist | find "node.exe"')
        if len(server_list)>0:
            self.dos.excute_cmd('taskkill -F -PID node.exe')

    def main(self):
        #主函数多线程
        print 'start main server...'
        thread_list=[]
        self.kill_server()
        self.opera_yaml.clear_data()

        for i in range(len(self.device_list)):
            appium_start=threading.Thread(target=self.start_server,args=(i,))
            thread_list.append(appium_start)
        for j in thread_list:
            print 'start thread ...'
            j.start()
        time.sleep(20)

if __name__=="__main__":
    server=Server()
    server.main()