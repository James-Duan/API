# -*- coding: utf-8 -*-
# @Author   : duanzhijun
# @time     : 18-8-24 18:50
# @File     : test.py

import unittest
from utils.base_configuration import GenerateURL, BaseConfig
from utils.log import Log
from utils.client import Client


class Test(unittest.TestCase):
    def setUp(self):
        self.uri = 'http://e.mi.com/openapi/'
        self.signId = 'HyASGBRpjkmwqdmo'
        self.customerId = '112651'
        self.port = 'campaign/list'
        self.method = 'GET'
        self.log = Log("TestCreativeList").print_log()

    def test_creative_test(self):
        data = {
            "customerId": self.customerId,
            "sdate": "2018-08-05",
            "edate": "2018-08-05"
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        print(url)
        request = Client(url, method=self.method).send_request()
        json = request.json()
        print(json)
        self.assertTrue(json['success'])
        self.assertEqual(0, json['code'])
        self.log.debug("response " + str(json['result']))


if __name__ == '__main__':
    unittest.main()
