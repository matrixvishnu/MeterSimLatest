#!/usr/bin/python
import traceback
import time
import datetime
import csv
from random import *
import math
from csv import DictReader
import pandas as pd
import numpy as np
import threading
import uuid
import cx_Oracle
import random
import json 
import pandas as pd
import bil_metesim as bm
import sys

import os
cwd = os.getcwd()

time_period = input("Enter the time Period:")
file_name = raw_input("""Enter the csv file name
:""")
ip_file = cwd + '/'+file_name
data = pd.read_csv(ip_file)
list = data["METER_NO"].tolist()
dic = dict(zip(data.METER_NO, data.CUM_ENG_KWH))
x= bm.billing()
con = cx_Oracle.connect('ORACLE','oracle123',cx_Oracle.makedsn('orcl.cociefkf8fny.ap-southeast-1.rds.amazonaws.com',1521,'ORACLE'))
cur = con.cursor()

while True:
    for i in dic:
        x.mtr_no = i
        x.cum_kwh = dic[i]
        result = x.bill()
        fields = result.keys()
        values  = result.values()
        bindvars = ":" + ",:".join(fields)
        sql = "insert into MPM.MPM_BILLING_PARAMETERS (BILLING_PARA_ID,REAL_TIME_CLOCK_DATE_TIME,BILLING_DATE,%s) values (MPM.MPM_BILLING_PARAMETERS_S.NEXTVAL,current_timestamp,current_timestamp,%s)" % (",".join(fields), bindvars)
        print sql
        cur.execute(sql, values)
        con.commit()
        dic[i] = result["CUM_ENG_KWH"] 
    print dic
    list = dic.items()
    print list
    index = range(len(list))
    print index
    cols = ['METER_NO', 'CUM_ENG_KWH']
    df_r = pd.DataFrame(list, columns = cols)
    df_r.to_csv(ip_file, index = False)
    print df_r
    time.sleep(time_period)
