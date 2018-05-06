
# def answer( numStr ):
#     n = int(numStr)
#
#     def helper( number ):
#         if number & 1 == 0:  # if the last bit is a 0
#             return number >> 1
#         if number & 2 == 0:  # if the second-to-last bit is a 0
#             return number - 1
#         return number + 1  # else, add 1
#
#     cnt = 0
#     while n != 1:
#         n = helper(n)
#         cnt += 1
#
#     return cnt

from collections import deque

def answer(numStr):
    number = int(numStr)
    d = {}
    s = set()
    d = {"yes": "no"}
    s = {"yes", "no"}
    queue = deque()
    queue.append((number, 0))

    while len(queue) > 0:
        n, cnt = queue.pop()
        if n == 1:
            return cnt

        if n & 1 == 0:
            queue.appendleft((n >> 1, cnt + 1))
            continue
        queue.appendleft((n + 1, cnt + 1))
        queue.appendleft((n - 1, cnt + 1))
