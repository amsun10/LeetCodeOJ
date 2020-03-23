# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) >= len(b):
            b = "0" * (len(a) - len(b)) + b
        else:
            a = "0" * (len(b) - len(a)) + a

        print(a)
        print(b)

        result = ""
        index = - 1
        offset = 0

        while True:
            if "{}{}".format(a[index], b[index]) in ['10', '01']:
                if offset == 1:
                    result = '0' + result
                else:
                    result = '1' + result
            elif "{}{}".format(a[index], b[index]) in ['00']:
                if offset == 1:
                    result = '1' + result
                else:
                    result = '0' + result
                offset = 0
            else:
                if offset == 1:
                    result = "1" + result
                else:
                    result = "0" + result
                offset = 1

            if abs(index) == len(a):
                break
            else:
                index += -1

        if offset == 1:
            result = "1" + result

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.addBinary("1010", "1011"))
