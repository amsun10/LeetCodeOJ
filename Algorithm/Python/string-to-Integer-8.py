
class Solution(object):
    """
    https://leetcode.com/problems/string-to-integer-atoi/
    """
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        value = str.strip()
        is_minus = False

        if value.startswith("-"):
            value = value[1:]
            is_minus = True

        elif value.startswith("+"):
            value = value[1:]

        number = []
        for i in value:
            if i not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                break
            else:
                number.append(i)

        value = "".join(number)

        if not value:
            return 0
        else:
            value = int(value)

        if is_minus:
            if value > (2**31):
                value = 2**31
        else:
            if value > 2**31 - 1:
                value = 2**31 - 1

        if is_minus is True:
            return value * -1

        return value


if __name__ == '__main__':
    solution = Solution()

    print(solution.myAtoi("2147483648"))
    print(solution.myAtoi("-+1"))
    print(solution.myAtoi("42"))
    print(solution.myAtoi("   -42"))
    print(solution.myAtoi("4193 with words"))
    print(solution.myAtoi("words and 987"))
    print(solution.myAtoi("-91283472332"))






