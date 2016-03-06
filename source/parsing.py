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

db = [["clinicRef", "clinicName", "clinicAddr", "clinicTel", "city", "groupRef", "groupName", "groupTel", "hos1Ref", "hos1Name", "hos2Ref", "hos2Name", "hos3Ref", "hos3Name", "hos4Ref", "hos4Name"]]

url_primer = 'http://www.nhi.gov.tw/OnlineQuery/FamilyDrSearch.aspx?menu=20&menu_id=926&webdata_id=3661&WD_ID=929&QueryType=2&City=&Area=&HName=&HID=&CName=&CID=&H1Name=&H1ID=&page='
for t in range(0, 302):
    url = url_primer +`t`
    html = urllib2.urlopen(url).read()
    tree = etree.HTML(html)
    #clin_list = tree[1][0][2][1][3][5][0][0][1][1][0][0][0]
    clin_list = tree[1][0][1][0][4][1][6][0][1][1][0][0][0]
    for i in range(1,len(clin_list)):
        clinic_ref = rm_blank(clin_list[i][3].text)
        clinic_name = rm_blank(clin_list[i][3][1].text)
        clinic_addr = rm_blank(unicodedata.normalize('NFKC', clin_list[i][3][3].tail))
        clinic_tel = rm_blank(clin_list[i][3][2].tail)
        group_tel = rm_blank(clin_list[i][4].text)
        city = rm_blank(clin_list[i][0].text)
        group_ref = rm_blank(clin_list[i][1][0].text)
        group_name = rm_blank(clin_list[i][1][0][0].tail)
        hos_1_ref = rm_blank(clin_list[i][2][0].text).replace("(第一)", "")
        hos_1_name = rm_blank(clin_list[i][2][0][0].tail)
        if len(clin_list[i][2][1]) > 0:
            hos_2_ref = rm_blank(clin_list[i][2][1].text).replace("(第二)", "")
            hos_2_name = rm_blank(clin_list[i][2][1][0].tail)
        else:
            hos_2_ref = ''
            hos_2_name = ''
        if len(clin_list[i][2][2]) > 0:
            hos_3_ref = rm_blank(clin_list[i][2][2].text).replace("(第三)", "")
            hos_3_name = rm_blank(clin_list[i][2][2][0].tail)
        else:
            hos_3_ref = ''
            hos_3_name = ''
        if len(clin_list[i][2][3]) > 0:
            hos_4_ref = rm_blank(clin_list[i][2][3].text).replace("(第四)", "")
            hos_4_name = rm_blank(clin_list[i][2][3][0].tail)
        else:
            hos_4_ref = ''
            hos_4_name = ''
        db.append([clinic_ref, clinic_name, clinic_addr, clinic_tel, city, group_ref, group_name, group_tel, hos_1_ref, hos_1_name, hos_2_ref, hos_2_name, hos_3_ref, hos_3_name, hos_4_ref, hos_4_name])
        print("add 1 data")

import csv

with open("../content/tmp.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(db)
