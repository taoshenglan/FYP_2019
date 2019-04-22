# -*- coding: utf-8 -*-

import numpy as np
import networkx as nx
# import matplotlib.pyplot as plt
# import os
import codecs
# import ast
import csv

def show_net(pathin,out1,out2):
    csvFile = codecs.open(pathin, 'r', encoding=u'utf-8', errors='ignore')
    csv_reader = csv.reader(csvFile)
    csv_fout = codecs.open(out1, 'w', encoding=u'utf-8', errors='ignore')
    writer = csv.writer(csv_fout)
    writer.writerow(['Item','Value'])
    # writer.writerow(['id','in-degree'])
    csv_fout1 = codecs.open(out2, 'w', encoding=u'utf-8', errors='ignore')
    writer2 = csv.writer(csv_fout1)
    writer2.writerow(['id', 'out-degree'])

    G = nx.DiGraph()
    for item in csv_reader:
        #item[0]-->parent, item[1]--> child, item[2]--> freq of child

        G.add_edges_from([(item[0],item[1])])
    indegrees=G.in_degree()
    outdegrees = G.out_degree()
    in_number = []
    in_id = []
    out_num = []
    out_id=[]
    for items in indegrees:
        in_number.append(items[1])
        in_id.append(items[0])
        # writer.writerow([items[0],items[1]])

    for items_o in outdegrees:
        out_num.append(items_o[1])
        out_id.append(items_o[0])
        # writer2.writerow([items_o[0], items_o[1]])

    max_in = max(in_number)
    max_out = max(out_num)

    avg_in = np.average(in_number)
    avg_out=np.average(out_num)
    writer.writerow(['Max_indegree',str(max_in)])
    writer.writerow(['Max_outdegree', str(max_out)])
    writer.writerow(['Avg_indegree', str(avg_in)])
    writer.writerow(['Avg_outdegree', str(avg_out)])
    # writer.writerow("Max_indegree\t"+str(max_in)+"\nMax_outdegree\t"+str(max_out)+"\nAvg_indegree\t "+str(avg_in)+"\nAvg_outdegree\t "+str(avg_out))
    # nx.draw(G, pos=nx.spring_layout(G),node_color = 'b', edge_color = 'r',alpha = 0.3, with_labels = False,
    #         node_size = 5,width = 0.5)

    # figname = "D:/For-F-drive/school/comp/FYP/TSL/diagram_python.png"
    # plt.savefig(figname, dpi=100, bbox_inches='tight')
    # plt.show()

if __name__=='__main__':
    pathin = "D:/For-F-drive/school/comp/eclipse-workspace/test/WebContent/rela_without_multi_Japan.csv"
    pathout1="D:/For-F-drive/school/comp/eclipse-workspace/test/WebContent/indegree_Japan.csv"
    pathout2="D:/For-F-drive/school/comp/eclipse-workspace/test/WebContent/outdegree_Japan.csv"
    pathout_table="D:/For-F-drive/school/comp/eclipse-workspace/test/WebContent/anal_table_Japan.csv"
    show_net(pathin,pathout_table,pathout2)