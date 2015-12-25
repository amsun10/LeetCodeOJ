
class Solution(object):
    def canWinNim(self, n):
        return bool(n % 4)

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