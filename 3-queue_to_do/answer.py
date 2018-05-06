def answer(start, length):
    result = 0
    for row in range(0, length):
        result ^= helper(start, start + length - row - 1)
        start += length
    return result

def helper(start, end):
    if start & 1:
        return helper(start + 1, end) ^ start
    width = end - start + 1
    if width & 1:
        return helper(start, end - 1) ^ end
    return width & 2 != 0