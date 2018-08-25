# -*- coding: utf-8 -*-
# @Author   : duanzhijun
# @time     : 18-7-23 14:55
# @File     : readfile.py
import os
import yaml
# from ruamel import yaml
from xlrd import open_workbook


class ReadYaml(object):
    """
    读取.yml格式文件
    返回值：list
    """
    def __init__(self, yaml_path):
        """
        :param yaml_path:yaml文件地址(包含文件名及后缀名)
        """
        if os.path.exists(yaml_path):
            self.path = yaml_path
        else:
            raise FileNotFoundError(yaml_path + "未找到文件！")
        self.data = None

    def get_yaml_data(self):
        if not self.data:
            with open(self.path, 'rb') as f:
                self.data = list(yaml.safe_load_all(f))
                # self.data = yaml.load(f, Loader=yaml.RoundTripLoader)
                f.close()
        return self.data

    def set_yaml_data(self, d=None):
        with open(self.path) as f:
            content = yaml.load(f)
        if d:
            content.update(d)
            with open(self.path, 'w') as wf:
                yaml.dump(content, wf, default_flow_style=False)


class ReadExcel(object):
    def __init__(self, excel_path, sheet=0, title_line=True):
        """
        初始化表格读取类
        :param excel_path:要读取的excel文件地址和文件名拼成的串
        :param sheet:获取工作表，支持工作表名称和工作表位置两种方式
        :param title_line:excel中是否首行为标题的标志位
        """
        if os.path.exists(excel_path):
            self.excel_path = excel_path
        else:
            raise FileNotFoundError("路径" + excel_path + "不存在！")
        self.sheet = sheet
        self.title_line = title_line
        self.data = list()

    def get_excel_data(self):
        """
        zip()函数用于合并列表，并创建一个元组对列表
        例:   a=[1,2,3] b=[4,5,6,7] list(zip(a,b)) >>>[(1,4),(2,5),(3,6)]
        """
        data = ''
        if not self.data:
            workbook = open_workbook(self.excel_path)
            if type(self.sheet) not in [int, str]:
                raise workbook.SheetTypeReeor("请输入int/str类型！现在类型为%s" .format(type(self.sheet)))
            elif type(self.sheet) == int:
                data = workbook.sheet_by_index(self.sheet)
            else:
                data = workbook.sheet_by_name(self.sheet)
        if self.title_line:
            title = data.row_values(0)
            for col in range(1, data.nrows):
                self.data.append(dict(zip(title, data.row_values(col))))
        else:
            for col in range(0, data.nrows):
                self.data.append(data.row_values(col))
        return self.data


if __name__ == '__main__':
    path = os.path.join('D:\python_work\API_test\config', 'api.xlsx')
    print(ReadExcel(excel_path=path).get_excel_data())
    pass
