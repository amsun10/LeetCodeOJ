# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits=[]) -> []:
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            digits_len = len(digits) - 1
            while digits[digits_len] == 9:
                digits[digits_len] = 0
                digits_len -= 1
                if digits_len == -1:
                    break

            if digits_len == -1:
                digits.insert(0, 1)
            else:
                digits[digits_len] += 1

        return digits


if __name__ == '__main__':
    solution = Solution()
    print(solution.plusOne([9, 8, 9]))


