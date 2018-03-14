# -*- coding:utf-8 -*-
# Author:Wong Du

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
sys.path.insert(0,BASE_DIR)

from conf import settings

db_dict = settings.DATABASE
print(db_dict['path'])
path = '%s/%s/*' %(db_dict['path'],db_dict['account_name'])
