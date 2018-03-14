# -*- coding:utf-8 -*-
# Author:Wong Du

import time
from core import accounts

def acc_login(user_data):
    '''
    进行用户登录时调用此函数，用来处理用户登录信息，
    形参引用用户标志信息，登录成功变更标志信息，且返回用户数据
    若3次登录失败，则锁定账户
    :param user_data:
    :return:
    '''
    retry_count = 0
    while user_data['is_authorized'] is not True and retry_count < 3:
        account = input("\033[32;1mAccount:\033[0m").strip()
        data = accounts.load_current_account(account)
        password = input("\033[32;1mPassword:\033[0m").strip()
        auth = acc_auth(data,password)
        if auth:    #有返回值代表auth验证成功，否则不成功
            user_data['is_authorized'] = True
            user_data['account_id'] = account
            return auth
        retry_count += 1
    else:
        acc_lock(account)

def acc_auth(data,password):
    '''
    验证账户密码时调用此函数，进行账户认证，认证成功，返回用户数据
    :param account:
    :param password:
    :return:
    '''
    # data = accounts.load_current_account(account)

    if password == data['password']:
        empire_time = time.mktime(time.strptime(data['empire_date'],"%Y-%m-%d"))
        if time.time() < empire_time:
            return data
        else:
            print("The card is empired...")
    else:
        print("Invalid password...")

def acc_lock(acc_id):
    '''
    用户账户连续输错3次密码时调用此函数，
    用以锁定信用卡账户id
    :param acc_id:
    :return:
    '''
    lock_data = accounts.load_current_account(acc_id)
    lock_data['status'] = 1
    accounts.dump_update(lock_data)
    exit("The account is locked!!!")

