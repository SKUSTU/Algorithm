#!/usr/bin/env python
# coding: utf-8
import sys
input = sys.stdin.readline

N = int(input())
ans = [ 0 for _ in range(N)]
n = list(map(int, input().split(' ')))
ans[0] = n[0]

for i in range(1, N):
    ans[i] = ans[i-1]+n[i] if (ans[i-1]+n[i])>=n[i] else n[i]
    
print(max(ans))
