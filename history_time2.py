#!/bin/env python
#-*- coding: utf-8 -*-

from history_all import *
import datetime

def get_datetime(date_str):
   return datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

def history_by_date(history_list, stary_date, end_date):
   cmd_list=[]
   for h in history_list:
       history_date = get_datetime(h[0])
       print (history_date)
       if(history_date >= start_date and history_date <= end_date):
          cmd_list.append(h)
       return cmd_list

if __name__ == "__main__":
   print "어느 시간에 실행한 명령어를 조회하시겠습니까?"
   input_date = raw_input("년-월-일 시각을 입력하세요(예 - 2016 -08 - 11 14) : ")
   input_date = input_date + ":00:00"

   date = get_datetime(input_date)
   start_date = date - datetime.timedelta(hours=1)
   end_date = date + datetime.timedelta(hours=1)
   
   print start_date, "~", end_date, "동안 입력된 명령어"
   print "-" * 70

   accounts = get_accounts()
   
   for account in accounts:
       history_list = history(account)
       if len(history_list)==0:
          continue

       history_list=history_by_date(history_list, start_date, end_date)
       if len(history_list)==0:
          continue

       print "계정 :", account
       for h in history_list :
           print "\t%s\t%s" % h
       print "-" * 70
    
