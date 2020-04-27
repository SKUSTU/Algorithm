import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    dp = [0 for i in range(N-1)]
    dp[:2] = 1,1,1
    
    for i in range(3,N):
        dp[i] = dp[i-2] + dp[i-3]
        
    print(dp[N-1])