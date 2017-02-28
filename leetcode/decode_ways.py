# python3

class Solution:
    def __init__(self):
        self.cache = {}

    def numDecodings(self, s):
        s = s.strip()
        if len(s) == 0:
            return 0
        return self.numDecodingsInt(s)
    
    def numDecodingsInt(self, s):
        if len(s) == 0:
            return 1
        if len(s) in self.cache:
            return self.cache[len(s)]
        res = 0
        if len(s) >= 2 and int(s[:2]) <= 26 and int(s[:2]) >= 10:
            res = self.numDecodingsInt(s[1:]) + self.numDecodingsInt(s[2:])
        elif int(s[:1]) > 0:
            res = self.numDecodingsInt(s[1:])
        self.cache[len(s)] = res
        return res

if __name__ == '__main__':
    s = input().strip()
    print(Solution().numDecodings(s))
    

