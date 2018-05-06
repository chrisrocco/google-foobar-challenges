
def answer(state):

    # Setup a mutable matrix representing the previous state
    rows = len(state) + 1
    cols = len(state[0]) + 1
    board = [[0] * cols for _ in range(rows)]

    # Backtracking and DP data-structures
    memo = {}
    history = []

    # Hashes a sub-problem into a key for memoization
    def key(i, j):
        # The previous 'rows + 1' moves uniquely identify this sub-problem
        return '{},{} => {}'.format(i, j, history[-(rows+1):])

    # Validates the next placement. Note that we _never_ make an invalid placement
    def can_put(i, j, choice):
        if i == 0 or j == 0:
            return 1

        alive = state[i-1][j-1]
        neighbors = board[i-1][j] + \
                    board[i-1][j-1] + \
                    board[i][j-1] + \
                    choice

        # check if this move would satisfy problem constraints
        return (neighbors == 1 and alive) or (neighbors != 1 and not alive)

    # Recursive function to permute possible board states
    def put(i, j):
        if i >= rows:  # line wrap for easier traversal
            i = 0
            j += 1
        if j >= cols:  # found solution - placed valid cells on the entire board
            return 1

        # DP lookup
        if key(i, j) in memo:
            return memo[key(i, j)]

        found = 0
        for opt in [1, 0]:  # Try all possible options
            if can_put(i, j, opt):
                board[i][j] = opt
                history.append(opt)
                found += put(i + 1, j)
                history.pop()

        memo[key(i, j)] = found
        return found

    return put(0, 0)
