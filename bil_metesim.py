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
#import cx_Oracle
import random
import json 
import pandas as pd

class billing():
    mtr_no = "123mtr_no"
    cum_kwh  = 2000
    def bill(self):
        rtc = datetime.datetime.now()
        Block_energy_kWhImport = round(np.random.uniform(0.12,0.22),2)
        max_demand = round(np.random.uniform(0.,0.22),2)

        MTR_NO                      = self.mtr_no
        REAL_TIME_CLOCK_DATE_TIME   = rtc.strftime("%d-%m-%y %I.%M.%S %p")
        BILLING_DATE                = rtc.strftime("%d-%m-%y %I.%M.%S %p")
        SYS_PWR_FACT_BILLING_PERIOD = round(np.random.uniform(0.89,0.99),2)
	Cumulative_energykWhImportInitial             = self.cum_kwh
        CUM_ENG_KWH        =round(Cumulative_energykWhImportInitial +  round(np.random.uniform(0.12,0.22),2),2)
        CUM_ENG_KWH_TZ_1   = round(CUM_ENG_KWH / 16,2)
        CUM_ENG_KWH_TZ_2   = round(CUM_ENG_KWH / 16,2)
        CUM_ENG_KWH_TZ_3   = round(CUM_ENG_KWH / 4,2)
        CUM_ENG_KWH_TZ_4   = round(CUM_ENG_KWH / 8,2)
        CUM_ENG_KWH_TZ_5   = round(CUM_ENG_KWH / 4,2)
        CUM_ENG_KWH_TZ_6   = round(CUM_ENG_KWH / 8,2)
        CUM_ENG_KWH_TZ_7   = round(CUM_ENG_KWH / 16,2)
        CUM_ENG_KWH_TZ_8   = round(CUM_ENG_KWH / 16,2)
        CUM_ENG_KVARH_LAG  = round(np.sqrt(np.power((CUM_ENG_KWH/SYS_PWR_FACT_BILLING_PERIOD),2)-np.power(CUM_ENG_KWH, 2)),2)
        CUM_ENG_KVARH_LEAD = 0
        CUM_ENG_KVAH       = round(CUM_ENG_KWH/SYS_PWR_FACT_BILLING_PERIOD,2)
        CUM_ENG_KVAH_TZ_1  =round( CUM_ENG_KVAH/16,2)
        CUM_ENG_KVAH_TZ_2  =round( CUM_ENG_KVAH/16,2)
        CUM_ENG_KVAH_TZ_3  =round( CUM_ENG_KVAH/4,2)
        CUM_ENG_KVAH_TZ_4  =round( CUM_ENG_KVAH/8,2)
        CUM_ENG_KVAH_TZ_5  =round( CUM_ENG_KVAH/4,2)
        CUM_ENG_KVAH_TZ_6  =round( CUM_ENG_KVAH/8,2)
        CUM_ENG_KVAH_TZ_7  =round( CUM_ENG_KVAH/16,2)
        CUM_ENG_KVAH_TZ_8  =round( CUM_ENG_KVAH/16,2)
        MD_KW              = round(Block_energy_kWhImport+round(np.random.uniform(0.0,2.0),2),2)
        MD_KW_TZ_1         =round( MD_KW/ 16,2)
        MD_KW_TZ_2         =round( MD_KW/ 16,2)
        MD_KW_TZ_3         =round( MD_KW/ 4,2)
        MD_KW_TZ_4         =round( MD_KW/ 8,2)
        MD_KW_TZ_5         =round( MD_KW/ 4,2)
        MD_KW_TZ_6         =round( MD_KW/ 8,2)
        MD_KW_TZ_7         =round( MD_KW/ 16,2)
        MD_KW_TZ_8         =round( MD_KW/ 16,2)
        MD_KVA             = round(MD_KW/SYS_PWR_FACT_BILLING_PERIOD,2)
        MD_KVA_TZ_1        =round( MD_KW / 16,2)
        MD_KVA_TZ_2        =round( MD_KW / 16,2)
        MD_KVA_TZ_3        =round( MD_KW / 4,2)
        MD_KVA_TZ_4        =round( MD_KW / 8,2)
        MD_KVA_TZ_5        =round( MD_KW / 4,2)
        MD_KVA_TZ_6        =round( MD_KW / 8,2)
        MD_KVA_TZ_7        =round( MD_KW / 16,2)
        MD_KVA_TZ_8        =round( MD_KW / 16,2)
        CUM_ENG_KWH_EXP    = 0
        CUM_ENG_KVAH_EXP   = 0
        CUM_ENG_KVARH_Q1   = 0
        CUM_ENG_KVARH_Q2   = CUM_ENG_KVARH_LAG
        CUM_ENG_KVARH_Q3   = 0
        CUM_ENG_KVARH_Q4   = 0
        def prvar(__x):
            print traceback.extract_stack(limit=2)[0][3][6:][:-1],"=",__x
       # prvar()
        l = {"MTR_NO" : self.mtr_no,
        "SYS_PWR_FACT_BILLING_PERIOD"        : SYS_PWR_FACT_BILLING_PERIOD ,
        "CUM_ENG_KWH"                        : round(Cumulative_energykWhImportInitial +  round(np.random.uniform(0.12,0.22),2),2)     ,
        "CUM_ENG_KWH_TZ_1"                   :round(CUM_ENG_KWH / 16,2)  ,
        "CUM_ENG_KWH_TZ_2"                   :round(CUM_ENG_KWH / 16,2)  ,
        "CUM_ENG_KWH_TZ_3"                   :round(CUM_ENG_KWH / 4,2)   ,
        "CUM_ENG_KWH_TZ_4"                   :round(CUM_ENG_KWH / 8,2)   ,
        "CUM_ENG_KWH_TZ_5"                   :round(CUM_ENG_KWH / 4,2)   ,
        "CUM_ENG_KWH_TZ_6"                   :round(CUM_ENG_KWH / 8,2)   ,
        "CUM_ENG_KWH_TZ_7"                   :round(CUM_ENG_KWH / 16,2)  ,
        "CUM_ENG_KWH_TZ_8"                   :round(CUM_ENG_KWH / 16,2)  ,
        "CUM_ENG_KVARH_LAG"                  : CUM_ENG_KVARH_LAG ,
        "CUM_ENG_KVARH_LEAD"                 : CUM_ENG_KVARH_LEAD,
        "CUM_ENG_KVAH"                       : CUM_ENG_KVAH      ,
        "CUM_ENG_KVAH_TZ_1"                  : CUM_ENG_KVAH_TZ_1 ,
        "CUM_ENG_KVAH_TZ_2"                  : CUM_ENG_KVAH_TZ_2 ,
        "CUM_ENG_KVAH_TZ_3"                  : CUM_ENG_KVAH_TZ_3 ,
        "CUM_ENG_KVAH_TZ_4"                  : CUM_ENG_KVAH_TZ_4 ,
        "CUM_ENG_KVAH_TZ_5"                  : CUM_ENG_KVAH_TZ_5 ,
        "CUM_ENG_KVAH_TZ_6"                  : CUM_ENG_KVAH_TZ_6 ,
        "CUM_ENG_KVAH_TZ_7"                  : CUM_ENG_KVAH_TZ_7 ,
        "CUM_ENG_KVAH_TZ_8"                  : CUM_ENG_KVAH_TZ_8 ,
        "MD_KW"                              : MD_KW             ,
        "MD_KW_TZ_1"                         : MD_KW_TZ_1        ,
        "MD_KW_TZ_2"                         : MD_KW_TZ_2        ,
        "MD_KW_TZ_3"                         : MD_KW_TZ_3        ,
        "MD_KW_TZ_4"                         : MD_KW_TZ_4        ,
        "MD_KW_TZ_5"                         : MD_KW_TZ_5        ,
        "MD_KW_TZ_6"                         : MD_KW_TZ_6        ,
        "MD_KW_TZ_7"                         : MD_KW_TZ_7        ,
        "MD_KW_TZ_8"                         : MD_KW_TZ_8        ,
        "MD_KVA"                             : MD_KVA            ,
        "MD_KVA_TZ_1"                        : MD_KVA_TZ_1       ,
        "MD_KVA_TZ_2"                        : MD_KVA_TZ_2       ,
        "MD_KVA_TZ_3"                        : MD_KVA_TZ_3       ,
        "MD_KVA_TZ_4"                        : MD_KVA_TZ_4       ,
        "MD_KVA_TZ_5"                        : MD_KVA_TZ_5       ,
        "MD_KVA_TZ_6"                        : MD_KVA_TZ_6       ,
        "MD_KVA_TZ_7"                        : MD_KVA_TZ_7       ,
        "MD_KVA_TZ_8"                        : MD_KVA_TZ_8       ,
        "CUM_ENG_KWH_EXP"                    : CUM_ENG_KWH_EXP   ,
        "CUM_ENG_KVAH_EXP"                   : CUM_ENG_KVAH_EXP  ,
        "CUM_ENG_KVARH_Q1"                   : CUM_ENG_KVARH_Q1  ,
        "CUM_ENG_KVARH_Q2"                   : CUM_ENG_KVARH_Q2  ,
        "CUM_ENG_KVARH_Q3"                   : CUM_ENG_KVARH_Q3  ,
        "CUM_ENG_KVARH_Q4"                   : CUM_ENG_KVARH_Q4  }

   #     print l
        return l   
