# -*- coding: utf-8 -*-
import numpy as np
import os
import pandas as pd
import networkx as nx
import codecs
import ast
import csv
from collections import defaultdict
from operator import attrgetter
from collections import namedtuple

def Change_into_IDANDFreq(pathin_rela,path_freq,path_name,pathout):
    csv_fout = codecs.open(pathout, 'w', encoding=u'utf-8', errors='ignore')
    #relation with ID
    file_rela=open(pathin_rela,'r',encoding=u'utf-8',errors='ignore')
    # #id and freq (node & freq)
    df_freq= pd.read_csv(path_freq)
    df_name_and_id = pd.read_csv(path_name)

    parent=defaultdict(list)
    rela = defaultdict(list)
    fieldnames = ['parent', 'name','value']
    writer = csv.writer(csv_fout)
    writer.writerow(fieldnames)

    root_freq = df_freq.query("node=='1'").get("freq").values
    root_freq = root_freq[0]
    root_name = df_name_and_id.query("ID=='1'").get("Name").values
    root_name = root_name[0]
    writer.writerow(['null',root_name,root_freq])
    remap = {
            ord("'"): '',
            ord("\""):'',
            ord("’"):'',
            ord('"'):'',
            ord('\''):''

        }
    lines = file_rela.readlines()
    rela_list=[]
    rela_list.append(['1', '0'])
    c_list=[]
    nodelist=[]
    for line in lines:
        if line.count("36525 15134"):
            continue;
        sub=line.split(" ")
    #     sub[0]-->pid, sub[1]-->cid
        pid = sub[0].translate(remap)
        cid = sub[1].translate(remap)
        pid=pid.strip("\r\n")
        cid=cid.strip("\r\n")
        rela_list.append([cid,pid])
        rela[int(pid)].append(cid)
        if c_list.count(cid)==0:
            c_list.append(cid)
        if nodelist.count(pid)==0:
            nodelist.append(pid)
        if nodelist.count(cid)==0:
            nodelist.append(cid)
    print("loaded rela_list")
    # print(rela)

    child_of_one=rela.get(1)
    # print(child_of_one)
    for i in c_list:
       plist = traversal(nodelist,rela,int(i))
       # print(plist)
       for k in plist:
           freq=df_freq.query("node=='"+str(k)+"'").get("freq").values
           freq=freq[0]
           if child_of_one.count(k)==0 and freq>20:
               rela[1].append(k)
    # print(rela.get(1))
    keys =sorted( rela.keys())
    for key in keys:
        values=rela.get(key)
        pname = df_name_and_id.query("ID=='"+str(key)+"'").get("Name").values
        pname = pname[0]
        for k in values:
            feq = df_freq.query("node=='"+str(k)+"'").get("freq").values
            feq=feq[0]
            cname = df_name_and_id.query("ID=='" + str(k) + "'").get("Name").values
            cname = cname[0]
            tmp = rela.get(int(k))
            length=0
            if tmp!=None:
                length=len(tmp)
            if pname != cname and cname != "Anime":
                writer.writerow([pname, cname, feq])
                print(pname, cname, str(feq))



    #
    #     # print(pid+" "+cid)
    #     # pname = df_name_and_id.query("ID=='"+pid+"'").get("Name").values
    #     # pname = pname[0]


        # print(pname+" --> "+cname);
        # freq = df_freq.query("node=='"+cid+"'").get("freq").values
        # freq=freq[0]
        # print(pname+" "+cname+" "+str(freq))
        # writer.writerow([pname,cname,freq])
    csv_fout.flush()
    csv_fout.close()
    file_rela.close()

def traversal(nodelist, rela, id):
    plist=[]
    # print(id)
    for i in nodelist:
        tmp = rela.get(int(i))
        if tmp==None:
            continue
        if str(id) in tmp:
            plist.append(id)
    # print("plist:")
    # print(plist)
    return plist

if __name__=='__main__':
    path_name="name_and_ID_Japan.csv"
    # path_relationship_outWithID="D:/For-F-drive/school/comp/Eclipse-workspace/Web_DAG_KvDO/WebContent/rela_with_ID.csv"
    path_node_withFreq = "files/freq_Japan.csv"
    path_relation_txt="files/rela_for_Kvdo_Japan.txt"
    path_relationship_without_multi = "files/rela_without_multi_Japan.csv"
    path_combined_relaANDfreq="rela_with_freq_Japan_allnodes-v2.csv"
    path_relationship_without_multi_name = "files/rela_without_multi_name_Japan.csv"
    Change_into_IDANDFreq(path_relation_txt,path_node_withFreq,path_name,path_combined_relaANDfreq)