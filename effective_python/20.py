# -*- coding: utf-8 -*-

'''
20:用None和文档字符串来描述具有动态默认值的参数
'''
import json


def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


def decode_debug(data, default=None):
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default


if __name__ == '__main__':
    foo = decode('bad data')
    foo['s'] = 5
    bar = decode('bad data')
    bar['x'] = 1
    print(foo, bar)

    foo_debug = decode_debug('bad data')
    foo_debug['s'] = 5
    bar_debug = decode_debug('bad data')
    bar_debug['x'] = 1
    print(foo_debug, bar_debug)
