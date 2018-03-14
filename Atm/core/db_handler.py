# -*- coding:utf-8 -*-
# Author:Wong Du

import os,json
from conf import settings

def file_db_han(acc_prams):
    '''
    pass
    :param acc_prams:
    :return:
    '''
    # print("file db: ",acc_prams)
    return db_exec
def db_han():
    '''
    判断用户数据类型时调用此函数，根据数据类型返回相应的函数方法
    :return:
    '''
    acc_prams = settings.DATABASE
    if acc_prams['engine'] == 'file_storage':
        return file_db_han(acc_prams)
    elif acc_prams['engine'] == 'mysql':
        pass    #to go

def db_exec(sql,**kwargs):
    '''
    操作用户数据文件时调用此函数，
    统一管理数据接口，使其自适应于storage、mysql等多种数据，
    :param sql: 操作文件语句
    :param kwargs: 不确定参数
    :return:
    '''
    acc_prams = settings.DATABASE
    db_path = '%s/%s' %(acc_prams['path'],acc_prams['account_name'])

    sql_list = sql.split("where")
    if sql_list[0].startswith("select") and len(sql_list) > 1:
        column, val = sql_list[1].strip().split("=")
        if column == 'account':
            return db_sel(val,db_path)
    elif sql_list[0].startswith("update") and len(sql_list) > 1:
        key, val = sql_list[1].strip().split("=")
        if key == 'account':
            return db_upd(val,db_path,**kwargs)
def db_sel(acc_id,db_path):
    '''
    获取用户账户信息时调用此函数，
    通过账户id和文件路径操作文件，
    获取账户信息成功返回账户数据
    :param acc_id:
    :param db_path:
    :return:
    '''
    db_file = '%s/%s.json' % (db_path, acc_id)
    if os.path.isfile(db_file):
        with open(db_file, 'r') as f:
            account_data = json.load(f)
            return id_flag(account_data)
    else:
        exit("The db_file does not exist! ")
def db_upd(acc_id,db_path,**kwargs):
    '''
    更新用户账户信息时调用此函数，
    通过账户id和文件路径操作文件，
    更新账户信息成功返回True
    :param acc_id:
    :param db_path:
    :param kwargs:
    :return:
    '''
    db_file = '%s/%s.json' % (db_path, acc_id)
    if os.path.isfile(db_file):
        account_data = kwargs.get('update_data')
        with open(db_file, 'w') as f:
            json.dump(account_data,f)
            return True
    else:
        exit("The db_file does not exist! ")

def id_flag(account_data):
    '''
    判断账户状态，0为正常，1为锁定，2为不可用
    :param account_data:
    :return:
    '''
    if account_data['status'] == 0:
        return account_data
    elif account_data['status'] == 1:
        exit("The card is locked...")
    elif account_data['status'] == 2:
        exit("The card is disabled...")
    else:
        pass