# -*- coding: utf-8 -*-
# @Author   : duanzhijun
# @time     : 18-8-3 10:19
# @File     : test_campaign_info.py

import unittest
from utils.randomparameter import RandomId
from config import setting
from utils.base_configuration import GenerateURL
from utils.client import Client


class TestCampaignInfo(unittest.TestCase):
    def setUp(self):
        # self.uri = BaseConfig().get_base_info().get("URI")
        # self.signId = BaseConfig().get_base_info().get("KEY")
        # self.customerId = BaseConfig().get_base_info().get("CUSTOMERID")
        # self.campaignId = str(BaseConfig().get_base_info().get("CAMPAIGNID")).split(',')[0]
        self.setting = setting.get_setting()
        self.uri = self.setting['URI']
        self.signId = self.setting['KEY']
        self.customerId = self.setting['CUSTOMERID']
        self.campaignId = str(self.setting['CAMPAIGNID']).split(',')
        self.campaignId = self.campaignId[RandomId.get_num(0, len(self.campaignId)-1)]
        self.port = 'campaign/info'
        self.method = 'GET'

    def test_campaign_info_base(self):
        data = {
            "customerId": self.customerId,
            "campaignId": self.campaignId
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url, method=self.method).send_request()
        json = request.json()
        self.assertTrue(json['success'])
        self.assertEqual(0, json['code'])
        self.assertEqual(str(json['result']['id']), str(data["campaignId"]))

    def test_campaign_info_without_campaignId(self):
        data = {
            "customerId": self.customerId
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url, method=self.method).send_request()
        json = request.json()
        self.assertFalse(json['success'])
        self.assertEqual(json['desc'], 'campaignId参数不能为空')


if __name__ == '__main__':
    unittest.main(verbosity=2)
