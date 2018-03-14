# -*- coding:utf-8 -*-
# Author:Wong Du

from core import auth
from core import accounts
from core import translation

# 用户标志信息
user_data = {
    'account_id':None,
    'is_authorized':False,
    'account_data':None
}

def interactive(_user_data):
    '''
    用户账户密码验证登录成功时调用此函数，是atm交互界面
    引用用户标志位信息进行数据传参以供后续使用
    :param _user_data:
    :return:
    '''
    Menu_list = """\033[33;1m
    1.账户信息
    2.还款
    3.提现
    4.转账
    5.账单
    6.退出
    \033[0m"""
    Menu = {
        '1':account_info,
        '2':repay,
        '3':withdraw,
        '4':transfer,
        '5':record,
        '6':logout
    }
    exit_flag = False
    while not exit_flag:
        print(Menu_list)
        user_option = input("\033[34;1mInput your option: \033[0m")
        if user_option in Menu:
            # print(_user_data)
            Menu[user_option](_user_data)
        else:
            print("Invalid option...")

def account_info(acc_data):
    '''
    查看当前账户信息
    :param acc_data:
    :return:
    '''
    current_data = accounts.load_current_account(acc_data['account_id'])
    print(current_data)
def repay(acc_data):
    '''
    当用户需要进行信用卡还款时调用此函数，用以处理还款操作
    :param acc_data:
    :return:
    '''
    account_data = accounts.load_current_account(acc_data['account_id'])
    acc_quota = """\033[35;1m
    -------------quota info-------------
    Credit : %s
    Quota  : %s
    \033[0m
    """ %(account_data['credit'],account_data['quota'])
    print(acc_quota)
    back_flag = False
    while not back_flag:
        # print(acc_data)
        _repay = input("\033[36;1mRepay Amount: \033[0m")
        if len(_repay) > 0 and _repay.isdigit():
            current_data = translation.make_translation('repay',_repay,account_data)
            print("""\033[31;1m
----------Account Info----------
%s
----------当前信用额度----------
Current_quota : %s\033[0m"""
% (current_data, current_data['quota'])
                  )
        elif _repay == 'b':
            back_flag = True
        else:
            print("Invalid repay...")
def withdraw(acc_data):
    '''
        当用户需要进行提现时调用此函数，用以处理提现操作
        :param acc_data:
        :return:
    '''
    account_data = accounts.load_current_account(acc_data['account_id'])
    acc_quota = """\033[35;1m
        -------------quota info-------------
        Credit : %s
        Quota  : %s
        \033[0m
        """ % (account_data['credit'], account_data['quota'])
    print(acc_quota)
    back_flag = False
    while not back_flag:
        _withdraw = input("\033[36;1mInput your withdrw: \033[0m")
        if len(_withdraw)>0 and _withdraw.isdigit():
            current_data = translation.make_translation('withdraw',_withdraw,account_data)
            print("""\033[31;1m
----------Account Info----------
%s
----------当前信用额度----------
Current_quota : %s\033[0m"""
% (current_data, current_data['quota'])
                  )
        elif _withdraw == 'b':
            back_flag = True
        else:
            print("Invalid withdraw...")
def transfer(acc_data):
    '''
        当用户需要进行转账时调用此函数，用以处理转账操作
        :param acc_data:
        :return:
    '''
    account_data = accounts.load_current_account(acc_data['account_id'])
    acc_quota = """\033[35;1m
        -------------quota info-------------
        Credit : %s
        Quota  : %s
        \033[0m
        """ % (account_data['credit'], account_data['quota'])
    print(acc_quota)
    back_flag = False
    while not back_flag:
        tran_id = input("\033[36;1mInput you want to transfer id: \033[0m")
        if tran_id == 'b':
            back_flag = True
            continue
        else:
            tran_data = accounts.load_current_account(tran_id)
        _transfer = input("\033[36;1mInput your transfer: \033[0m")
        if len(_transfer) > 0 and _transfer.isdigit():
            current_data = translation.make_translation('transfer',_transfer,account_data)
            tran_data = translation.make_translation('repay',_transfer,tran_data)
            print("""\033[31;1m
----------Account Info----------
%s
----------当前信用额度----------
Current_quota : %s\033[0m"""
% (current_data, current_data['quota'])
                )
        elif _transfer == 'b':
            back_flag = True
        else:
            print("Invalid transfer...")
def record(acc_data):
    pass
def logout(acc_data):
    '''
    退出登录
    :param acc_data:
    :return:
    '''
    exit("感谢您的使用！！！")

def run():
    '''
    当程序启动的时候调用该函数，管理用户认证，处理用户交互信息
    :return:
    '''
    acc_data = auth.acc_login(user_data)
    if user_data['is_authorized']:
        user_data['account_data'] = acc_data
        interactive(user_data)