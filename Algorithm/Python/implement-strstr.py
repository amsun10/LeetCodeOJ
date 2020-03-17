# https://leetcode.com/problems/implement-strstr/
# TODO: give a solution


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack:
            return -1

        for index, char in enumerate(haystack):
            if needle[0] == char:
                for sub_index, i in enumerate(needle[1:]):
                    if index + sub_index + 1 < len(haystack):
                        if i != haystack[index + sub_index + 1]:
                            break
                    else:
                        return -1
                else:
                    return index

        return -1

if __name__ == '__main__':
    solution = Solution()
    print(solution.strStr("aaaa", "aaaaa"))
    print(solution.strStr("Hello", "bc"))
