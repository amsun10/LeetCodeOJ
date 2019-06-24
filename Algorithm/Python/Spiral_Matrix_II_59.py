class Solution(object):
    """
    https://leetcode.com/problems/spiral-matrix-ii/
    """
    output=[]

    def changemode(self, row_index, row_mode, row_positive_mode, col_index, col_mode, col_positive_mode, n):
        if row_mode:
            if row_positive_mode:
                if col_index > n - 1:
                    return True
                else:
                    if self.output[row_index][col_index] != 0:
                        return True
            else:
                if col_index < 0:
                    return True

                else:
                    if self.output[row_index][col_index] != 0:
                        return True

        if col_mode:
            if col_positive_mode:
                if row_index > n - 1:
                    return True
                else:
                    if self.output[row_index][col_index] != 0:
                        return True
            else:
                if row_index < 0:
                    return True
                else:
                    if self.output[row_index][col_index] != 0:
                        return True

        return False

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.output = [[0 for i in range(n)] for j in range(n)]

        current_row_index = 0
        current_col_index = 0
        row_mode = True
        row_positive_mode = True
        col_mode = False
        col_positive_mode = False
        for index, i in enumerate(range(1, n**2 + 1)):
            if row_mode:
                if row_positive_mode:
                    self.output[current_row_index][current_col_index] = i
                    if current_col_index < n - 1:
                        if self.output[current_row_index][current_col_index + 1] == 0:
                            current_col_index += 1
                else:
                    self.output[current_row_index][current_col_index] = i
                    if current_col_index > 0:
                        if self.output[current_row_index][current_col_index - 1] == 0:
                            current_col_index -= 1

            if col_mode:
                if col_positive_mode:
                    self.output[current_row_index][current_col_index] = i
                    if current_row_index < n - 1:
                        if self.output[current_row_index + 1][current_col_index] == 0:
                            current_row_index += 1

                else:
                    self.output[current_row_index][current_col_index] = i
                    if current_row_index > 0:
                        if self.output[current_row_index - 1][current_col_index] == 0:
                            current_row_index -= 1

            if self.changemode(current_row_index, row_mode, row_positive_mode, current_col_index, col_mode, col_positive_mode, n) is True:
                if row_mode:
                    row_mode = False
                    col_mode = True
                    col_positive_mode = not col_positive_mode
                    if col_positive_mode:
                        current_row_index += 1
                    else:
                        current_row_index -= 1

                elif col_mode:
                    row_mode = True
                    col_mode = False
                    row_positive_mode = not row_positive_mode
                    if row_positive_mode:
                        current_col_index += 1
                    else:
                        current_col_index -= 1

        return self.output

2
if __name__ == '__main__':
    solution = Solution()
    print(solution.generateMatrix(4))