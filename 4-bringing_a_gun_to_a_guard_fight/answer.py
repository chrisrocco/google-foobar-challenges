from collections import deque

def answer((rows, cols), (xStart, yStart), (xTarget, yTarget), limit):

    def neighbors(x, y):
        yield flip(x, 0), y
        yield flip(x, rows), y
        yield x, flip(y, 0)
        yield x, flip(y, cols)

    # Captain remembers the Pythagorean Formula from high-school! ..And he never thought he'd use it!
    # He realizes that if he can stretch the winding path of the laser into on straight line,
    # it will be easy to calculate the total length!
    canReach = lambda x, y: limit**2 >= (y - yStart)**2 + (x - xStart)**2

    # Captain also happens to be a pool shark; he knows to aim BEYOND the table for easier bank shots!
    flip = lambda point, axis: point - ((point - axis) * 2)

    # Captain notices he's repeating himself, so he starts writing down answers.
    visited = set()
    key = lambda x, y: '{},{}'.format(x, y)

    def bfs(node):
        queue = deque([node])
        count = 0
        while len(queue) != 0:
            (x, y) = queue.popleft()
            if not canReach(x, y): continue
            if key(x, y) in visited: continue
            visited.add(key(x, y))
            count += 1
            for (xx, yy) in neighbors(x, y):
                if not(xx == xStart or yy == yStart):
                    queue.append((xx, yy))
        return count

    return bfs((xTarget, yTarget))

    # CAN'T DFS. CALL STACK TOO DEEP
    # def reducer(acc, (x, y)):
    #     if x == xStart or y == yStart: return acc  # *Phew* - that was a close one. Captain almost shot himself!
    #     return acc + dfs(x, y)

    # def dfs(x, y):
    #     if not canReach(x, y): return 0
    #     if key(x, y) in visited: return 0
    #     visited.add(key(x, y))
    #     return reduce(reducer, neighbors(x, y), 0) + 1

    # return dfs(xTarget, yTarget)
