# -*- coding: utf-8 -*-
# @Author   : duanzhijun
# @time     : 18-7-23 15:08
# @File     : base_configuration.py
import hashlib
import os
import inspect
import datetime


from utils.readfile import ReadYaml


class ElementNotFound(Exception):
    """定义配置文件中变量名不存在异常"""
    pass


"""
获取项目所在的根目录
.abspath(file)：返回file的规范化路径(包括文件名及后缀名)
.dirname(file)：返回file的路径
.split(file)：分割文件名与目录，生成一个二元组(若传参不包含文件名，将最后一个目录名当作文件名分离)
"""
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
"config中存放基础配置文件"
CONFIG_PATH = os.path.join(BASE_PATH, 'config')
"log程序运行日志目录"
LOG_PATH = os.path.join(BASE_PATH, 'log')
"测试生成的测试报告目录"
RESULT_PATH = os.path.join(BASE_PATH, 'result')
"基础类存放目录"
UTILS_PATH = os.path.join(BASE_PATH, 'utils')
"系统配置文件地址"
CONFIG_YAML_PATH = os.path.join(CONFIG_PATH, 'config.yml')
# CONFIG_YAML_PATH = os.path.join(CONFIG_PATH, 'setting.yml')
"运行日志配置文件地址"
LOG_YAML_PATH = os.path.join(CONFIG_PATH, 'log.yml')


class BaseConfig:
    def __init__(self, config_path=CONFIG_YAML_PATH):
        self.config_data = ReadYaml(config_path).get_yaml_data()

    def get_config_data(self, element):
        """
        获取config配置文件中的值
        :param element:返回值字典中的key
        """
        if element not in self.config_data[0].keys():
            raise ElementNotFound('字段key：%s不存在' % element)
        return self.config_data[0].get(element)

    def get_base_info(self, t="CONDITION"):
        p = self.config_data[0]
        result = ''
        for key in p.keys():
            if key == p.get(t):
                result = p.get(key)
        return result

    def get_ids(self):
        p = self.config_data[0]
        c = p.get("CONDITION")
        result = ""
        if c == "PREVIEW":
            result = p.get("EMI")
        elif c == "EMI":
            result = p.get("PREVIEW")
        elif c == "STAGING":
            result = p.get("PREVIEW")
        return result


class GetFunctionName:
    """
    获取当前执行的方法名
    inspect.stack()获取当前执行类的名称，返回字典类型
    调用方式 "GerFunctionName().get_function_name"
    """
    @property
    def get_function_name(self):
        return inspect.stack()[1][3]


class MD5:
    def md5(self, str_text):
        """
        字符串MD5加密
        :param str_text: str类型串
        :return: 返回加密后的字符串
        """
        h = hashlib.md5()
        h.update(str_text.encode(encoding='utf-8'))
        return str(h.hexdigest())


class DictSort:
    def dictsort(self, dt=None):
        """
        字典排序类
        :param dt:字典类型参数，以字典中的key为基准排序
        :return: 返回完成排序的字典
        """
        result = {}
        if dt:
            # 排序方法,返回元组类型数据[(a,1),(b,2),(c,4)]
            mid_dict = sorted(dt.items(), key=lambda x: x[0])
            # 拆分元组数据到字典中
            for j in range(mid_dict.__len__()):
                result.update({str(mid_dict[j][0]): str(mid_dict[j][1])})
        return result


class GenerateURL:
    """
    请求的URL排序
    """
    def generate_url(self, u=None, d=None):
        """
        :param u:url即问号之前(或包括问号)的参数
        :param d:请求参数，字典类型
        :return:返回拼接完成的url字符串
        """
        url = ''
        data_md = ''
        data_uri = ''
        re_key = ''
        if u and '?' in u:
            url = u
        elif u and '?' not in u:
            url = u + '?'
        if d and isinstance(d, dict):
            d = DictSort().dictsort(d)
            for key, value in d.items():
                if key == 'signId':
                    data_md += key + MD5().md5(value)
                    data_uri += key + '=' + MD5().md5(value) + '&'
                    re_key = value
                else:
                    data_md += key + value
                    data_uri += key + '=' + value + '&'
        sign = MD5().md5(data_md + re_key)
        result = url + data_uri + 'sign=' + sign
        return result


class Time:
    def __init__(self):
        self.time = datetime.datetime.now()

    def get_datetime(self):
        return self.time.strftime("%Y-%m-%d")

    @staticmethod
    def count_datetime(date='2018-08-23', days=1):
        result_date = datetime.datetime.strptime(date, "%Y-%m-%d") + datetime.timedelta(days=days)
        return result_date.strftime("%Y-%m-%d")


if __name__ == '__main__':
    # print(BaseConfig().get_config_data('Emi_URL'))
    base_uri1 = 'http://staging.e.mi.com/openapi/creative/list?'
    base_uri = 'http://staging.e.mi.com/openapi/campaign/list?'
    data = {"customerId": "25432",
            "status": "1",
            "signId": "GLVLjBhkehGPkBuS"
            }
    # print(Time().get_datetime())
    # print(Time().count_datetime("2018-08-06", -5))
    # print(GenerateURL().generate_url(base_uri, data))
    # print(GenerateURL().generate_url(base_uri, data))
    print(BaseConfig().get_ids())
