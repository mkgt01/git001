#!/bin/env python3
#-*- coding: utf-8 -*-

from subprocess import *

def exec_cmd(cmd):
    p= Popen(cmd, shell= True, stdout=PIPE, encoding= 'cp949')
    # print(p)
    (ret, err)= p.communicate()    
    # print(ret, err)
    return ret

def grep_login_defs(keyword):
    ret= exec_cmd("grep '%s' /etc/login.defs" % keyword)
    # print(ret)
    return ret.split()[1]
    
def get_accounts():
    min_u= grep_login_defs("^UID_MIN")
    max_u= grep_login_defs("^UID_MAX")
    
    # print(min_u, max_u)
    
    cmd= ("awk -F':' -v 'min=%s'") % min_u
    # print(cmd)
    cmd= cmd + (" -v 'max=%s'") % max_u
    # print(cmd)
    cmd= cmd + (" '{ if ($3 >= min && $3 <= max) print $1}' /etc/passwd")
    # print(cmd)
    answer= exec_cmd(cmd).split()
    # print(answer) 
    return answer

if __name__ == '__main__':
    accouts= get_accounts()
    for account in accouts:
        print(account)
