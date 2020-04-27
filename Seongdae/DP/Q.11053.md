## 문제

https://www.acmicpc.net/problem/11053

## 접근법

수열이 주어지고, 가장 긴 증가하는 부분 수열을 구하는 프로그램이다.

ex) A = {10, 20, 10, 30, 20, 50} 일때, 

**10**, **20**, 10, **30**, 20, **50**

10 20 30 50 증가하는 부분 수열을 관찰 할 수 있으며, 이 길이는 4이다.

for문을 돌며, i번째 까지의 수열중 가장 긴 부분 수열을 찾는다.
    - 첫번째 인덱스부터 수열의 길이의 최대값을 저장해나감

언제 i번째 숫자가 증가하는 수열에 포함시키는가?(갱신)
    - i번째 숫자는 항상 i-1번째 숫자보다 커야함(포함조건)
    - 자기 자신보다 작은 숫자들 중 가장 큰 길이를 구하고, 그 길이에 +1을 해서 갱신 (동작) 
    


## 코드
```
import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(N)]

for i in range(0, N): # 0부터 N번까지 _ i
    min_value = 0
    for j in range(i):
        # 현재 인덱스의 수가 더 큰 경우는 작은 경우의 수에다 +1
        if a[i] > a[j]:
            min_value = max(min_value, dp[j])
    dp[i] = min_value+1
    
print(max(dp))

```
