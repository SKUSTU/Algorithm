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