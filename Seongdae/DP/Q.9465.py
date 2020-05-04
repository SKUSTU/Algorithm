for _ in range(int(input())):
    l = []
    n = int(input())
    for _ in range(2):
        l.append(list(map(int, input().split())))
    l[0][1] += l[1][0]
    l[1][1] += l[0][0]
    for j in range(2, n):
        l[0][j] += max(l[1][j - 1], l[1][j - 2])
        l[1][j] += max(l[0][j - 1], l[0][j - 2])
    print(max(l[0][n - 1], l[1][n - 1]))