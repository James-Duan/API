# -*- coding: utf-8 -*-
# @Author   : duanzhijun
# @time     : 18-8-3 20:55
# @File     : test_campaign_edit_budget.py

import unittest
from utils.base_configuration import GenerateURL
from utils.randomparameter import RandomId
from utils.log import Log
from utils.client import Client

from config import setting


class TestCampaignEditBudget(unittest.TestCase):
    def setUp(self):
        # self.uri = BaseConfig().get_base_info().get("URI")
        # self.signId = BaseConfig().get_base_info().get("KEY")
        # self.customerId = BaseConfig().get_base_info().get("CUSTOMERID")
        # self.campaignId = str(BaseConfig().get_base_info().get("CAMPAIGNID")).split(',')
        self.setting = setting.get_setting()
        self.uri = self.setting['URI']
        self.signId = self.setting['KEY']
        self.customerId = self.setting['CUSTOMERID']
        self.campaignId = str(self.setting['CAMPAIGNID']).split(',')
        # print(self.campaignId)
        self.port = 'campaign/edit/budget'
        self.method = 'POST'
        self.log = Log("TestCampaignEditBudget").print_log()

    def test_campaign_edit_budget_base(self):
        data = {
            "customerId": self.customerId,
            "campaignId": self.campaignId[RandomId.get_num(m=len(self.campaignId))-1],
            "newval": "1000"
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url, method=self.method).send_request()
        json = request.json()
        self.assertTrue(json['success'])
        self.assertEqual(0, json['code'])
        self.assertEqual(str(data['newval']), str(json['result']))

    def test_campaign_edit_budget_campaignid(self):
        data = {
            "customerId": self.customerId,
            "campaignId": RandomId.get_num(1000, 100000),
            "newval": "1000"
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url, method=self.method).send_request()
        json = request.json()
        self.assertFalse(json['success'])

    def test_campaign_edit_budget_newval(self):
        data = {
            "customerId": self.customerId,
            "campaignId": self.campaignId[RandomId.get_num(m=len(self.campaignId))-1],
        }
        data.update({"signId": self.signId})
        n = ('-1', '199', '199.9', '100000000.99', '100000001', '', ' ')
        for k in n:
            data.update({"newval": k})
            url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
            request = Client(url, method=self.method).send_request()
            json = request.json()
            self.assertFalse(json['success'])
            print(json)


if __name__ == '__main__':
    unittest.main()
