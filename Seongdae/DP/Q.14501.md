## 문제

https://www.acmicpc.net/problem/14501

## 접근법

주어진 날짜 내에서 최대한의 금액을 구하는 문제이다.

- 가격(P[])과 같이 얕은 복사를 받은 DP[]의 끝에 초기값 0 을 추가한 후,

- for문을 역순으로 돌렸다.(정순으로 돌려도 풀이는 가능할 것 같다)

for문 내부 동작 :

    if T[i]+i > N, 주어진 날짜만큼 상담을 진행 하였을 때, 날짜를 초과하는 경우
        - DP[i] = DP[i+1], DP[i+1]의 값(가장 끝값)으로 초기화,(가장 처음일 경우 0)
    
    else, 그 외에 DP[] 갱신 동작
        - DP[i] = max(DP[i+1], P[i] + DP[i+T[i]]), DP[i+T[i]] 정해진 날짜만큼(T[i])
        
| |1일 i = 0|2일 i = 1|3일 i = 2|4일 i = 3|5일 i = 4|6일 i = 5|7일 i = 6| |
|------|---|---|---|---|---|---|---|---|
|T|3|5|1|1|2|4|2||
|P|10|20|10|20|15|40|200||
|DP|45|45|45|35|15|0|0|0||

ex) 예제에서 i가 4일 경우,

    DP[i+1]_DP[5]의 값 '0' <- P[5]는 40 이지만, T[i]+i > N 동작으로 인해 DP[5]는 0이 들어감
    
    DP[i]_DP[4]에 DP[i+1](0) 과 P[i] + DP[i+T[i]] (15+0) 의 값중 큰 15를 넣어줌

ex) 예제에서 i가 3일 경우,

    DP[i+1]_DP[4]의 값 (15), P[i] + DP[i+T[i]] (20+15)의 값중 큰 35를 넣어줌



## 코드
```
import sys
input = sys.stdin.readline

Tlist, Plist = [],[]
N = int(input())
for _ in range(N):
    t,p = map(int, input().split())
    Tlist+=[t]
    Plist+=[p]
T, P, DP = Tlist[:], Plist[:], Plist[:] # 얕은 복사
DP.append(0) # DP[] 맨 끝에 0 추가

for i in range(N-1, -1, -1): # 날짜 끝(N-1)부터 역순으로  0까지, for 루프
    if (T[i]+i) > N: # N을 초과하는 날짜일 경우
        DP[i] = DP[i+1] 
            # DP[i+1]의 값(가장 끝값)으로 초기화,(가장 처음일 경우 0)
    else:
        DP[i] = max(DP[i+1], P[i] + DP[i+T[i]]) 
            # DP[i+T[i]] 정해진 날짜만큼(T[i])
    print(DP[0])
```
