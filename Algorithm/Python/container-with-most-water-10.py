# https://leetcode.com/problems/container-with-most-water/

# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.
#
# Example:
#
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49


#TODO: Need A Solution

class Solution:
    def maxArea(self, height: list) -> int:
        max_height = max(height)
        min_height = min(height)

        total_volume = min_height * len(height)
        cur_height = min_height

        height = [x - min_height for x in height]

        while cur_height <= max_height:
            temp_volume = self.calculate_volume(cur_height, total_volume, height)
            if total_volume > temp_volume:
                break
            else:
                total_volume = temp_volume
                cur_height += 1

        return total_volume

    def calculate_volume(self, cur_height, cur_volume, height):
        max_height = max(height)
        min_height = min(height)
        cur_volume += min_height * len(height)


        return cur_volume
        pass
