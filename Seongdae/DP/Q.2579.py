#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q.2579
# 계단은 한계단 또는 두계단 씩 상승 가능
# 시작점을 제외하고, 연속되게 세개의 계단을 밟아선 안된다
# 마지막 도착 계단은 반드시 밟아야한다

# 이 게임에서 얻을 수 있는 최대값
# 첫쨰 줄 계단의 개수  300이하 자연수
# 둘쨰줄부터 한줄에 하나씩 계단의 순서대로 계단의 점수가 주어짐 10000이하의 자연수


# In[3]:


N = int(input())
s = []
for _ in range(N):
    s.append(int(input()))
    


# In[9]:


# upcount = 0
# index = -1
# required = 0
# result = [0 for _ in range(N)]
# # 인덱스별로 얻은 점수 카운트?

# while index <len(s):
#     if index +1 == len(s)-1:
#         # 두계단은 무조건 오를 수 없는 경우, 한계단 남은 경우
#         index+=1
#         result[index]+= s[index]+required
#     else:
#         if upcount!=2:
#             # 한계단 오르기
#             index, s, upcount, required, result=upper_one(
#                 index, s, upcount, required, result)
#         # 두계단 오르기


# In[42]:


# def upper_one(index, s, upcount, required, result):
#     upcount += 1
#     index+=1
#     required+= s[index]
#     result[index] += s[index]
    
#     return index, s, upcount, required, result

# def upper_two(index, s, upcount, required, result):
#     upcount = 0
#     index+=2
#     required+= s[index]
#     result[index] += s[index]
    
#     return index, s, upcount, required, result


# In[ ]:


# 총 네개의 계단을 올라갈때, 어떤 방법이 더 점수를 얻는지 비교
# 왜 네개냐?
# 연속에서 한개의 계단을 3번 올라갈 수 없으므로, 1개의 계단을 연속해서
# 밟을 경우는 최대 2번, ... 등으로 3개의 경우로 나누어짐 
    # case0 : 1,1,2 -> upcount =1일 때만 검사, upcount=1 end
    # case1 : 1,2,1 -> upcount =1or2 일때 검사, upcount=2 end
    # case2 : 2,2 -> upcount =1or2 일때 검사, upcount=1 end
    
    # case3 : 1,2
    # case4 : 2,1
# upcount == 3면 3연속 발판
# 1. 계단을 4묶음으로 나눔
# 각 묶음 당 할 수 있는 모든 경우를 검사
    # 검사 후 이전 블록과 합산했을 경우, 가장 높은 점수를 가진 경우를 저장하고 다음 블록으로 넘어감
    


# In[116]:


def upper_four(s_tok):
    cal_list = [0,1],[0,2],[0,1]
        # [case0[4칸 점수,upcount], case1.., case3]
    # case0
    cal_list[0][0] += s_tok[0]+s_tok[1]+s_tok[3]
    # case1
    cal_list[1][0] += s_tok[0]+s_tok[2]+s_tok[3]
    # case2
    cal_list[2][0] += s_tok[1]+s_tok[3]
    
    return cal_list
# 밟을 계단들의 점수 합 계산


# In[117]:


four_token = len(s)//4
tok = 0
tok_list = [[] for _ in range(four_token+1)]
    
while tok <four_token:
    tok_list[tok] = s[tok*4:(tok+1)*4]
    tok+=1
tok_list[tok] = s[tok*4:]


# In[123]:


first = [0,1],[0,2],[0,1]
# 앞의 토큰에서
        # case0, case1, case2
for check in tok_list:
    if len(check) ==4:
        second = upper_four(check)
        for i in second:
            if i[1] ==1:
                i[0] = max(first[0][0]+i[0], first[1][0]+i[0],
                           first[2][0]+i[0])
                # 앞의 모든 경우를 뒤의 토큰과 검사, 가장 높은 점수 선택, 나머지 0
            elif i[1] ==2:
                i[0] = max(first[1][0]+i[0], first[2][0]+i[0])
                # 앞의 case1,2경우를 뒤의 토큰과 검사, 가장 높은 점수 선택, 나머지 0
    else:
        # 마지막 부분
        print(check)
        print('직전까지의 합:',first)
        result1, result2 = 0, 0
        for i in first:
            if i[1] == 1:
                if len(check) <2: result =
                result1 = 
            elif i[1]==2:
                if len(check) <2: result-=1
                if i[0]+check[1] > result: result=i[0]+check[1]
                # 무조건 2칸 뛰는것
        
    first = second


# In[119]:


first[0][0]


# In[127]:


print(check)
print('직전까지의 합:',first)
result1, result2 = [0], [0]
for i in first:
    if i[1] == 1: # 1칸 내지, 두칸 올라갈 수 있을경우
        if len(check) ==1: result1.append(i[0]+check[0])
            # 남은 계단이 1칸
        elif len(check) ==2: 
            result1.append(i[0]+check[1])
            # 남은 계단이 2칸
        else:
            result1.append(max(i[0]+check[0]+check[2], i[0]+check[1]+check[2]))
            # 남은 계단이 3칸
    elif i[1]==2:# 무조건 두칸 올라가야하는 경우
        if len(check) ==1: result2.append(-1)# 1칸밖에 없을때
        elif len(check) ==2: result2.append(i[0]+check[1])# 2칸 올라갈 수 있을때
        else: result2.append(-1) # 3칸은 리타이어
        


# In[131]:


print(max(max(result1),max(result2)))


# In[115]:


second


# In[ ]:


# def upper_four(last_list,index, s, upcount, required, result):
#     cal_list = [[,0],[,1],[,2],[,0]]
#         # [case0[4칸 점수,upcount], case1.., case3]
#     if upcount == 0 or upcount==1:
#         if upcount ==0:
#             case_0func() ? case_1func() : 
#                 큰거에 따라 
#                 case0->upcount=0 or case1->upcount=1
#             # case0
#         case_1func()
#         # case1
#     if upcount ==0 or upcount ==1:
        
#         upcount=1
#         # case1


# In[ ]:




