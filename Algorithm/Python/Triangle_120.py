class Solution(object):
    """
    https://leetcode.com/problems/triangle/
    """
    def minimumTotal(self, triangle=[]):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        while len(triangle) != 1:
            last_column_index = len(triangle) - 1
            for index, item in enumerate(triangle[last_column_index - 1]):
                triangle[last_column_index - 1][index] = min(item + triangle[last_column_index][index],
                                                             item + triangle[last_column_index][index+1])
            triangle.pop(last_column_index)

        return triangle[0][0]




