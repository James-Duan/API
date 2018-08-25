# -*- coding: utf-8 -*-
# @Author   : duanzhijun
# @time     : 18-7-24 16:04
# @File     : client.py


import requests
from utils.log import Log
from datetime import datetime
import traceback
import os.path
from requests.exceptions import RequestException
import time

METHOD = {'GET', 'POST'}


class UnKnowMethod(Exception):
    """继承异常类，主要用于校验输入的请求方式不一致"""
    pass


class Client(object):
    def __init__(self, base_url, method='GET', headers=None, cookies=None):
        """
        :param method: 请求方式，类型要与METHOD中的一致
        :param base_url: 请求地址like:1."http://e.mi.com/get" 2."http://e.mi.com/get?customerId=3306&creativeId=1000789"
        :param headers: 请求的headers参数,入参类型为字典(dict)
        :param cookies: 请求的cookies参数,入参类型为字典(dict)
        """
        self.url = base_url
        if method in METHOD:
            self.method = method
        else:
            raise UnKnowMethod('不能识别参数%s' % method)
        self.header = headers
        self.cookie = cookies
        # 声明日志类
        self.log = Log('httpclient').print_log()
        # 新建会话
        self.session = requests.session()
        self.set_session_headers(self.header)
        self.set_session_cookies(self.cookie)
        # 获取调用函数的名字
        self.module_name = traceback.extract_stack()[-2][2]
        # 获取调用函数所在文件的文件名
        self.module_file = os.path.basename(str(traceback.extract_stack()[-2][0]))

    def send_request(self, params=None, data=None, timeout=20, remark='', **kwargs):
        """
        用于单次请求
        :param remark: 备注
        :param params:关键字参数，字典类型(dict) like：{'key1':'values1', 'key2':['values2', 'values3']}
               requests会自动与URL拼装，得：http://e.mi.com/get?key1=values1&key2=values2&key2=values3
        :param data:post请求发送表单数据参数，字典类型(dict)
        :param timeout:设置请求超时时间，防止服务器无响应，程序仍在等待中
        :param kwargs:其余参数
        :return:返回request对象
        """
        response = ''
        msg = ''
        desc = ''
        if self.method == 'GET':
            start_time = datetime.utcnow()
            try:
                response = requests.get(url=self.url, headers=self.header, cookies=self.cookie,
                                        params=params, data=data, timeout=timeout, **kwargs)
            except RequestException:
                return None
            time.sleep(0.02)
            end_time = datetime.utcnow()
            sub_time = end_time - start_time
            result = response.json()
            if response.status_code == 200:
                if 'msg' in result:
                    msg = result['msg']
                if 'desc' in result:
                    desc = result['desc']
                self.log.debug('>File:%s Module:%s Method:GET Success:%s Code:%s Msg:%s Desc:%s Time_Cost:%s \n URL:%s'
                               % (self.module_file, self.module_name, result['success'], result['code'],
                                  msg, desc, sub_time, response.url))
                response.encoding = 'utf-8'
            else:
                # print(response.text)
                self.log.debug('error :%s' % response.text)
                return None
        elif self.method == 'POST':
            start_time = datetime.utcnow()
            try:
                response = requests.post(url=self.url, headers=self.header, cookies=self.cookie,
                                         params=params, data=data, timeout=timeout, **kwargs)
            except RequestException:
                return None
            time.sleep(0.02)
            end_time = datetime.utcnow()
            sub_time = end_time - start_time
            result = response.json()
            if response.status_code == 200:
                if 'msg' in result:
                    msg = result['msg']
                if 'desc' in result:
                    desc = result['desc']
                self.log.debug('>File:%s Module:%s Method:GET Success:%s Code:%s Msg:%s Desc:%s Time_Cost:%s URL:%s' % (
                    self.module_file, self.module_name, result['success'], result['code'], msg, desc, sub_time,
                    response.url))
                response.encoding = 'utf-8'
            else:
                # print(response.text)
                self.log.debug('error :%s' % response.text)
                return None
        return response

    def send_session(self, params=None, data=None, timeout=1, **kwargs):
        """
        使用session会话请求，特点：会话可记忆设置的headers及cookies
        :param params: 关键字参数
        :param data: form类型数据
        :param timeout: 超时
        :param kwargs:
        :return:返回session会话，自由变更cookies和headers
        """
        start_time = datetime.utcnow()
        response = self.session.request(method=self.method, url=self.url, params=params,
                                        data=data, timeout=timeout, **kwargs)
        end_time = datetime.utcnow()
        sub_time = end_time - start_time
        self.log.debug('Execute>> method:%s code:%s time_cost:%s URL:%s' % (self.method, response.status_code,
                                                                            sub_time, response.url))
        response.encoding = 'utf-8'
        return response

    def set_session_headers(self, headers):
        """设置会话的headers"""
        if headers:
            self.session.headers.update(headers)

    def set_session_cookies(self, cookies):
        """设置会话的cookies"""
        if cookies:
            self.session.cookies.update(cookies)


if __name__ == '__main__':
    a = {'a': '1', 'b': '2'}
    print(type(a), a.get('b'))
    if type(a) == dict:
        print('write')
