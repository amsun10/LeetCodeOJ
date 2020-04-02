# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int):
        result = []
        if numRows >= 1:
            result.append([1])

        if numRows > 1:
            for i in range(1, numRows):
                pascal_array = []
                for index, item in enumerate(result[i-1]):
                    if index == 0:
                        pascal_array.append(1)
                    else:
                        pascal_array.append(result[i-1][index - 1] + result[i-1][index])
                pascal_array.append(1)
                result.append(pascal_array)
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.generate(1))
    print(solution.generate(2))
    print(solution.generate(3))
    print(solution.generate(4))
    print(solution.generate(5))