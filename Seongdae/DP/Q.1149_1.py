#!/usr/bin/env python
# coding: utf-8

# In[5]:


#top-down 
n = int(input())
rgb = [[int(x) for x in input().split()] for i in range(n)]


# In[6]:


def dp(lev):
    if lev == -1:
        return [0,0,0]
    cache = dp(lev-1)
    rgb[lev][0] += min(cache[1], cache[2])
    rgb[lev][1] += min(cache[0], cache[2])
    rgb[lev][2] += min(cache[0], cache[1])
    return rgb[lev]


# In[19]:


print(min(dp(n-1)))


# In[ ]:


import sys
sys.setrecursionlimit(10**6)


# In[20]:


S = []


N = int(input())
for _ in range(N):
    S.append(list(map(int, input().split())))

D = [(S[0][0], S[0][1], S[0][2])]

for i in range(1, N):
    temp1 = min(D[i-1][1], D[i-1][2]) + S[i][0]
    temp2 = min(D[i-1][0], D[i-1][2]) + S[i][1]
    temp3 = min(D[i-1][0], D[i-1][1]) + S[i][2]
    D.append((temp1, temp2, temp3))
print(min(D[N-1][0], D[N-1][1], D[N-1][2]))


# In[23]:


D


# In[25]:


S[1][0]


# In[ ]:




