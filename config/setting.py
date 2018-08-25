# -*- coding: utf-8 -*-
# @Author   : duanzhijun
# @time     : 18-8-24 20:04
# @File     : setting.py
CURRENT_SETTING = 'emi'
EMI = {
    'AGENTID': '6191',
    'CAMPAIGNID': '100038745,100038746,100038747',
    'CREATIVEID': '100210616,100210617,100210618,100210619,100210620,100210621,100210622,100210623,100210624,100210625,'
                  '100210626,100210627',
    'CUSTOMERID': '39382',
    'GROUPID': '100065486,100065487,100065488,100065489,100065490,100065491,100065492,100065493,100065494',
    'KEY': 'bjEcvVYqqHAWjrDw',
    'URI': 'http://api.e.mi.com/'
}

PREVIEW = {}

STAGING = {
    'AGENTID': '4706',
    'CAMPAIGNID': '100030600,100030570,100030569,100030568',
    'CREATIVEID': '100003034,100002765,100002752',
    'CUSTOMERID': '25432',
    'GROUPID': '100002940,100002939,100002850,100002756',
    'KEY': 'oecnejUCDvupZCUD',
    'URI': 'http://staging.e.mi.com/openapi/'
}


def get_setting():
    if CURRENT_SETTING == 'staging':
        return STAGING
    elif CURRENT_SETTING == 'emi':
        return EMI
    elif CURRENT_SETTING == 'preview':
        return PREVIEW
