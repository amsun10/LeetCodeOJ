# https://leetcode.com/problems/reverse-words-in-a-string/


class Solution:
    def reverseWords(self, s: str) -> str:
        s_array = s.split(" ")
        reversed_array = [x for x in s_array if x]
        reversed_array.reverse()
        return " ".join(reversed_array)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords("the sky is blue"))
    print(solution.reverseWords("  hello world  "))
    print(solution.reverseWords("a good   example"))