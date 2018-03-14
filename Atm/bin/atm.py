# -*- coding:utf-8 -*-
# Author:Wong Du


"""
本python文件是普通用户运行接口
用以运行整个ATM信用卡程序
功能：定义程序基础环境变量，调用atm运行程序
"""
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import main

if __name__ == '__main__':
    main.run()
