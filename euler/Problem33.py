# python3

def solve():
    res = []
    for x in range(1, 10):
        for z in range(1, 10):
            y = 10 * x * z // (9 * z + x)
            if 10 * x * z % (9 * z + x) == 0 and x * z / (9 * z + x ) < 1 and x != y:
                res.append((10 * z + x,10 * x + y))
    return res;

def factorize(n):
    i = 2
    res = {}
    N = n
    while i * i < N:
        k = 0
        while n % i == 0:
            k += 1
            n //= i
        if k > 0:
            res[i] = k
        i += 1
    return res


if __name__ == '__main__':
    X, Y = 1, 1
    for n in solve():
        X *= n[0]
        Y *= n[1]
    Xf = factorize(X)
    Yf = factorize(Y)
    print(Xf)
    print(Yf)
    res = 1
    for k in Yf.keys():
        p = Yf[k] if k not in Xf else max(0, Yf[k] - Xf[k])
        res *= k ** p
    print(res)
