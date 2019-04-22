# -*- coding: utf-8 -*-
from operator import attrgetter
from collections import namedtuple

d_list = [['1','0'],['2','1'],['3','1'],['4','1'],['5','1'],['6','2'],['7','2'],['8','3']]

node_dict = {}
node = namedtuple('node', 'id, p_id')

for i in d_list:

    node_dict[i[0]] = node(*i)


def traversal(node_dict, id):
    if node_dict[id].p_id == '0':
        return [node_dict[id]]
    else:
        return traversal(node_dict, node_dict[id].p_id) + [node_dict[id]]


c_list = ['1','2','3','4','5','6','7','8']
for i in c_list:
    res = traversal(node_dict, i)
    path = ','.join(map(attrgetter('id'), res))
    level = path.count(',')
    print(i, path)