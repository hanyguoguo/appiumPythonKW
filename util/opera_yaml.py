#coding=utf-8
import yaml

class OperaYaml:
    def __init__(self,file_path=None):
        if file_path==None:
            self.file_path='E:\\pyAppium\\appiumPythonKW\\config\\userconfig.yaml'
        else:
            self.file_path=file_path
        self.data = self.read_yaml()

    def read_yaml(self):
        #加载yaml数据
        with open(self.file_path) as fr:
            data = yaml.load(fr)
        return data

    def get_lines(self):
        #获取行数
        data = self.read_yaml()
        if data!=None:
            return len(data)
        else:
            return 0


    def get_value(self,key,port):
        #获取value
        #user_info_0: {bp: '4916', deviceName: '127.0.0.1:21503', port: '4700'}
        value =self.data[key][port]
        return value

    def write_data(self,i,bp,device,port):
        #写入数据
        data= self.join_data(i,bp,device,port)
        with open(self.file_path,'a') as fr:
            yaml.dump(data,fr)

    def join_data(self,i,bp,device,port):
        #拼接数据，使符合格式user_info_0: {bp: '4916', deviceName: '127.0.0.1:21503', port: '4700'}
        data={
            "user_info_"+str(i):{
                "bp":bp,
                "deviceName":device,
                "port":port
            }
        }
        return data

    def clear_data(self):
        with open(self.file_path,'w') as fr:
            fr.truncate()
        fr.close()

if __name__ == '__main__':
    oy = OperaYaml()
    print oy.get_lines()
    # print oy.clear_data()
    # oy.write_data(1,4900,'xxxx',4700)
    # print oy.get_value('user_info_1','port')