# -*- coding: utf-8 -*-
# @Author   : duanzhijun
# @time     : 18-7-24 16:34
# @File     : randomparameter.py


from faker import Faker
from utils.readfile import ReadYaml
from utils.base_configuration import CONFIG_PATH
import os,random


class RandomParameter(object):
    def __init__(self, language='zh_CN'):
        self.fake = Faker(language)

    def get_address(self):
        return self.fake.address()

    def get_name(self):
        # print(self.fake.first_name_male())   "名字"
        # print(self.fake.last_name_male())  "姓氏"
        return self.fake.name()

    def get_mail(self):
        # print("fake.ascii_free_email:" + self.fake.ascii_free_email())
        # print("fake.ascii_company_email:" + self.fake.ascii_company_email())
        # print("fake.company_email:" + self.fake.company_email())
        # print("fake.safe_email:" + self.fake.safe_email())
        # print("fake.ascii_safe_email:" + self.fake.ascii_safe_email())
        # print("fake.free_email:" + self.fake.free_email())
        # print("fake.free_email_domain:" + self.fake.free_email_domain())
        # print("fake.ascii_email:" + self.fake.ascii_email())
        # print("fake.email:" + self.fake.email())
        return self.fake.email()

    def get_ip(self):
        # print(self.fake.ipv4_public())
        # "private生成局域网ip"
        # print(self.fake.ipv4_private())
        # print(self.fake.ipv4())
        return self.fake.ipv4()

    def get_url(self):
        # fake.image_url()
        return self.fake.uri()

    def get_phone_num(self):
        # print(self.fake.phone_number())
        # print(self.fake.msisdn())
        return self.fake.phone_number()

    def get_id_card(self):
        # print(self.fake.ein())
        # print(self.fake.ssn())
        return self.fake.ssn()


class GetCountryCode(object):
    def __init__(self):
        self.path = os.path.join(CONFIG_PATH, 'countrycode.yml')
        self.data = ReadYaml(yaml_path=self.path).get_yaml_data()

    def get_countrycode(self, value='中国'):
        """
        获取国家对应的代码
        :param value:支持中文国家名称和英文国家名称 例：
        :return:返回元组
        """
        result = []
        for key, values in self.data[0].items():
            if str(values).lower().find(value.lower()) != -1:
                result.append(dict(key=key, value=values))
        return result

    def check_key(self, key):
        result = False
        for k in self.data[0].keys():
            if str(k) == key:
                result = True
        return result


class RandomId:
    @staticmethod
    def get_id(l):
        if isinstance(l, list):
            length = l.__len__()
            num = random.randint(0, length)
            return l[num]

    @staticmethod
    def get_num(n=0, m=1):
        num = random.randint(n, m)
        return num


if __name__ == "__main__":
    print(RandomParameter().get_address())
    print(RandomParameter().get_mail())
    u = RandomParameter('en_US')
    print(u.get_address())
    print(u.get_mail())
    s = GetCountryCode().get_countrycode('俄语')[0].get('key')
    r = RandomParameter(s)
    print(r.get_address())
    print(r.get_mail())
    # print(GetCountryCode().get_countrycode(value='台湾'))
    # print(GetCountryCode().check_key(''))
    # print(GetCountryCode().check_key('ro_RO'))
