# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp


def func(x):
    return '\\' + x

test_item1 = [1, 2]
bool_item2 = True
str_item3 = 'test'
dict_item4 = dict(
    a={
        'c/d': 'path/d',
        'f': 's3//f',
        6: '2333',
        '2333': 'number'
    },
    b={'8': 543},
    c={9: 678},
    d={'a': 0},
    f=dict(a='69'))
dict_item5 = {'x/x': {'a.0': 233}}
dict_list_item6 = {'x/x': [{'a.0': 1., 'b.0': 2.}, {'c/3': 3.}]}
dict_item7 = osp.expanduser('~')
dict_item8 = func('a')
