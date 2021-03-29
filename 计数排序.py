# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 10:18:32 2020

@author: RJ
"""

def counting_sort(mylist):##只适用于整数排序
    n=len(mylist)
    temp=[]
    outlist=list(range(n))
    
    min_mylist=min(mylist)    
    if min_mylist<0:##负值的正化
        for index in range(n):
            mylist[index]=mylist[index]-min_mylist
    max_mylist=max(mylist)
    
    for i in range(max_mylist+1):
        temp.append(0)
    for j in range(n):
        temp[mylist[j]]=temp[mylist[j]]+1
    for i in range(1,max_mylist+1):
        temp[i]=temp[i]+temp[i-1]
        
    for j in range(n-1,-1,-1):
        outlist[temp[mylist[j]]-1]=mylist[j]
        temp[mylist[j]]=temp[mylist[j]]-1

    if min_mylist<0:##负值的还原
        for index in range(n):
            outlist[index]=outlist[index]+min_mylist
            mylist[index]=mylist[index]+min_mylist
    
    return outlist

if __name__=='__main__':
    mylist=[2,5,3,0,2,3,0,3,-5,-3,0,0,1]
    outlist=counting_sort(mylist)
    print(outlist)
    