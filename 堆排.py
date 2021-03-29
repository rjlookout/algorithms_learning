# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:42:16 2020

@author: RJ
"""

import math

def max_heapify(a,i,n): ###最大堆操作
    left=2*i+1
    right=2*i+2
    if left<=n-1 and a[left]>a[i]:
        lag=left
    else:
        lag=i
    if right<=n-1 and a[right]>a[lag]:
        lag=right
    if lag!=i:
        temp=a[i]
        a[i]=a[lag]
        a[lag]=temp
        max_heapify(a,lag,n)


def duipai(a):
    ##建堆以及最大堆操作
    n=len(a)
    half_m=math.floor(n)
    for i in range(half_m-1,-1,-1):
        max_heapify(a,i,n)
    ##拆堆
    for i in range(n-1,0,-1):
        temp=a[i]
        a[i]=a[0]
        a[0]=temp
        n=n-1
        max_heapify(a,0,n)
    return a
        
##测试
if __name__=="__main__":
    b=[1,3,1,5,0,9,80,75,3,-9,3,11]
    c=duipai(b)
    print(c)