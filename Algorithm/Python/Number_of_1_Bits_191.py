__author__ = 'amsun'
"https://leetcode.com/problems/number-of-1-bits/"

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 0:
            if n % 2 != 0:
                count += 1
            n = int(n/2)
        return count


if __name__ == '__main__':
    solu = Solution()
    print solu.hammingWeight(24)