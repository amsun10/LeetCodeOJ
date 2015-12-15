
class Solution(object):
    def __init__(self):
        self.a = {1: True,
                  2: True,
                  3: True,
                  4: False,
                }

    def canWinNim(self, n):
        if self.a.has_key(n):
            return self.a[n]
        else:
            print range(len(self.a.keys())+1, n+1)
            for i in range(len(self.a.keys()) + 1, n+1):
                if self.a[i-1] == True:
                   self. a[i] = False

                elif self.a[i-2] == True:
                    self.a[i] = False

                elif self.a[i-3] == True:
                    self.a[i] = False

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
    # print solu.canWinNim(1348820612)