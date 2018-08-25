# -*- coding: utf-8 -*-
# @Author   : duanzhijun
# @time     : 18-8-7 22:47
# @File     : api_sigle_test.py

import unittest
from utils.base_configuration import GenerateURL, BaseConfig
from utils.log import Log
from utils.client import Client


class TestAccountBalance(unittest.TestCase):
    def setUp(self):
        self.uri = BaseConfig().get_base_info().get("URI")
        # self.signId = BaseConfig().get_base_info().get("KEY")
        self.signId = 'bjEcvVYqqHAWjrDw'
        # self.signId = 'ljkgTgVFYExewpCm'
        # self.customerId = BaseConfig().get_base_info().get("CUSTOMERID")
        # self.customerId = '68631'
        self.customerId = '39382'
        self.port = 'campaign/list'
        self.method = 'GET'
        self.log = Log("TestAccountBalance").print_log()

    def test_single(self):
        data = {
            "customerId": self.customerId,
            # "customerId": "12",
            # "campaignIds": "100000098,100000711,100001265",
            "kw": "100038745",
            "sdate": "2018-07-16",
            "edate": "2018-07-16"
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url, method=self.method).send_request()
        j = request.json()
        # print(j)
        print(j)
        for i in range(len(j['result']['list'])):
            for key, values in j['result']['list'][i].items():
                print(str(key) + ": " + str(values))
            print('\n')
        # print(j['msg'])
        print(j['result']['list'])


if __name__ == "__main__":
    unittest.main()
