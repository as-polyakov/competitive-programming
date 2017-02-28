
def solve(n, k):
    if n <= 1:
        return 1
    if k > n:
        return solve(n, n)
    if c[n][k] != None:
        return c[n][k]

    s = 0
    for i in range(1, k + 1):
        s += solve(n - i, i)

    c[n][k] = s
    return s

if __name__ == '__main__':
    n = int(input())
    c = [ [None] * (n + 1)] * (n + 1)
    print(solve(n, n) - 1)
