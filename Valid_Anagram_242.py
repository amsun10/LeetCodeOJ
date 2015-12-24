__author__ = 'amsun'
"https://leetcode.com/problems/valid-anagram/"

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
if __name__ == '__main__':
    solu = Solution()
    print solu.isAnagram("Hello", "World")
    print solu.isAnagram("ab", "a")
    print solu.isAnagram("aacc", "ccac")