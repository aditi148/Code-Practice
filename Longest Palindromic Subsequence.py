# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 23:42:28 2019

@author: Aditi
"""

#Longest Palindromic Subsequence

def LPS(S, m, n):
    if m == n:
        return 1
    if (S[m] == S[n]) and (m+1 == n):
        return 2
    if (S[m] == S[n]):
        return LPS(S, m+1, n-1) + 2
    
    return max(LPS(S, m+1, n), LPS(S, m, n-1))


Seq= "ALPHABETAALPHA"
LPS(Seq, 0, len(Seq)-1)