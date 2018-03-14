# -*- coding:utf-8 -*-
# Author:Wong Du


# def man():
#     print("in the man...")
#     return file_execute
# import json,time ,os
#
# print(time.strptime('2018-11-11','%Y-%m-%d'))
# d = "wo do sha where you=2"
# print(d.split("where"))

dict = {1:2,3:4}
def foo(**kwargs):
    print("in the foo...")
    print(kwargs)
    return dict

# foo2 = foo()
# print(foo2[1])
foo(kwargs = dict)


