# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 21:53:12 2022

@author: Zuzet Sanga
"""

def fibo(n) :
    if (n == 0 ) :
        return 0
    if(n==1):
        res = 0
        return res
    if(n==2):
        res =1
        return res
    elif (n == 3) :
        res=1
        return res
    else :
        return (fibo(n - 1) +
                fibo(n - 2) +
                fibo(n - 3))
         
 
def resu(n) :
    for i in range(1, n+1) :
        print( fibo(i) , " ", end = "")
         
 
# Driver code
n = input()
cant = int(n)
print(resu(cant))