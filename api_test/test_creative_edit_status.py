# -*- coding: utf-8 -*-
# @Author   : duanzhijun
# @time     : 18-8-7 16:04
# @File     : test_creative_info.py

import unittest

from config import setting
from utils.base_configuration import GenerateURL
from utils.log import Log
from utils.client import Client
from utils.randomparameter import RandomId


class TestCreativeEditStatus(unittest.TestCase):
    def setUp(self):
        # self.uri = BaseConfig().get_base_info().get("URI")
        # self.signId = BaseConfig().get_base_info().get("KEY")
        # self.customerId = BaseConfig().get_base_info().get("CUSTOMERID")
        self.setting = setting.get_setting()
        self.uri = self.setting['URI']
        self.signId = self.setting['KEY']
        self.customerId = self.setting['CUSTOMERID']
        self.creativeId = str(self.setting['CREATIVEID']).split(',')
        self.creativeId1 = self.creativeId[RandomId.get_num(0, len(self.creativeId)-1)]
        self.creativeId2 = self.creativeId[RandomId.get_num(0, len(self.creativeId)-1)]
        self.port = 'creative/edit/status'
        self.method = 'POST'
        self.log = Log("TestCreativeEditStatus").print_log()

    def test_creative_edit_list_base(self):
        data = {
            "customerId": self.customerId,
            "creativeIds": str(self.creativeId1) + "," + str(self.creativeId2),
            "newval": "2"
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url, method=self.method).send_request()
        json = request.json()
        self.assertTrue(json['success'])
        self.assertEqual(0, json['code'])


if __name__ == '__main__':
    unittest.main()
