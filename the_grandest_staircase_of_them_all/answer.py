
def answer(bricks):
    N = bricks + 1
    dp = [[0] * N for _ in range(N)]

    for c in reversed(range(1, N)):
        for b in range(1, N):
            if c >= b:
                dp[c][b] = 1
            else:
                dp[c][b] = dp[c + 1][b - 1] + dp[c + 1][b - c - 1]

    return dp[1][bricks] - 1