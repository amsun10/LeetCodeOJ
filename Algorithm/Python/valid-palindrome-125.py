# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        pre_order = ''.join([x.lower() for x in s if x.isalpha() or x.isdigit()])
        reverse = ''.join([x.lower() for x in s[::-1] if x.isalpha() or x.isdigit()])

        print(pre_order)
        print(reverse)

        return pre_order == reverse

if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))