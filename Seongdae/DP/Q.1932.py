#!/usr/bin/env python
# coding: utf-8

# In[244]:


# Q.1932
N = int(input())
tri = []
for i in range(N):
    tri.append(list(map(int, input().split())))
index = 2
# tri 돌아다니는 인덱스
for head in range(1, N):
    for j in range(index):
        if j == 0:
            tri[head][j] = tri[head][j] + tri[head - 1][j]
            # 맨 왼쪽 경우
        elif head == j:
            tri[head][j] = tri[head][j] + tri[head - 1][j - 1]
            # 맨 오른쪽 경우 
        else:
            tri[head][j] = max(tri[head - 1][j - 1], 
                               tri[head - 1][j]) + tri[head][j]
            # 다른 모든 경우, 왼쪽의 합_오른쪽의 합 중 큰 경우를 선택함
    index += 1
    # 트리 한층 내려갈때마다 탐색 범위 넓어짐(tri가 아래로 갈수록 넓어지므로 1칸씩)
print(max(tri[N - 1]))


# In[245]:


tri


# In[247]:


# Q.1932
N = int(input())
tri, k = [], 2
for i in range(N):
    tri.append(list(map(int, input().split())))
for i in range(1, N):
    for j in range(k):
        if j == 0: tri[i][j] = tri[i][j] + tri[i - 1][j]
        elif i == j:tri[i][j] = tri[i][j] + tri[i - 1][j - 1]
        else:  tri[i][j] = max(tri[i - 1][j - 1], tri[i - 1][j]) + tri[i][j]
    k += 1
print(max(tri[N - 1]))


# In[ ]:




