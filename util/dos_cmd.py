#coding=utf-8
import os
class DosCmd:

    def excute_cmd(self,command):
        #执行dos命令，不输出结果
        os.system(command)


    def excute_cmd_result(self,command):
        #执行dos命令，并获取结果
        result_list=[]
        result =os.popen(command).readlines()
        for i in result:
            if i=='\n':
                continue
            result_list.append(i.strip('\n'))
        return result_list




if __name__=="__main__":
    dos_cmd=DosCmd()
    # dos_cmd.excute_cmd('adb tcpip 5557')
    # dos_cmd.excute_cmd('adb connect 192.168.31.34:5557')
    print dos_cmd.excute_cmd_result('adb devices')
    # device_list=[]
    # result_list=dos_cmd.excute_cmd_result('adb devices')
    # if len(result_list)>=2:
    #     for i in result_list:
    #         if 'List' in i:
    #             continue
    #         device_info = i.split('\t')
    #         if device_info[1]=='device':
    #             device_list.append(device_info[0])
    #     print device_list
    # else:
    #     print None
