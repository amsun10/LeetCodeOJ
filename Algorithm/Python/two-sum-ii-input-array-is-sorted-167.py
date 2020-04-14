class Solution:
    def twoSum(self, numbers: [], target: int) -> []:
        for index1, number in enumerate(numbers):
            if number > target:
                break

            index2 = self.binary_search(numbers, target - number)

            if index2 != - 1 and index1 != index2:
                return [min(index1 + 1, index2 + 1), max(index1 + 1, index2 + 1)]

    def binary_search(self, numbers: [], target: int) -> int:
        start_index = 0
        end_index = len(numbers) - 1
        mid = int((start_index + end_index)/2)
        target_index = -1
        while numbers[mid] != target:
            if numbers[mid] > target:
                end_index = mid - 1
            else:
                start_index = mid + 1

            mid = int((start_index + end_index)/2)

            if end_index < start_index:
                break
        else:
            target_index = mid

        return target_index





if __name__ == '__main__':
    solution = Solution()
    print(solution.binary_search([2, 7, 11, 13, 15], 1))
    print(solution.binary_search([2, 7, 11, 13, 15], 2))
    print(solution.binary_search([2, 7, 11, 13, 15], 7))
    print(solution.binary_search([2, 7, 11, 13, 15], 11))
    print(solution.binary_search([2, 7, 11, 13, 15], 13))
    print(solution.binary_search([2, 7, 11, 13, 15], 15))
    print(solution.binary_search([2, 7, 11, 13, 15], 16))
