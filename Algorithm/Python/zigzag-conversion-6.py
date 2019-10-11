# https://leetcode.com/problems/zigzag-conversion/

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#

# P   A   H   N
# A P L S I I G
# Y   I   R

# P    I    N
# A  L S  I G
# Y A  H R
# P    I


class Solution:
    def get_char(self, s, index):
        try:
            return s[index]
        except IndexError:
            return ""

    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows:
            return s

        if numRows == 1:
            return s

        if numRows == 2:
            return ''.join([x for index, x in enumerate(s) if index % numRows == 0]) + \
                   ''.join([x for index, x in enumerate(s) if index % numRows == 1])

        result = s[0]
        down_gap = (numRows - 1) * 2
        top_gap = 0
        use_top_gap = False
        cur_row = numRows
        cur_index = 0
        while cur_row >= 0:
            if not top_gap:
                result += self.get_char(s, cur_index + down_gap)
                cur_index += down_gap
            elif not down_gap:
                result += self.get_char(s, cur_index + top_gap)
                cur_index += top_gap
            else:
                if use_top_gap:
                    result += self.get_char(s, cur_index + top_gap)
                    cur_index += top_gap
                else:
                    result += self.get_char(s, cur_index + down_gap)
                    cur_index += down_gap

                use_top_gap = not use_top_gap

            if use_top_gap:
                limit = cur_index + top_gap
            else:
                limit = cur_index + down_gap

            if limit >= len(s):
                cur_row -= 1
                down_gap = (cur_row - 1) * 2
                top_gap = (numRows - cur_row) * 2
                use_top_gap = False
                result += self.get_char(s, numRows - cur_row)
                cur_index = numRows - cur_row

            if len(result) == len(s):
                break

        return result


if __name__ == '__main__':
    solution = Solution()
    # PAHNAPLSIIGYIR
    # print(solution.convert("PAYPALISHIRING", 3))
    # print(solution.convert("A", 3))
    # print(solution.convert("AB", 1))
    print(solution.convert("ABCD", 3))