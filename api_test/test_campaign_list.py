# -*- coding: utf-8 -*-
# @Author   : duanzhijun
# @time     : 18-8-1 19:03
# @File     : test_campaign_list.py


import unittest

from config import setting
from utils.base_configuration import GenerateURL
from utils.client import Client
from utils.base_configuration import Time


class TestCampaignList(unittest.TestCase):
    def setUp(self):
        # self.uri = BaseConfig().get_base_info().get("URI")
        # self.signId = BaseConfig().get_base_info().get("KEY")
        # self.customerId = BaseConfig().get_base_info().get("CUSTOMERID")
        self.setting = setting.get_setting()
        self.uri = self.setting['URI']
        self.signId = self.setting['KEY']
        self.customerId = self.setting['CUSTOMERID']
        self.port = 'campaign/list'
        self.method = 'GET'
        self.time = Time().get_datetime()
        self.sub = -1

    def test_campaign_list_base(self):
        print("获取广告计划列表基础请求")
        data = {
            "customerId": self.customerId,
            "sdate": Time().count_datetime(self.time, self.sub),
            "edate": Time().count_datetime(self.time, self.sub)
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url, method=self.method).send_request()
        json = request.json()
        self.assertTrue(json['success'])
        self.assertEqual(str(json['code']), str(0))

    def test_campaign_list_base_customerId_empty_1(self):
        print("获取广告计划列表customerId未传")
        data = {
            # "customerId": self.customerId,
            "sdate": Time().count_datetime(self.time, self.sub),
            "edate": Time().count_datetime(self.time, self.sub)
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url, method=self.method).send_request()
        json = request.json()
        self.assertFalse(json['success'])
        self.assertEqual(str(json['code']), str(20))
        self.assertEqual(str(json['msg']), str('参数错误'))
        self.assertEqual(str(json['desc']), str('customerId参数不能为空'))

    def test_campaign_list_base_customerId_empty_2(self):
        print("获取广告计划列表customerId为空")
        data = {
            "customerId": '',
            "sdate": Time().count_datetime(self.time, self.sub),
            "edate": Time().count_datetime(self.time, self.sub)
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url, method=self.method).send_request()
        json = request.json()
        self.assertFalse(json['success'])
        self.assertEqual(str(json['code']), str(20))
        self.assertEqual(str(json['msg']), str('参数错误'))
        self.assertEqual(str(json['desc']), str('customerId参数不能为空'))

    def test_campaign_list_base_customerId_empty_3(self):
        print("获取广告计划列表customerId与singId不匹配")
        data = {
            "customerId": '123',
            "sdate": Time().count_datetime(self.time, self.sub),
            "edate": Time().count_datetime(self.time, self.sub)
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url, method=self.method).send_request()
        json = request.json()
        self.assertFalse(json['success'])
        self.assertEqual(str(json['code']), str(12))
        self.assertEqual(str(json['msg']), str('错误的sign参数'))
        self.assertEqual(str(json['desc']), str('非法的账户信息'))

    def test_campaign_list_kw(self):
        print('kw关键字正常校验')
        kw = ['', '商店', 100030663, 'hfdsajdkas', '1234hhh']
        data = {
            "customerId": self.customerId,
            # "kw": "非商店",
            "sdate": Time().count_datetime(self.time, self.sub),
            "edate": Time().count_datetime(self.time, self.sub)
        }
        data.update({"signId": self.signId})
        for i in range(len(kw)):
            data.update({"kw": kw[i]})
            url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
            request = Client(url).send_request().json()
            self.assertTrue(request['success'])
            self.assertEqual(request['code'], 0)
            r = False
            # if kw[i] != '' or not isinstance(kw[i], int):
            #     for j in range(len(request['result']['list'])):
            #         for keys, values in request['result']['list'][j].items():
            #             if request['result']['list'][j] and keys == 'name' and kw[i] in values:
            #                 r = True
            #     self.assertTrue(r)
            if request['result']['list']:
                for j in range(len(request['result']['list'])):
                    for key, value in request['result']['list'][j].items():
                        if kw[i] != '' or not isinstance(kw[i], int):
                            if key == 'name' and kw[i] in value:
                                r = True
                        if kw[i] != '' and isinstance(kw[i], int):
                            if key == 'id' and kw[i] == value:
                                r = True
                    self.assertTrue(r)

    def test_campaign_list_type(self):
        data = {
            "customerId": self.customerId,
            "type": "1",
            "sdate": Time().count_datetime(self.time, self.sub),
            "edate": Time().count_datetime(self.time, self.sub)
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url).send_request()
        self.assertEqual(200, request.status_code)

    def test_campaign_list_status(self):
        data = {
            "customerId": self.customerId,
            "status": "1",
            "sdate": Time().count_datetime(self.time, self.sub),
            "edate": Time().count_datetime(self.time, self.sub)
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url).send_request()
        self.assertEqual(200, request.status_code)

    def test_campaign_list_sdate(self):
        data = {
            "customerId": self.customerId,
            "sdate": Time().count_datetime(self.time, self.sub),
            "edate": Time().count_datetime(self.time, self.sub)
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url).send_request()
        json = request.json()
        self.assertEqual(0, json['code'])
        self.assertTrue(json['success'], msg='返回正常')

    def test_campaign_list_edate(self):
        data = {
            "customerId": self.customerId,
            "sdate": Time().count_datetime(self.time, self.sub),
            "edate": Time().count_datetime(self.time, self.sub)
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url).send_request()
        json = request.json()
        self.assertEqual(0, json['code'])
        self.assertTrue(json['success'])

    def test_campaign_list_page(self):
        data = {
            "customerId": self.customerId,
            "page": "1",
            "sdate": Time().count_datetime(self.time, self.sub),
            "edate": Time().count_datetime(self.time, self.sub)
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url).send_request()
        json = request.json()
        self.assertEqual(0, json['code'])
        self.assertTrue(json['success'])

    def test_campaign_list_pagesize(self):
        data = {
            "customerId": self.customerId,
            "pagesize": "2",
            "sdate": Time().count_datetime(self.time, self.sub),
            "edate": Time().count_datetime(self.time, self.sub)
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url).send_request()
        json = request.json()
        self.assertEqual(0, json['code'])
        self.assertTrue(json['success'])

    def test_campaign_list_orderby(self):
        data = {
            "customerId": self.customerId,
            "orderby": "viewSum",
            "sdate": Time().count_datetime(self.time, self.sub),
            "edate": Time().count_datetime(self.time, self.sub)
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url).send_request()
        json = request.json()
        self.assertEqual(0, json['code'])
        self.assertTrue(json['success'])

    def test_campaign_list_sortMode(self):
        data = {
            "customerId": self.customerId,
            "sortMode": "1",
            "sdate": Time().count_datetime(self.time, self.sub),
            "edate": Time().count_datetime(self.time, self.sub),
            "orderby": "viewSum"
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url).send_request()
        json = request.json()
        self.assertEqual(0, json['code'])
        self.assertTrue(json['success'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
    # suite = unittest.TestSuite()
    # suite.addTest(TestCampaignList("test_campaign_list_base"))
    # suite.addTest(TestCampaignList("test_campaign_list_kw"))
    # suite.addTest(TestCampaignList("test_campaign_list_type"))
    # suite.addTest(TestCampaignList("test_campaign_list_status"))
    # suite.addTest(TestCampaignList("test_campaign_list_sdate"))
    # suite.addTest(TestCampaignList("test_campaign_list_edate"))
    #
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)
