# -*- coding: utf-8 -*-
# @Author   : duanzhijun
# @time     : 18-8-7 16:04
# @File     : test_creative_info.py

import unittest

from config import setting
from utils.base_configuration import GenerateURL, Time
from utils.log import Log
from utils.client import Client
from utils.randomparameter import RandomId


class TestReportGetQuarterData(unittest.TestCase):
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
        self.port = 'report/getQuarterData'
        self.method = 'GET'
        self.log = Log("TestReport").print_log()
        self.time = Time().get_datetime()
        self.sub = -1

    def test_report_getquarterdata_base(self):
        data = {
            "customerId": self.customerId,
            "creativeIds": self.creativeId1,
            "date": Time().count_datetime(self.time, self.sub)
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url, method=self.method).send_request()
        json = request.json()
        self.assertTrue(json['success'])
        self.assertEqual(0, json['code'])

    def test_report_getquarterdata_creatives(self):
        data = {
            "customerId": self.customerId,
            "creativeIds": self.creativeId1 + ',' + self.creativeId2,
            "date": Time().count_datetime(self.time, self.sub)
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url, method=self.method).send_request()
        json = request.json()
        self.assertTrue(json['success'])
        self.assertEqual(0, json['code'])


if __name__ == '__main__':
    unittest.main()
