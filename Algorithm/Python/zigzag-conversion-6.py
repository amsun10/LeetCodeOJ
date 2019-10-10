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
# P    I    N
# A  L S  I G
# Y A  H R
# P    I
#TODO NEED A SOLUTION


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        if numRows == 2:
            return ''.join([x for index, x in enumerate(s) if index % 2 == 0]) + \
                   ''.join([x for index, x in enumerate(s) if index % 1 == 0])
        str_array = []
        for i in range(numRows):
            str_array.append([""] * len(s))

        cur_col = 0
        index_row = 1
        middle_row = 0
        middle_row_limit = numRows - 2
        for index, char in enumerate(s):
            str_array[cur_col + index % numRows][index % numRows].append(char)
            curcol = int(index/numRows)
            index_row += 1
            if index % numRows == 0:
                index = 1

        return str_array[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.convert("PAYPALISHIRING", 2))




