## 문제
--------------

https://www.acmicpc.net/problem/11727

## 접근법
--------------
점화식 접근:

* 2x0 -> 0, 초기화

* 2x1 직사각형을 채우는 case -> 1, 초기화

* 2x2 직사각형을 채우는 case -> 3, 초기화
     * 2x1로 채우는 경우 2가지, 2x2로 채우는 경우 1

* 2x3 ?? -> 2x2 case + 2x1 case(좌측에 들어갈 경우, 우측에 들어갈 경우)*2 

f(n) : f(n-1) + f(n-2)*2


## 코드
--------------

```
import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for i in range(n)]
dp[1:2] = 1,3
for i in range(3,n+1):
    dp[i] = (dp[i-1] + (dp[i-2]*2))%10007
print(dp[n])


```