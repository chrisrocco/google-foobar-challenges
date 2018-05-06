
def answer(state):

    rows = len(state) + 1
    cols = len(state[0]) + 1
    board = [[0] * cols for _ in range(rows)]

    memo = {}
    history = []

    def key(i, j):
        return '{},{} => {}'.format(i, j, history[-(rows+1):])

    def canPut(i, j, choice):
        if i == 0 or j == 0:
            return True
        alive = state[i-1][j-1]
        neighbors = board[i-1][j] + \
                 board[i-1][j-1] + \
                 board[i][j-1] + choice

        return (neighbors == 1 and alive) or (neighbors != 1 and not alive)

    def put(i, j):
        if i >= rows:              # line wrap
            i = 0
            j += 1
        if j >= cols:                 # found solution
            return 1

        if key(i, j) in memo:
            return memo[key(i, j)]

        found = 0
        for opt in [1, 0]:
            if canPut(i, j, opt):
                board[i][j] = opt
                history.append(opt)
                found += put(i + 1, j)
                history.pop()

        memo[key(i, j)] = found
        return found

    return put(0, 0)
