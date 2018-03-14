# -*- coding:utf-8 -*-
# Author:Wong Du

from conf import settings
from core import accounts

def make_translation(tran_type,amount,account_data):
    '''
    信用卡交易时调用此函数
    此函数为信用卡交易接口，用以进行交易操作
    交易成功，返回交易后的账户信息数据
    :param tran_type: 交易类型
    :param amount: 交易金额
    :param account_data: 账户信息
    :return:
    '''
    amount = float(amount)
    old_quota = account_data['quota']
    tran_data = settings.TRANSLATION_TYPE
    interst = amount * tran_data[tran_type].get('scale')
    if tran_type in tran_data:
        if tran_data[tran_type]['action'] == 'plus':
            new_quota = old_quota + amount - interst
            # print(new_quota)
        elif tran_data[tran_type]['action'] == 'minus':
            new_quota = old_quota - amount - interst
            if new_quota < 0:
                print("""\033[36;1m
                您的信用额度不足...
                Credit : %s
                Quota  : %s
                可操作金额：%s\033[0m"""
                %(account_data['credit'],
                  account_data['quota'],
                  account_data['quota']-interst))
                return account_data
        account_data['quota'] = new_quota
        accounts.dump_update(account_data)
        # print(account_data)
        return account_data
    else:
        print("Invalid tran_type...")