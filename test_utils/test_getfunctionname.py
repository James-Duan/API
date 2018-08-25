# -*- coding: utf-8 -*-
# @Author   : duanzhijun
# @time     : 18-7-24 11:01
# @File     : test_getfunctionname.py

import unittest
from utils.base_configuration import GetFunctionName


class TestGetFunctionName(unittest.TestCase):
    def test_name(self):
        s = GetFunctionName().get_function_name
        self.assertEqual('test_name', s)


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(TestGetFunctionName))
    unittest.main()
