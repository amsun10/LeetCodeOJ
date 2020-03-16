# https://leetcode.com/problems/valid-parentheses/


class Solution:
    parent_map = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

    def isValid(self, s: str) -> bool:
        if not s:
            return True

        temp = ""
        while s:
            if s[0] in ['{', '[', '(']:
                temp += s[0]
            else:
                if temp:
                    if self.parent_map[temp[-1]] != s[0]:
                        return False
                    else:
                        temp = temp[:-1]
                else:
                    return False
            s = s[1:]

        if not temp:
            return True

        return False
