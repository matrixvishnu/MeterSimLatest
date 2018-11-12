#!/usr/bin/python
import sys
import os
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

df_log = pd.DataFrame()
timestamp = []
log_fip = [] 
log_freq = []
log_coscat = []
class Config():
    def file_ip(self):
        global log_fip 
        flag = True
        while flag:
            file_name = raw_input("Enter the file Name:")
            cwd = os.getcwd()
            file_path = cwd +'/'+file_name
            if(os.path.isfile(file_path)):
                print 'File '+ file_path +' found'
                log = file_path +" Found"
                log_fip.append(log)
                timestamp.append(str(datetime.datetime.now()))
                flag  = False
                return file_path
            else:
                log = file_path +" Not found"
                log_fip.append(log)
                timestamp.append(str(datetime.datetime.now()))
                print "File   "+file_path+""" not found in present working directory 
please make sure that csv file is at present working directory"""
    def freq_ip(self):
        global log_freq 
        flag = True 
        while flag:
            time_period = raw_input("Enter the time freequency in secoends :")
            try:
                val = int(time_period)
                print "Freq is "+str(time_period)+"Sec"
                log = str(time_period)
                log_freq.append(log)
                falg = False 
                timestamp.append(str(datetime.datetime.now()))
                return time_period
            except ValueError:
                log = 'invalid freeq'
                print("That's not a valid time input please enter value in secoends")
                log_freq.append(log)
                timestamp.append(str(datetime.datetime.now()))
    def consumerCat(self):
        global log_coscat  
        flag = True 
        while flag:
            consumercat = raw_input("""Enter the consumer category :
        1 for residential 
        2 for industrial
        3 for commercial
        :""")
            consumers = {'1': [0.12,0.22],
                '2' : [10.00,22],
                '3' : [5,15]}
            if(consumercat in consumers):
                log = str(consumercat)
                log_coscat.append(log)
                flag = False
                timestamp.append(str(datetime.datetime.now()))
                return consumers[consumercat]
            else:
                print('Invalid consumercategory select any of the following values 1,2,3')
                log = 'Invalid consumercategory'
                log_coscat.append(log)
                timestamp.append(str(datetime.datetime.now()))
x = Config()
y = x.file_ip()
t= x.freq_ip()
c = x.consumerCat()
print y
print t
print c
print log_fip
print log_freq
print log_coscat
print timestamp


