# -*- coding: utf-8 -*-
import codecs
import csv
from operator import attrgetter

from collections import namedtuple

def FindParent(pathin1, pathin2,pathin3,pathout):
    dict_data={ }
    file_tree = open(pathin1,'r')
    lines = file_tree.readlines()

    rela_list=[]

    rela_list.append(['1','0'])
    for line in lines:
        if line.count('\n')==len(line):
            continue
        line = line.strip("\r\n").strip("\n")
        line = line.strip()
        rela = line.split(" ")
        rela_list.append([rela[1],rela[0]])
        # print("rela:"+rela[0]+"+"+rela[1])



    print("loaded data...")
    print(rela_list)
    node_dict = {}
    node = namedtuple('node', 'id, p_id')
    for a in rela_list:
        node_dict[a[0]] = node(*a)

    file_tree.close()
    file_testresult=codecs.open(pathin2,'r',encoding=u'utf-8',errors='ignore')
    reader = csv.reader(file_testresult)
    c_list=[]
    for item in reader:
        c_list.append(item[0])
    file_testresult.close()
    print(c_list)

    relationships=[]
    for i in c_list:
        res = traversal(node_dict,i)
        path = ','.join(map(attrgetter('id'), res))
        print(path)
        elements=path.split(",")
        tmp_rela=[]
        for k in c_list:

            if elements.count(k)!=0 and k!=i:
                tmp_rela=[k,i]
                break
            else:
                tmp_rela=['1',i]
        relationships.append(tmp_rela)


    print(relationships)
    print(relationships.__len__())
    file_testresult.close()
    file_tree.close()

    file_freq=open(pathin3,'r',encoding='utf-8',errors='ignore')
    freqlist=[]
    freqs = file_freq.readlines()
    for line in freqs:
        if line.count('\n')==len(line):
            continue
        item = line.strip("\r\n").split(" ")
        frq='-1'
        for i in c_list:
            if item[0]==i:
                frq=item[1]
        if frq!='-1':
            freqlist.append([item[0],frq])
    file_freq.close()

    fout = open(pathout,'w',encoding='utf-8',newline='')
    writer=csv.writer(fout)
    writer.writerow(['parent','name','value'])
    writer.writerow(['null','1','30'])
    for i in relationships:
        for k in freqlist:
            if i[1]==k[0]:
                # print(i[0],i[1],k[1])
               writer.writerow([i[0],i[1],k[1]])


    fout.flush()
    fout.close()






def traversal(node_dict, id):
    if node_dict[id].p_id == '0':
        return [node_dict[id]]
    else:
        return traversal(node_dict, node_dict[id].p_id) + [node_dict[id]]


if __name__=='__main__':
    path_treedata="D:\\For-F-drive\\school\\comp\\FYP\\TSL\\code\\DAG_LATT20.txt"
    path_treeResult="test_out.csv"
    path_freq = "C:\\Users\\lenovo\\Desktop\\Web_DAG_KvDO\\WebContent\\Call_KvDO\\feq-patient.txt"
    path_out = "tree-result.csv"
    FindParent(path_treedata,path_treeResult,path_freq,path_out)