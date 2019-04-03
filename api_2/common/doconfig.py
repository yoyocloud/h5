#coding=utf-8
import configparser
from configparser import ConfigParser

class deConfig:
    def __init__(self,file_name):
        #创建对象调用这个类
        self.cf=ConfigParser()
        #用这个类的对象方法read去打开配置文件，因为必须要打开一个配置文件所以放在初始化中
        self.cf.read(file_name,encoding="utf-8")
        #取值
    def read_config(self,section,option):

        value=self.cf.get(section,option)
        return value

if __name__ == '__main__':
    de=deConfig("/Users/didi/day_0214/api_2/test_case/excel_config.config")
    print(de.read_config("case","button"))






