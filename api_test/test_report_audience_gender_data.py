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


class TestReportGetAudienceGenderData(unittest.TestCase):
    def setUp(self):
        # self.uri = BaseConfig().get_base_info().get("URI")
        # self.signId = BaseConfig().get_base_info().get("KEY")
        # self.customerId = BaseConfig().get_base_info().get("CUSTOMERID")
        self.setting = setting.get_setting()
        self.uri = self.setting['URI']
        self.signId = self.setting['KEY']
        self.customerId = self.setting['CUSTOMERID']
        self.campaignId = str(self.setting['CAMPAIGNID']).split(',')
        self.campaignId1 = self.campaignId[RandomId.get_num(0, len(self.campaignId)-1)]
        self.campaignId2 = self.campaignId[RandomId.get_num(0, len(self.campaignId)-1)]
        self.time = Time().get_datetime()
        self.sub = -1
        self.port = 'report/audienceGenderData'
        self.method = 'GET'
        self.log = Log("TestReportGetAudienceGenderData").print_log()

    def test_report_audience_gender_data_base(self):
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
        self.assertEqual(0, json['code'])

    def test_report_audience_gender_data_campaign(self):
        data = {
            "customerId": self.customerId,
            "sdate": Time().count_datetime(self.time, self.sub),
            "edate": Time().count_datetime(self.time, self.sub),
            "campaignIds": self.campaignId1
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url, method=self.method).send_request()
        json = request.json()
        self.assertTrue(json['success'])
        self.assertEqual(0, json['code'])

    def test_report_audience_gender_data_campaigns(self):
        data = {
            "customerId": self.customerId,
            "sdate": Time().count_datetime(self.time, self.sub),
            "edate": Time().count_datetime(self.time, self.sub),
            "campaignIds": self.campaignId1 + ',' + self.campaignId2
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url, method=self.method).send_request()
        json = request.json()
        self.assertTrue(json['success'])
        self.assertEqual(0, json['code'])


if __name__ == '__main__':
    unittest.main()
