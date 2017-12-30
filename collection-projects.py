1  #!/usr/bin/python
2  # -*- coding:utf-8 -*- 
3  #Author: Lingchao Chen

import requests
import time
import os

#set your github account
github_account=('', '')


def request(url,github_account):
    r = requests.get(url,auth=github_account)
    response_dict = r.json()
    return response_dict

def get_num(url):
    data=request(url,github_account)
    total_num=data["total_count"]
    return total_num

def writedata(repo_dicts,i):
    file = open("new-log5.txt", "a")
    repo_dicti = repo_dicts[i]
    print repo_dicti['git_url']
    file.writelines(repo_dicti['git_url'])
    file.writelines("\n")


def collect_data(url,total_num):
    num=int(total_num/100)+1
    print num
    for j in range(1,num+1):
        print j
        url = url + '&page=' + str(j)
        data=request(url,github_account)
        print data
        repo_dicts=data['items']
        lenth=len(repo_dicts)
        print lenth
        i=0
        while(i<lenth):
            writedata(repo_dicts,i)
            i=i+1


        time.sleep(10)


def main():
    #set start folks 
    end_num=15594
    #set end folks    
    while(end_num>10):
        start_num=int(end_num*0.95)
        url = 'https://api.github.com/search/repositories?q=language:Java+forks:' + str(start_num) + '..' + str(end_num) + '&per_page=100&order=desc&sort=forks'
        total_num=get_num(url)
        if total_num>0:
            collect_data(url,total_num)
        end_num=start_num

main()







