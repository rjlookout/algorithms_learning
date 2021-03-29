# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 18:26:47 2020

@author: RJ
"""

def partition(a,p,r):
    x=a[r]
    i=p-1
    for j in range(p,r):
        if a[j]<=x:
            i=i+1
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
    temp2=a[i+1]
    a[i+1]=a[r]
    a[r]=temp2
    return i+1

def quicksort(a,p,r):
    if p<r:
        q=partition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1,r)
        
if __name__=="__main__":
    b=[1,3,1,5,0,9,80,75,3,-9,3,11,0,-10]
    n=len(b)
    quicksort(b,0,n-1)
    print(b)
