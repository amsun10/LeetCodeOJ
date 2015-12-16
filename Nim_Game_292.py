
class Solution(object):
    def __init__(self):
        self.a = {}

    def reset_dic(self):
        self.a = {1: True,
                  2: True,
                  3: True,
                  4: False,
                  }

    def canWinNim(self, n):
        self.reset_dic()
        if self.a.has_key(n):
            return self.a[n]
        else:
            for i in xrange(len(self.a.keys()) + 1, n+1):
                self.a[i] = not (self.a[i-1] and self.a[i-2] and self.a[i-3])
                self.a = {i: self.a[i],
                          i-1: self.a[i-1],
                          i-2: self.a[i-2]}
        return self.a[n]

if __name__ == '__main__':
    solu = Solution()
    print solu.canWinNim(1)
    print solu.canWinNim(2)
    print solu.canWinNim(3)
    print solu.canWinNim(4)
    print solu.canWinNim(5)
    print solu.canWinNim(6)
    print solu.canWinNim(7)
    print solu.canWinNim(8)
    print solu.canWinNim(9)
    print solu.canWinNim(10)
    print solu.canWinNim(11)
    print "--------------------------"
    print solu.canWinNim(1348820612)