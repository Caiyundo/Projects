# -*- coding:utf-8 -*-
# Author:Wong Du

'''
本程序配置文件
定义文件数据类型，配置了账户文件路径变量
定义账户交易类型、操作类型及交易手续费等
'''

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = {
    'engine':'file_storage',
    'account_name':'accounts',
    'path':'%s/db' %BASE_DIR,
}

TRANSLATION_TYPE = {
    'repay':{'action':'plus','scale':0},
    'withdraw': {'action': 'minus', 'scale': 0.05},
    'transfer': {'action': 'minus', 'scale': 0.01},
    # 'repay': {'action': 'plus', 'scale': 0},
}