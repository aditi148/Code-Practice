# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 23:22:33 2019

@author: Aditi
"""

#Longest Common Subsequence
def LCS(X,Y,m,n):
    if m==0 or n==0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + LCS(X, Y, m-1, n-1)
    else:
        return max(LCS(X, Y, m, n-1), LCS(X, Y, m-1, n))

A= "abcdeeeefgk"
B="eeeejhlkkkt"
LCS(A, B, len(A), len(B))