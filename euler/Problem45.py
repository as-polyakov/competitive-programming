
def k():
    v = {2 : 1}
    M, m = 2, 1
    while(not ( (m + 1) // 3 > 165 and M % 3 == 0 and (M // 3 in v) and match(v[M // 3], m))):
        m += 1
        M = m * (m + 1)
        v[M] = m
    n = v[M // 3]
    k = (m + 1) // 3
    l = (n + 1) // 2
    print("n = " + str(n) + " k = " + str(k) + " l = " + str(l))
    print(n * (n + 1) // 2)
    #print(k * (3 * k - 1) // 2)
    #print(l * (2 * l - 1))

def match(n, m):
    a = (2 * m + 1)
    return (a + 1) % 6 == 0 and (n + 1) % 2 == 0

if __name__ == "__main__":
    k()

