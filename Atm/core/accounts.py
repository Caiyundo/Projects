# -*- coding:utf-8 -*-
# Author:Wong Du

from core import db_handler

def load_current_account(account_id):
    '''
    加载账户数据信息时调用此函数，根据账户id加载信息成功后返回账户数据
    :param account_id:
    :return:
    '''
    db_api = db_handler.db_han()
    data = db_api("select * from accounts where account=%s" %account_id)

    return data

def dump_update(update_data):
    '''
    更新账户数据时调用此函数，用以更新账户数据到文件当中
    :param update_data: 修改后的账户数据
    :return:
    '''
    db_api = db_handler.db_han()
    data = db_api("update * from accounts where account=%s" % update_data['id'],update_data=update_data)

    return True