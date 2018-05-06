
def answer(state):

    # Setup a mutable matrix representing the previous state
    rows = len(state) + 1
    cols = len(state[0]) + 1
    board = [[0] * cols for _ in range(rows)]

    # Backtracking and DP data-structures
    memo = {}
    history = []

    # Hashes a sub-problem into a key for memoization
    def key(row, col):
        # The last 'rows + 1' moves uniquely identify this sub-problem
        return '{},{} => {}'.format(row, col, history[-(rows+1):])

    # Validates the next placement. Note that we _never_ make an invalid placement
    def can_put(row, col, choice):
        if row == 0 or col == 0:
            return 1

        alive = state[row-1][col-1]
        neighbors = board[row-1][col] + \
                    board[row-1][col-1] + \
                    board[row][col-1] + \
                    choice

        # check if this move would satisfy problem constraints
        return (neighbors == 1 and alive) or (neighbors != 1 and not alive)

    # Recursive function to permute possible board states
    def put(row, col):
        if row >= rows:  # line wrap for easier traversal
            row = 0
            col += 1
        if col >= cols:  # found solution - entire board is filled with valid cells
            return 1

        # DP lookup
        if key(row, col) in memo:
            return memo[key(row, col)]

        # Try all possible options
        found = 0
        for opt in [1, 0]:
            if can_put(row, col, opt):
                board[row][col] = opt
                history.append(opt)
                found += put(row + 1, col)
                history.pop()

        memo[key(row, col)] = found
        return found

    return put(0, 0)
