# -*- coding: utf-8 -*-
# @Author   : duanzhijun
# @time     : 18-8-7 15:44
# @File     : test_creative_list.py

import unittest

from config import setting
from utils.base_configuration import GenerateURL, Time
from utils.log import Log
from utils.client import Client
from utils.randomparameter import RandomId


class TestCreativeList(unittest.TestCase):
    def setUp(self):
        # self.uri = BaseConfig().get_base_info().get("URI")
        # self.signId = BaseConfig().get_base_info().get("KEY")
        # self.customerId = BaseConfig().get_base_info().get("CUSTOMERID")
        self.setting = setting.get_setting()
        self.uri = self.setting['URI']
        self.signId = self.setting['KEY']
        self.customerId = self.setting['CUSTOMERID']
        self.groupId = str(self.setting['GROUPID']).split(',')
        self.groupId = self.groupId[RandomId.get_num(0, len(self.groupId)-1)]
        self.time = Time().get_datetime()
        self.sub = -1
        self.port = 'creative/list'
        self.method = 'GET'
        self.log = Log("TestCreativeList").print_log()

    def test_creative_list_base(self):
        data = {
            "customerId": self.customerId,
            "groupId": self.groupId,
            "sdate": Time.count_datetime(self.time, self.sub),
            "edate": Time.count_datetime(self.time, self.sub)
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url, method=self.method).send_request()
        json = request.json()
        self.assertTrue(json['success'])
        self.assertEqual(0, json['code'])


if __name__ == '__main__':
    unittest.main()

