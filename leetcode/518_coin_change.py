# python3

class Solution:
    def __init__(self):
        self.cache = {}

    def num_ways(self, amount, coins):
        if amount == 0:
            return 1
        if len(coins) == 0:
            return 0
        if (amount, coins[-1]) in self.cache:
            return self.cache[(amount, coins[-1])]

        r = 0
        for idx, c in enumerate(coins):
            if amount - c < 0:
                break
            r += self.num_ways(amount - c, coins[:(idx + 1)])
        self.cache[(amount, coins[-1])] = r
        return r

    def change(self, amount, coins):
        res = 0
        return self.num_ways(amount, sorted(coins))

if __name__ == '__main__':
    amount = int(input())
    coins = list(map(int, input().split()))
    print(Solution().change(amount, coins))
