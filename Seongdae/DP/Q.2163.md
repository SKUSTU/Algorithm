## 문제

https://www.acmicpc.net/problem/2163

## 접근법

NxM 크기의 초콜릿이 주어진다. 이를 1x1 조각으로 모두 자르려 할 때, 최소한의 수행횟수를 구하라

작은 문제부터 생각해서, N크기를 1의 크기로 쪼개기 위해선 N-1의 동작이 필요하다
- ex) 5x1 크기 초콜릿 -> 4번 쪼개야함

마찬가지로 M크기도 M-1번의 수행을 거치는데, 그 M-1번의 수행을 N번 반복해야하기 때문에
- (N-1) + (M-1)*N 의 결과값이 답이 된다


## 코드
```
import sys
input = sys.stdin.readline
N,M = map(int, input().split())
print((N-1)+((M-1)*(N)))

```
