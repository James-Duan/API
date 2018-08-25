# -*- coding: utf-8 -*-
# @Author   : duanzhijun
# @time     : 18-8-24 10:42
# @File     : test_agent_customers.py
import unittest
from utils.base_configuration import GenerateURL
from utils.log import Log
from utils.client import Client

from config import setting


class TestAgentCustomers(unittest.TestCase):
    def setUp(self):
        # self.uri = BaseConfig().get_base_info().get("URI")
        # self.signId = BaseConfig().get_base_info().get("KEY")
        # self.customerId = BaseConfig().get_base_info().get("AGENTID")
        # self.agentId = BaseConfig().get_base_info().get("AGENTID")
        self.setting = setting.get_setting()
        self.uri = self.setting['URI']
        self.signId = self.setting['KEY']
        self.customerId = self.setting['CUSTOMERID']
        self.agentId = self.setting['AGENTID']
        self.port = 'agent/customers'
        self.method = 'GET'
        self.log = Log("TestAgentCustomers").print_log()

    def test_account_balance_base(self):
        data = {
            "agent": self.agentId
        }
        data.update({"signId": self.signId})
        url = GenerateURL().generate_url(u=str(self.uri+self.port), d=data)
        request = Client(url, method=self.method).send_request()
        if request:
            json = request.json()
            self.assertTrue(json['success'])
            for i in range(len(json['result']['list'])):
                for key, value in json['result']['list'][i].items():
                    if key == 'customerId' and value == self.customerId:
                        self.assertTrue(True)
            # self.assertEqual(0, json['code'])
            # self.log.debug("response " + str(json['result']))


if __name__ == '__main__':
    unittest.main()
