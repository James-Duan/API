# -*- coding: utf-8 -*-
# @Author   : duanzhijun
# @time     : 18-8-7 16:04
# @File     : test_creative_info.py

import unittest

from utils.randomparameter import RandomId
from config import setting
from utils.base_configuration import GenerateURL
from utils.log import Log
from utils.client import Client


class TestCreativeEditBid(unittest.TestCase):
    def setUp(self):
        # self.uri = BaseConfig().get_base_info().get("URI")
        # self.signId = BaseConfig().get_base_info().get("KEY")
        # self.customerId = BaseConfig().get_base_info().get("CUSTOMERID")
        self.setting = setting.get_setting()
        self.uri = self.setting['URI']
        self.signId = self.setting['KEY']
        self.customerId = self.setting['CUSTOMERID']
        self.creativeId = str(self.setting['CREATIVEID']).split(',')
        self.creativeId = self.creativeId[RandomId.get_num(0, len(self.creativeId)-1)]
        self.port = 'creative/edit/bid'
        self.method = 'POST'
        self.log = Log("TestCreativeEditBid").print_log()

    def test_creative_edit_bid_base(self):
        data = {
            "customerId": self.customerId,
            "creativeId": self.creativeId,
            "bidding": "{\"bid\":2,\"billingType\":1}"
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url, method=self.method).send_request()
        json = request.json()
        print(json)
        self.assertTrue(json['success'])
        self.assertEqual(0, json['code'])

    def test_creative_edit_bid_creative_error(self):
        data = {
            "customerId": self.customerId,
            "bidding": "{\"bid\":2,\"billingType\":1}"
        }
        creative = ['', '   ', RandomId.get_num(1000, 10000)]
        data.update({"signId": self.signId})
        for i in range(len(creative)):
            data.update({"creativeId": creative[i]})
            url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
            request = Client(url, method=self.method).send_request()
            json = request.json()
            print(json)
            self.assertFalse(json['success'])
            # self.assertEqual(0, json['code'])

    def test_creative_edit_bid_bid_error(self):
        data = {
            "customerId": self.customerId,
            "creativeId": self.creativeId,
            "bidding": "{\"bid\":200,\"billingType\":1}"
        }
        data.update({"signId": self.signId})
        bid = ['', '0.01', '1000', 't']
        for i in range(len(bid)):
            data.update({'bid': "{\"bid\":"+str(bid[i])+",\"billingType\":1}"})
            url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
            request = Client(url, method=self.method).send_request()
            json = request.json()
            print(json)
            self.assertFalse(json['success'])
            # self.assertEqual(0, json['code'])


if __name__ == '__main__':
    unittest.main()

