# python3

import math
def is_prime(n):
    #print(str(n))
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solve():
    count, sum = 0, 0
    i = 1
    while(count < 11):
        c = 6 * i + 1
        if check(c):
            print('found ' + str(c))
            count += 1
            sum += c

        c = 6 * i + 5
        if check(c):
            print('found ' + str(c))
            count += 1
            sum += c
        i += 1
    return sum

def check(n):
    if n in {2, 3, 5, 7}:
        return False
        
    d = math.floor(math.log(n, 10))
    if not is_prime(n // int(math.pow(10, d))) or not is_prime(n % 10):
        return False
    i = d
    while(i > 0):
        if not is_prime(n // int(math.pow(10, d - i))) or not is_prime(n % int(math.pow(10, i))):
                return False
        i -= 1
    return True

if __name__ == '__main__':
    print(solve())
    #print(check(41))



    
