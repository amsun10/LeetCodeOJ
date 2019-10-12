__author__ = 'amsun'
"https://leetcode.com/problems/excel-sheet-column-number/"

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        base = 26
        num = 0
        len_s = len(s)
        for index, i in enumerate(s):
            j = (ord(i) - 64)
            num += j * (base ** (len_s - index - 1))
            pass
        return num

if __name__ == '__main__':
    solu = Solution()
    print solu.titleToNumber('AA')
