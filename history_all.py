#!/bin/env python3
#-*- coding: utf-8 -*-

# echo 'export HISTTIMEFORMAT="%F %T "' >> /etc/profile

from user_list import *
from datetime import datetime

def remove_num(string):
    tmp = string.strip()
    first_space = tmp.find(" ")
    if first_space < 0:
        return string
    tmp= tmp[first_space : len(tmp)]
    return tmp.strip()

def history(account):
    ret= exec_cmd("sudo -H -u %s bash -i -c 'history -r; history'" % account)
    # print(ret)
    ret_split = ret.strip().split("\n")
    
    # print(ret_split)
    i= len(ret_split) - 1
    history_list= []
    while i > 0:
        # print(ret_split[i])
        cmd= ret_split[i].strip()
        # print(cmd)
        # cmd= ret_split.strip()
        timestamp = ret_split[i-1]
        # print(timestamp)
        i= i-2
        
        if timestamp.find("#") < 0:
            # continue
            break
        cmd= remove_num(cmd)
        timestamp= remove_num(timestamp)
        
        timestamp= timestamp.replace("#", "")
        date= str(datetime.fromtimestamp(float(timestamp)))
        history_list.append((date, cmd))
    return history_list

if __name__ == '__main__':
    accouts= get_accounts()
    
    file = open('report.txt', "w")
    for account in accouts:        
        print("계정 : ", account)
        file.write("계정 : {0}".format(account))
        
        history_list= history(account)
        
        if len(history_list) == 0:
            print("\t 기록된 이력이 없음")
            file.write("\t 기록된 이력이 없음")
            file.write("\n")
        for h in history_list:
            print( "\t %s \t %s" % h)
            file.write("\t {0} \t {1}".format(h[0], h[1]))
            file.write("\n")
        print("-" * 70)
            # file.write("-"* 70)
            # file.write("\n")
    file.close()
            
