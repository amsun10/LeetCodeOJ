class Solution:
    def getRow(self, rowIndex: int):
        result = []
        if rowIndex >= 0:
            result = [1]

        for i in range(0, rowIndex):
            pascal_array = []
            for index, item in enumerate(result):
                if index == 0:
                    pascal_array.append(1)
                else:
                    pascal_array.append(result[index - 1] + result[index])
            pascal_array.append(1)
            result = pascal_array

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.getRow(3))
    print(solution.getRow(1))
    print(solution.getRow(2))
    print(solution.getRow(3))
    print(solution.getRow(4))
    print(solution.getRow(33))