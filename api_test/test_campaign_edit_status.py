# -*- coding: utf-8 -*-
# @Author   : duanzhijun
# @time     : 18-8-3 20:24
# @File     : test_campaign_edit_status.py

import unittest
from utils.base_configuration import GenerateURL
from utils.log import Log
from utils.client import Client

from config import setting
from utils.randomparameter import RandomId


class TestCampaignEditStatus(unittest.TestCase):
    def setUp(self):
        # self.uri = BaseConfig().get_base_info().get("URI")
        # self.signId = BaseConfig().get_base_info().get("KEY")
        # self.customerId = BaseConfig().get_base_info().get("CUSTOMERID")
        # self.campaignId = str(BaseConfig().get_base_info().get("CAMPAIGNID"))
        self.setting = setting.get_setting()
        self.uri = self.setting['URI']
        self.signId = self.setting['KEY']
        self.customerId = self.setting['CUSTOMERID']
        self.campaignId = self.setting['CAMPAIGNID']
        self.port = 'campaign/edit/status'
        self.method = 'POST'
        self.log = Log("TestCampaignEditStatus").print_log()

    def test_campaign_edit_status_base(self):
        self.campaignId = str(self.campaignId).split(',')
        data = {
            "customerId": self.customerId,
            "campaignIds": self.campaignId[RandomId.get_num(0, len(self.campaignId))],
            # "campaignIds": "100038746",
            "newval": "1"
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url, method=self.method).send_request()
        json = request.json()
        self.assertTrue(json['success'])
        self.assertEqual(0, json['code'])

    def test_campaign_edit_status_more_campaignid(self):
        data = {
            "customerId": self.customerId,
            "campaignIds": self.campaignId,
            "newval": "2"
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url, method=self.method).send_request()
        json = request.json()
        self.assertTrue(json['success'])
        self.assertEqual(0, json['code'])
        self.assertTrue(str(json['result'][0]['id']) in data['campaignIds'])


if __name__ == '__main__':
    unittest.main()

