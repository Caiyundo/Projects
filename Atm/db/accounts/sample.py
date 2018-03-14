# -*- coding:utf-8 -*-
# Author:Wong Du

import os,sys,json
DB_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(DB_DIR)
sys.path.append(DB_DIR)
import account_sample

if __name__ == '__main__':
    print("true")
    # account_sample.main()


