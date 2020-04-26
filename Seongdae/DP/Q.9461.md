## 문제

https://www.acmicpc.net/problem/9461

## 접근법
점화식 접근:

문제에서 주어진 수열: 1, 1, 1, 2, 2, 3, 4, 5, 7, 9
* 직관적으로 바라봤을 때, f(n) : f(n-2) + f(n-3) 임을 알 수 있었다

그러나 왜 그렇게 될까?

이 문제는 점화식 도출을 통해서 아주 직관적으로 풀었지만, 다른 문제에서도 적용 할 수 있을지 모르겠다..


## 코드

```
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    dp = [0 for i in range(N-1)]
    dp[:2] = 1,1,1
    for i in range(3,N):
        dp[i] = dp[i-2] + dp[i-3]
    print(dp[N-1])
```