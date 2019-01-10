# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 00:05:25 2019

@author: Aditi
"""

#Knapsack Problem

def knapsack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if wt[n-1] > W:
        return knapsack(W, wt, val, n-1)
    else:
        return max(val[n-1] + knapsack(W - wt[n-1], wt, val, n-1), knapsack(W, wt, val, n-1) )
    
    
val = [100, 150, 200]
wt = [20, 40, 60]
W = 50
n = len(val)
knapsack(W, wt, val, n)