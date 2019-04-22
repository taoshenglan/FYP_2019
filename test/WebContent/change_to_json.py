import csv;
import json;
import codecs

# csvfile = open('anal_table.csv','r')
# jsonfile = open('anal_table.json','w')
# reader = csv.reader(csvfile)
# for row in reader:
#     json.dump(row, jsonfile)
#     jsonfile.write("\n")

txtfile = open('tree-MED.txt','r')
csvfile_result = open("tree_MED.csv",'w',encoding='utf8',newline='')
lines = txtfile.readlines()
writer = csv.writer(csvfile_result)
writer.writerow(['parent','name'])
for row in lines:
    if row == "\n":
        continue
    temp = row.split(" ")
    print(temp[0]+"+"+temp[1].strip('\r\n').strip(" "))
    # temp[0] item, temp[1] value
    writer.writerow([temp[0],temp[1].strip('\r\n').strip(" ")])
csvfile_result.flush()
csvfile_result.close()
txtfile.close()