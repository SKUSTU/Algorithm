import sys
input = sys.stdin.readline
Tlist, Plist = [],[]
N = int(input())
for _ in range(N):
    t,p = map(int, input().split())
    Tlist+=[t]
    Plist+=[p]
T, P, DP = Tlist[:], Plist[:], Plist[:]
DP.append(0)
for i in range(N-1, -1, -1):
    if (T[i]+i) > N:
        DP[i] = DP[i+1]
    else:
        DP[i] = max(DP[i+1], P[i] + DP[i+T[i]])
print(DP[0])