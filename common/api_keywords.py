import json
import allure
import jsonpath
import requests
from common.logs import log

"""
    这是接口关键字驱动类，用于提供自动化接口测试的关键字方法。
    主要实现常用的关键字内容，并定义好所有的参数内容即可
"""


class ApiKey:

    # 基于jsonpath获取数据的关键字：用于提取所需要的内容
    @allure.step("获取返回结果字典值")
    def get_text(self, res_data, key):
        """
        :param res_data: json：需要提取数据的接口响应报文
        :param key: string：jsonpath表达式，成功则返回list，失败则返回false
        :return: list：返回提取的数据
        """
        dict_data = json.loads(res_data)  # jsonpath接收的是dict类型的数据，loads是将json格式的内容转换为字典的格式
        return jsonpath.jsonpath(dict_data, key)

    @allure.step("发送get请求")
    def get(self, url, params=None, **kwargs):
        """
        :param url: 请求地址
        :param params: 请求参数,params可能存在无值的情况，存放默认None
        :param kwargs: 请求头/cookies/headers等参数，如：requests.post(url, json=payload, headers=headers)
        :return: 接口响应体
        """
        try:
            response_body = requests.get(url=url, params=params, **kwargs)
            log.info(f'发送GET请求!!!请求参数= {params},请求头及其他= {kwargs}')
            return response_body
        except Exception as e:
            log.error(f"GET请求发送失败，失败原因：{e}")

    @allure.step("发送post请求")
    def post(self, url, body=None, **kwargs):
        """
        :param url: 请求地址
        :param body: 请求体,data可能存在无值的情况，存放默认None
        :param kwargs: 请求头/cookies/headers等参数，如：requests.post(url, json=payload, headers=headers)
        :return: 接口响应体
        """
        try:
            response_body = requests.post(url=url, data=body, **kwargs)
            log.info(f"发送POST请求!!!请求参数= {body},请求头及其他= {kwargs}")
            return response_body
        except Exception as e:
            log.error(f"POST请求发送失败，失败原因：{e}")



if __name__ == '__main__':
    ak = ApiKey()
    # res = ak.get(url='http://39.98.138.157:5000/api/getuserinfo',timeout=0.1)
    # print(res.text)
    data = {
        "username": "admin",
        "password": "123456"
    }

    res2 = ak.post(url='http://39.98.138.157:5000/api/login', json=data)
    re_data = res2.text
    print('re_data= ', re_data)
    print(ak.get_text(re_data, '$.info.[age,name]'))