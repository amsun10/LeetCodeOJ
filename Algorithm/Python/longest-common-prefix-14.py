# https://leetcode.com/problems/longest-common-prefix/


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs or not all(strs):
            return ""

        index = 0
        target = strs[0][index]
        while True:
            try:
                iter_result = map(lambda x: x[index] == target, strs)
                if all(iter_result):
                    index += 1
                    target = strs[0][index]
                else:
                    break
            except IndexError:
                break

        return strs[0][:index]


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
    print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
    print(solution.longestCommonPrefix(["", "racecar", "car"]))
    print(solution.longestCommonPrefix([]))


