#!/usr/bin/env python
# coding: utf-8

import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))

dp = [0 for i in range(N)]
for i in range(0, N):
    min_value = 0
    for j in range(i):
        if a[i] > a[j]:
            min_value = max(min_value, dp[j])
    dp[i] = min_value+1
    
print(max(dp))



