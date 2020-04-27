## 문제
https://www.acmicpc.net/problem/1912

## 접근법
연속된 수를 선택했을 때, 구할 수 있는 합 중 가장 큰 합을 구해야 하기 때문에, 연속하는 모든 경우를 탐색해야 합니다.

그러므로 배열 for문을 진행시키면서, 그전 위치의 인덱스와 이번 위치의 인덱스의 합을 각 비교하여, 큰 값을 넣고 갱신시켜 나갑니다.

    ans[i] = max(ans[i-1] + n[i], n[i]) 
    # max()함수 사용
    ans[i] = ans[i-1]+n[i] if (ans[i-1]+n[i])>=n[i] else n[i] 
    # 삼항연산자 사용
    

## 코드

```
import sys
input = sys.stdin.readline

N = int(input())
ans = [ 0 for _ in range(N)]
n = list(map(int, input().split(' ')))
ans[0] = n[0]

for i in range(1, N):
    ans[i] = ans[i-1]+n[i] if (ans[i-1]+n[i])>=n[i] else n[i]
    
print(max(ans))

```

