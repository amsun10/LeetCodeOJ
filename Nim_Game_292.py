
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1 or n == 2 or n == 3:
            return True
        elif n == 4:
            return False
        else:
            while n != 1:
                if n - 1 > 3:
                    n -= 1
                if n - 2 > 3:
                    n -= 2
                if n - 3 > 3:
                    n -= 3
                else:
                    if n - 1 > 3:
                        return True
                    else:
                        return False
            return False

if __name__ == '__main__':
    solu = Solution()
    print solu.canWinNim(1)
    print solu.canWinNim(2)
    print solu.canWinNim(3)
    print solu.canWinNim(4)
    print solu.canWinNim(5)
    print solu.canWinNim(6)
    print solu.canWinNim(7)
    print solu.canWinNim(1348820612)