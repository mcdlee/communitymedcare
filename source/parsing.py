# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 15:46:19 2014

@author: mcdlee
"""

from lxml import etree
import urllib2
import unicodedata

def rm_blank(s):
    u = s.replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", "")
    return u

db = [["clinicRef", "clinicName", "clinicAddr", "city", "groupRef", "groupName", "hos1Ref", "hos1Name", "hos2Ref", "hos2Name", "hos3Ref", "hos3Name", "hos4Ref", "hos4Name"]]

url_primer = 'http://www.nhi.gov.tw/OnlineQuery/FamilyDrSearch.aspx?menu=20&menu_id=926&webdata_id=3661&WD_ID=929&QueryType=2&City=&Area=&HName=&HID=&CName=&CID=&H1Name=&H1ID=&page='
for t in range(1,305):
    url = url_primer +`t`
    html = urllib2.urlopen(url).read()
    tree = etree.HTML(html)
    clin_list = tree[1][0][2][1][3][6][0][0][1][1][0][0][0]
    for i in range(1,len(clin_list)):
        clinic_ref = rm_blank(clin_list[i][3].text.encode('utf-8'))
        clinic_name = rm_blank(clin_list[i][3][1].text.encode('utf-8'))
        clinic_addr = rm_blank(unicodedata.normalize('NFKC', clin_list[i][3][3].tail).encode('utf-8'))
        city = rm_blank(clin_list[i][0].text.encode('utf-8'))
        group_ref = rm_blank(clin_list[i][1][0].text.encode('utf-8'))
        group_name = rm_blank(clin_list[i][1][0][0].tail.encode('utf-8'))
        hos_1_ref = rm_blank(clin_list[i][2][0].text.encode('utf-8')).replace("(第一)", "")
        hos_1_name = rm_blank(clin_list[i][2][0][0].tail.encode('utf-8'))
        if len(clin_list[i][2][1]) > 0:
            hos_2_ref = rm_blank(clin_list[i][2][1].text.encode('utf-8')).replace("(第二)", "")
            hos_2_name = rm_blank(clin_list[i][2][1][0].tail.encode('utf-8'))
        else:
            hos_2_ref = ''
            hos_2_name = ''
        if len(clin_list[i][2][2]) > 0:
            hos_3_ref = rm_blank(clin_list[i][2][2].text.encode('utf-8')).replace("(第三)", "")
            hos_3_name = rm_blank(clin_list[i][2][2][0].tail.encode('utf-8'))
        else:
            hos_3_ref = ''
            hos_3_name = ''
        if len(clin_list[i][2][3]) > 0:
            hos_4_ref = rm_blank(clin_list[i][2][3].text.encode('utf-8')).replace("(第四)", "")
            hos_4_name = rm_blank(clin_list[i][2][3][0].tail.encode('utf-8'))
        else:
            hos_4_ref = ''
            hos_4_name = ''
        db.append([clinic_ref, clinic_name, clinic_addr, city, group_ref, group_name, hos_1_ref, hos_1_name, hos_2_ref, hos_2_name, hos_3_ref, hos_3_name, hos_4_ref, hos_4_name])
	print("Add a new record")
import csv

with open("../content/clinic_list.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(db)
