# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string, find the length of the longest substring without repeating characters.


class Solution(object):
    def get_max_not_repeat_len(self, s):
        temp_str = s[0]
        max_length = 1
        i = 1
        while i < len(s):
            if s[i] not in temp_str:
                temp_str += s[i]
                max_length += 1
                i += 1
            else:
                break

        return max_length

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        max_length = 1
        s_len = len(s)

        for i in range(s_len):
            temp_length = self.get_max_not_repeat_len(s[i:])
            if max_length < temp_length:
                max_length = temp_length

        return max_length


if __name__ == '__main__':

    solution = Solution()

    print(solution.lengthOfLongestSubstring("pwwkew"))



