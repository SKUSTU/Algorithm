#!/usr/bin/env python
# coding: utf-8

# In[129]:


# Q.2156
N = int(input())
test = [0,]
for _ in range(N):
    test.append(int(input()))


# In[130]:


dp = [[0 for _ in range(N+1)]for _ in range(4)]
    


# In[131]:


# dp


# In[132]:


for i in range(1, N+1):
    dp[0][i] = dp[2][i-1] + test[i]
    # 11 이전 잔과 이번 잔 모두 마심
    dp[1][i] = max(dp[0][i-1], dp[2][i-1])
    # 10 이전 잔만 마심
    dp[2][i] = max(dp[1][i-1], dp[3][i-1]) + test[i]
    # 01 이번 잔만 마심
    dp[3][i] = max(dp[1][i-1], dp[3][i-1])
    # 00 이전 잔과 이번잔을 모두 마시지 않음
print(max(dp[0][N], dp[1][N], dp[2][N], dp[3][N]))


# In[ ]:


N = int(input())
test = [0,]
for _ in range(N):
    test.append(int(input()))
dp = [[0 for _ in range(N+1)]for _ in range(4)]
for i in range(1, N+1):
    dp[0][i] = dp[2][i-1] + test[i]
    dp[1][i] = max(dp[0][i-1], dp[2][i-1])
    dp[2][i] = max(dp[1][i-1], dp[3][i-1]) + test[i]
    dp[3][i] = max(dp[1][i-1], dp[3][i-1])
print(max(dp[0][N], dp[1][N], dp[2][N], dp[3][N]))


# In[136]:


for i in range(N):
    print(max(dp[0][i], dp[1][i], dp[2][i], dp[3][i]))


# In[165]:


N = int(input())
test = [0,]
for _ in range(N):
    test.append(int(input()))
dp = [0 for _ in range(4)]
for i in range(1, N+1):
    temp = []
    temp += [
        dp[2] + test[i],
        max(dp[0], dp[2]),
        max(dp[1], dp[3]) +test[i],
        max(dp[1], dp[3])
    ]
    dp = temp

print(max(temp))


# In[166]:


temp


# In[ ]:


import sys
input = sys.stdin.readline

