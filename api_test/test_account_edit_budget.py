# -*- coding: utf-8 -*-
# @Author   : duanzhijun
# @time     : 18-8-7 16:04
# @File     : test_creative_info.py

import unittest
from utils.base_configuration import GenerateURL
from utils.log import Log
from utils.client import Client

from config import setting


class TestAccountEditBudget(unittest.TestCase):
    def setUp(self):
        # self.uri = BaseConfig().get_base_info().get("URI")
        # self.signId = BaseConfig().get_base_info().get("KEY")
        # self.customerId = BaseConfig().get_base_info().get("CUSTOMERID")
        self.setting = setting.get_setting()
        self.uri = self.setting['URI']
        self.signId = self.setting['KEY']
        self.customerId = self.setting['CUSTOMERID']
        self.port = 'account/edit/budget'
        self.method = 'POST'
        self.log = Log("TestAccountEditBudget").print_log()

    def test_account_edit_budget_base(self):
        data = {
            "customerId": self.customerId,
            "newDayThreshold": "500"
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url, method=self.method).send_request()
        json = request.json()
        self.assertTrue(json['success'])
        self.assertEqual(0, json['code'])

    def test_account_edit_newDayThreshold_err(self):
        data = {
            "customerId": self.customerId,
        }
        shold = ('199', '199.99', '100000001', '100000000.01', '', '  ')
        for k in range(shold.__len__()):
            data.update({"newDayThreshold": shold[k]})
            data.update({"signId": self.signId})
            url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
            request = Client(url, method=self.method).send_request()
            json = request.json()
            self.assertFalse(json['success'])
            self.assertEqual(20, json['code'])


if __name__ == '__main__':
    unittest.main()
