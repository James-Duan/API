# -*- coding: utf-8 -*-
# @Author   : duanzhijun
# @time     : 18-8-2 21:43
# @File     : main.py
from api_test.test_account_balance import TestAccountBalance
from api_test.test_account_edit_budget import TestAccountEditBudget
from api_test.test_agent_customers import TestAgentCustomers
from api_test.test_campaign_edit_budget import TestCampaignEditBudget
from api_test.test_campaign_edit_status import TestCampaignEditStatus
from api_test.test_campaign_list import TestCampaignList
from api_test.test_campaign_info import TestCampaignInfo
from api_test.test_creative_edit_bid import TestCreativeEditBid
from api_test.test_creative_edit_status import TestCreativeEditStatus
from api_test.test_creative_getids import TestCreativeGetIds
from api_test.test_creative_info import TestCreativeInfo
from api_test.test_creative_list import TestCreativeList
from api_test.test_group_edit_status import TestGroupEditStatus
from api_test.test_group_info import TestGroupInfo
from api_test.test_group_list import TestGroupList
from api_test.test_report_audience_gender_data import TestReportGetAudienceGenderData
from api_test.test_report_audience_province_data import TestReportGetAudienceProvinceData
from api_test.test_report_getdata import TestReportGetData
from api_test.test_report_getquarterdata import TestReportGetQuarterData
from utils.base_configuration import RESULT_PATH
from utils.HTMLTestRunner import HTMLTestRunner
import os.path
import unittest


def suite():
    s = unittest.TestSuite()
    s.addTest(unittest.TestLoader().loadTestsFromTestCase(TestCampaignList))
    s.addTest(unittest.TestLoader().loadTestsFromTestCase(TestCampaignInfo))
    s.addTest(unittest.TestLoader().loadTestsFromTestCase(TestCampaignEditStatus))
    s.addTest(unittest.TestLoader().loadTestsFromTestCase(TestCampaignEditBudget))
    s.addTest(unittest.TestLoader().loadTestsFromTestCase(TestGroupList))
    s.addTest(unittest.TestLoader().loadTestsFromTestCase(TestGroupInfo))
    s.addTest(unittest.TestLoader().loadTestsFromTestCase(TestGroupEditStatus))
    s.addTest(unittest.TestLoader().loadTestsFromTestCase(TestCreativeGetIds))
    s.addTest(unittest.TestLoader().loadTestsFromTestCase(TestCreativeList))
    s.addTest(unittest.TestLoader().loadTestsFromTestCase(TestCreativeInfo))
    s.addTest(unittest.TestLoader().loadTestsFromTestCase(TestCreativeEditStatus))
    s.addTest(unittest.TestLoader().loadTestsFromTestCase(TestCreativeEditBid))
    s.addTest(unittest.TestLoader().loadTestsFromTestCase(TestReportGetQuarterData))
    s.addTest(unittest.TestLoader().loadTestsFromTestCase(TestReportGetData))
    s.addTest(unittest.TestLoader().loadTestsFromTestCase(TestReportGetAudienceProvinceData))
    s.addTest(unittest.TestLoader().loadTestsFromTestCase(TestReportGetAudienceGenderData))
    s.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAccountBalance))
    s.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAccountEditBudget))
    s.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAgentCustomers))
    return s


if __name__ == '__main__':
    # 初始化测试环境配置 ：key: EMI/STAGING
    # ReadYaml(CONFIG_YAML_PATH).set_yaml_data({'CONDITION': 'STAGING'})
    # ReadYaml(CONFIG_YAML_PATH).set_yaml_data({'DATE': Time().get_datetime()})
    report = os.path.join(RESULT_PATH, 'report.html')
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='测试结果', description='API result')
        runner.run(suite())
