## 문제

https://www.acmicpc.net/problem/10844

## 접근법

인접한 모든 자리수의 차이가 1이 날 경우, 계단 수라고 한다.

- ex) 45656

N이 주어졌을때, 길이가 N인, 계단 수가 몇개 있는지 구해야 한다.

- 인접한 자리수를 비교하는 수가 0인 경우 -> 다음 숫자가 줄어들 수 없음
    
- 인접한 자리수를 비교하는 수가 9인 경우 -> 다음 숫자가 커질 수 없음

2중 for문을 통해, dp[][] 배열에 값을 갱신

위의 고려사항을 if문으로 for문 내에 내포함


## 코드
```
import sys
input = sys.stdin.readline

N = int(input())
mil = 1000000000
dp = [[0 for _ in range(10)]for _ in range(N+1)]
# 2차원 배열 초기화

for i in range(1, N+1):
    for j in range(10):
        if i == 1 : 
        # 한자리 경우
            if j >0 : dp[1][j] = 1
            else : dp[1][j] = 0
        else:
        # 두자리 이상(N>1)
            # 이전자리 계단 수의 갯수를 더해서 갱신
            if j > 0: dp[i][j] += dp[i-1][j-1]
            if j < 9: dp[i][j] += dp[i-1][j+1]
            dp[i][j] %= mil
            
print(sum(dp[N])%mil) # N번째 자리 출력
```