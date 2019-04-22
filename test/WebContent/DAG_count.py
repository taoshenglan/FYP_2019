# -*- coding: utf-8 -*-

import os
import pandas as pd
import networkx as nx
import codecs
import ast
import csv
from collections import defaultdict

def load_data(path,path_ID,path_out):
    # load the relationship-table and ID information

    df_id = pd.read_csv(path_ID)
    csv_fout = codecs.open(path_out, 'w', encoding=u'utf-8', errors='ignore')
    csvFile = codecs.open(path, 'r', encoding=u'utf-8', errors='ignore')
    csv_reader = csv.reader(csvFile)
    fieldnames = ['pid', 'cid']
    writer = csv.writer(csv_fout)

    row_count = 1
    for item in csv_reader:
        # item[0]-->parent item[1]-->child

        if csv_reader.line_num == 1:
            continue
        parent_id = df_id.query("Name=='"+item[0]+"'").get("ID").values
        child_id = df_id.query("Name=='" + item[1] + "'").get("ID").values
        if len(parent_id)>0 and len(child_id)>0:
            parent_id = parent_id[0]
            child_id = child_id[0]
            print("parent id:" + str(parent_id))
            print("child id:" + str(child_id))
            print("===================")
            row_count = row_count + 1
            writer.writerow([parent_id, child_id])
        else:
            continue


    node_count = df_id.__len__()


    csv_fout.flush()
    csv_fout.close()
    csvFile.close()

def get_ID(path,fout):
    csv_fout = codecs.open(fout, 'w', encoding=u'utf-8', errors='ignore')
    csvFile = codecs.open(path, 'r', encoding=u'utf-8', errors='ignore')
    csv_reader = csv.reader(csvFile)
    ID_list = []
    name_set = []
    if os._exists(csv_fout):
        csv_dict= csv.DictReader(csv_fout)
        for item in csv_dict:
            print("======in f_out===========")
            print(item)
    else:

        fileHeader = ["ID", "Name"]
        writer = csv.writer(csv_fout)
        writer.writerow(fileHeader)
        remap = {
            ord("'"): '',
            ord("\""): '',
            ord("’"): '',
            ord('"'): '',
            ord('\''): ''

        }

        for item in csv_reader:
            # item[0]-->parent item[1]-->child
            if csv_reader.line_num == 1:
                continue
            pname = item[0].translate(remap)
            cname = item[1].translate(remap)
            pname = pname.strip("\r\n")
            cname = cname.strip("\r\n")
            if pname not in name_set:
               name_set.append(pname)
            if cname not in name_set:
                name_set.append(cname)

        # name_set.sort()
        print(len(name_set))
        id = 1
        for name in name_set:
            tmp = []
            # name = name.strip("\r\n")
            # name = name.translate(remap)
            tmp.append(str(id))
            tmp.append(name)
            ID_list.append(tmp)
            writer.writerow(tmp)
            id += 1

    csv_fout.flush()
    csv_fout.close()
    csvFile.close()
    return ID_list

def tranlateTableRelation(pathin,pathout):
    csv_fout = codecs.open(pathout, 'w', encoding=u'utf-8', errors='ignore')
    csvFile = codecs.open(pathin, 'r', encoding=u'utf-8', errors='ignore')
    csv_reader = csv.reader(csvFile)
    fileHeader = ["parent", "child"]
    writer = csv.writer(csv_fout)
    writer.writerow(fileHeader)
    for item in csv_reader:
        # item[0]-->parent item[1]-->child
        if csv_reader.line_num == 1:
            continue
        p_name=item[0]
        c_name=item[1]
        remap = {
            ord("'"): '',
            ord("\""):'',
            ord("’"):'',
            ord('"'):'',
            ord('\''):''

        }
        p_name = p_name.translate(remap)
        c_name = c_name.translate(remap)
        p_name = p_name.strip("\r\n")
        c_name=c_name.strip("\r\n")


        data = [p_name,c_name]
        writer.writerow(data)
    csv_fout.flush()
    csv_fout.close()
    csvFile.close()


def count_freq(path_in, path_out):
    csv_fout = codecs.open(path_out, 'w', encoding=u'utf-8', errors='ignore')
    csvFile = codecs.open(path_in, 'r', encoding=u'utf-8', errors='ignore')
    csv_reader = csv.reader(csvFile)
    link_set = {}
    for item in csv_reader:
        # item[0]-->parent item[1]-->child
        if csv_reader.line_num == 1:
            continue
        if link_set.__contains__(item[0]):
            count = link_set.get(item[0])
            count = count+1
            link_set[item[0]]=count
            # print(link_set)
        else:
            link_set[item[0]]=1

        if link_set.__contains__(item[1]):
            count_c = link_set.get(item[1])
            count_c = count_c+1
            link_set[item[1]]=count_c
            # print(link_set)
        else:
            link_set[item[1]]=1

    print(link_set)
    writer = csv.writer(csv_fout)
    fileheader=['node','freq']
    writer.writerow(fileheader)
    for key,value in link_set.items():
        writer.writerow([key,value])
    csv_fout.flush()
    csv_fout.close()
    csvFile.close()

def clean_multi(pathin,pathout):
    csv_fout = codecs.open(pathout, 'w', encoding=u'utf-8', errors='ignore')
    csvFile = codecs.open(pathin, 'r', encoding=u'utf-8', errors='ignore')
    csv_reader = csv.reader(csvFile)
    link_set = {}
    for item in csv_reader:
        # item[0]-->parent item[1]-->child
        if csv_reader.line_num == 1:
            continue
        string = item[0]+","+item[1]
        if link_set.__contains__(string):
            count = link_set.get(string)
            count = count + 1
            link_set[string] = count
            # print(link_set)
        else:
            link_set[string] = 1
    writer = csv.writer(csv_fout)
    fileheader = ['parent', 'child']
    writer.writerow(fileheader)
    for key, value in link_set.items():
        nodes = key.split(",")
        writer.writerow([nodes[0],nodes[1]])
    csv_fout.flush()
    csv_fout.close()
    csvFile.close()

def transfore_to_kVDO(pathin,pathout,pathin_freq, pathout_freq):
    csvFile = codecs.open(pathin, 'r', encoding=u'utf-8', errors='ignore')
    csv_reader = csv.reader(csvFile)
    csvFile2 = codecs.open(pathin_freq, 'r', encoding=u'utf-8', errors='ignore')
    csv_reader2 = csv.reader(csvFile2)
    fout = open(pathout, "w", encoding='UTF-8',errors='ignore',newline='')
    fout.write("null null\n")
    fout_freq = open(pathout_freq, "w", encoding='UTF-8',errors='ignore',newline='')
    row_count=0
    relation=defaultdict(list)
    for item in csv_reader:
        # item[0]-->parent item[1]-->child
        if csv_reader.line_num == 1:
            continue
        if item[0]==item[1]:
            continue
        # str1 = item[0] + " " + item[1]
        relation[int(item[0])].append(item[1])
        row_count = row_count + 1
        # fout.write(str1)
    tmp = sorted(relation.keys())
    for pid in tmp:
        print(pid)
        childlist = relation.get(pid)
        for cid in childlist:
            str1 = str(pid)+" "+cid+"\n"

            fout.write(str1)
    row2=0
    freqlist=defaultdict(list)
    for item2 in csv_reader2:
    #     item[0]-->parent item[1]-->child
        if csv_reader2.line_num == 1:
            continue
        freqlist[int(item2[0])].append(item2[1])
    tmp_feq=sorted(freqlist.keys())
    for id in tmp_feq:
        feq = freqlist.get(id)
        print("feq = "+feq[0])
        str2 = str(id)+" "+feq[0]+"\n"
        row2 =row2+1
        fout_freq.write(str2)
    print("row_count:"+str(row_count))
    print("row_count_feq:" + str(row2))


if __name__=='__main__':
    path_table="table_relation.csv"
    path_table2 = "table_relation_Japan.csv"
    path_name="name_and_ID_Japan.csv"
    path_relationship_outWithID="rela_with_ID_Japan.csv"
    path_node_withFreq = "freq_Japan.csv"
    path_relationship_without_multi = "rela_without_multi_Japan.csv"
    path_relationship_without_multi_name="rela_without_multi_name_Japan.csv"
    path_use_for_KvDO = "rela_for_Kvdo_Japan.txt"
    path_use_for_KvDO_freq = "freq_for_Kvdo_Japan.txt"

    # tranlateTableRelation(path_table,path_table2)
    # ID_list = get_ID(path_table2,path_name)
    # load_data(path_relationship_without_multi_name,path_name,path_relationship_without_multi)
    # count_freq(path_relationship_without_multi,path_node_withFreq)
    # transfore_to_kVDO(path_relationship_without_multi, path_use_for_KvDO, path_node_withFreq, path_use_for_KvDO_freq)
    # count_row(path_use_for_KvDO_freq);
    # clean_multi(path_table2,path_relationship_without_multi_name)
    # clean_file(path_use_for_KvDO,path_name,path_node_withFreq,)