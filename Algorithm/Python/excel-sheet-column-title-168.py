class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ""
        base = 64
        while n > 26:
            a = n % 26
            if a == 0:
                result = 'Z' + result
                n = n - 26
            else:
                result = chr(base+a) + result
                n = n - a
            n = int(n / 26)
        else:
            result = chr(base+n) + result
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.convertToTitle(1))
    print(solution.convertToTitle(28))
    print(solution.convertToTitle(52))
    print(solution.convertToTitle(701))


