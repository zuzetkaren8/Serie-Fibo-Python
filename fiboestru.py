# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 21:21:06 2022

@author: Zuzet Sanga
"""

def fibo(signature, n):
    if n:
        resu = signature.copy()

        if n<3:
            return resu[0:n]

        for i in range(2,n-1):
            el = resu[i-2]+resu[i-1]+resu[i]
            resu.append(el)

        return resu

    return []
print("Introduce la cantidad de numeros que deseas de la secuencia de fibonacci: ")
m=input()
cant = int(m)
print(fibo([0,1,1], cant))