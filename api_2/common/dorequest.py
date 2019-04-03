#coding=utf-8
import requests
class deRequest:
    def http_request(self,method,url,data):
        if method.lower()=="get":
            #try...except..一般是在传递数据的代码块加入,raise把异常抛出
            try:
                resp=requests.get(url,params=data)
            except Exception as e:
                print("请求报错了{}".format(e))
                raise e
            # finally:
            #     print("你好")

        elif method.lower()=="post":
            try:
                resp=requests.post(url,data=data)
            except Exception as e:
                print("请求报错了{}".format(e))
                raise e
        else:
            print("请求方式不对")
        return resp
if __name__ == '__main__':
    dr=deRequest()
    url="http://www.baiu.com"
    data=None
    a=dr.http_request("get",url,data)
    print(a)
