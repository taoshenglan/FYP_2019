import os
import codecs
import csv

def load_data(fin, fout):
    fin = codecs.open(fin,'r',encoding=u'utf-8',errors='ignore')
    csv_fout = codecs.open(fout,'w',encoding=u'utf-8',errors='ignore')

    fileHeader = ["parent", "child"]
    writer = csv.writer(csv_fout)
    writer.writerow(fileHeader)

    # d1 = ["Wang", "100"]
    lines = fin.readlines()
    for line in lines:
        ignore_cate = line.strip('Category:')
        # print(ignore_cate)
        # ignore_cate_value=""
        sub = ignore_cate.split("\t")
        if sub[1].find("learn more")==-1:
            if sub[1].find("next page")==-1:
                if sub[1].find(".hack")<0:
                    print(sub)
                    data = [sub[0],sub[1]]
                    writer.writerow(data)


    csv_fout.flush()
    csv_fout.close()
    fin.close()

if __name__=='__main__':
    path_raw_data = "data3.txt"
    path_table_for_relation="table_relation.csv"

    load_data(path_raw_data,path_table_for_relation)

