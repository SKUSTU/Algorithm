## 문제

https://www.acmicpc.net/problem/11052

## 접근법

1팩 구매 : 1번팩 1개

2팩 구매 : 2번팩 2개, 1번팩 2개 중 큰수 
   
    여기까지 초기화

3팩 구매 : 3번팩 1개, 2팩+1팩 경우

4팩 구매 : 4번팩 1개, 3팩+1팩 경우, 2팩 2개 경우

n팩 구매

    max(dp[n] case, dp[1]+dp[n-1] case, dp[2]+do[n-2] case, ... dp[i]+dp[n-i] case)

점화식 : dp[n] = max(dp[n], dp[i] + dp[n-i])


## 코드

```
import sys
input = sys.stdin.readline

N, card = int(input()), [0]
card += list(map(int, input().split()))

if N == 1: print(card[1])
else:
    dp = [0] * (N+1)
    dp[1] = card[1]
    dp[2] = max(card[2], card[1]*2)

    for i in range(3, N+1):
        dp[i] = card[i] #자기 자신으로 가장 비싼 경우
        for j in range(1, i//2 + 1): #j와 i-j로 만드는 경우, 
                        # i index의 middle값
            dp[i] = max(dp[i], dp[j] + dp[i-j])

    print(dp[N])
```