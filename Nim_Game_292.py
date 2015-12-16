
class Solution(object):
    def canWinNim(self, n):
        if n in [1, 2, 3]:
            return True
        if n == 4:
            return False
        else:
            k = n % 4
            if k == 0:
                return False
            else:
                return True

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