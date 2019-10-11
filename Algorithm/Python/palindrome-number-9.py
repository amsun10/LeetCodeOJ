# https://leetcode.com/problems/palindrome-number/

# Determine whether an integer is a palindrome. An
# integer is a palindrome when it reads the same backward as forward.
#
# Example 1:
#
# Input: 121
# Output: true
# Example 2:
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
#
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Follow up:
#
# Coud you solve it without converting the integer to a string?


class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_pal = str(x)

        i = 0
        j = len(str_pal) - 1

        while str_pal[i] == str_pal[j]:
            i += 1
            j -= 1
            if i >= j:
                break
        else:
            return False

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(1))
    print(solution.isPalindrome(121))
    print(solution.isPalindrome(-121))
