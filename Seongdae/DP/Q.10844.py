#!/usr/bin/env python
# coding: utf-8
import sys
input = sys.stdin.readline
N = int(input())
mil = 1000000000
dp = [[0 for _ in range(10)]for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(10):
        if i == 1 : 
            if j >0 : dp[1][j] = 1
            else : dp[1][j] = 0
        else:
            if j > 0: dp[i][j] += dp[i-1][j-1]
            if j < 9: dp[i][j] += dp[i-1][j+1]
            dp[i][j] %= mil

print(sum(dp[N])%mil)




