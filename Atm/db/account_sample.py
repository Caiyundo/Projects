# -*- coding:utf-8 -*-
# Author:Wong Du

import json

acc_dict = {
    'id':4321,
    'password':'abc',
    'credit':200000,
    'quota':89000,
    'enroll_date':'2018-11-12',
    'empire_date':'2026-11-12',
    'pay_date':22,
    'status':0       #0:normal, 1:locked, 2:disabled
}

print(json.dumps(acc_dict))

with open('%s.json' %acc_dict['id'],'w') as f:
    json.dump(acc_dict,f)


