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


# P   A   H   N
# A P L S I I G
# Y   I   R

#TODO NEED A SOLUTION
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        if numRows == 2:
            return ''.join([x for index, x in enumerate(s) if index % numRows == 0]) + \
                   ''.join([x for index, x in enumerate(s) if index % numRows == 1])

        result = s[0]
        down_gap = numRows
        top_gap = 0
        use_top_gap = False
        cur_row = numRows
        cur_index = 0
        while cur_row >= 0:
            if not top_gap:
                result += s[cur_index + numRows + 1]
                cur_index += numRows + 1
            elif not down_gap != 1:
                result += s[cur_index + numRows + 1]
                cur_index += numRows + 1
            else:
                if use_top_gap:
                    result += s[cur_index + top_gap + 1]
                    cur_index += top_gap + 1
                else:
                    result += s[cur_index + down_gap]
                    cur_index += down_gap

                use_top_gap = not use_top_gap

            if cur_index + down_gap + 1 > len(s):
                cur_row -= 1
                down_gap -= 1
                top_gap += 1
                use_top_gap = False
                result += s[numRows-cur_row]
                cur_index = numRows - cur_row






if __name__ == '__main__':
    solution = Solution()
    # PAHNAPLSIIGYIR
    print(solution.convert("PAYPALISHIRING", 3))