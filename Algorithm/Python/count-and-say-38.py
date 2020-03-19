# https://leetcode.com/problems/count-and-say/
# TODO:


class Solution:
    base_term = {
        1: '1',
        2: '11',
        3: '21',
        4: '1211',
        5: '111221',

    }

    def __init__(self):
        for i in range(6, 31):
            target = self.base_term[i-1]
            result = ""
            index = 1
            target_len = len(target)
            while target:
                if index < target_len:
                    if target[index] == target[index - 1]:
                        index += 1
                    else:
                        result += "{}{}".format(index, target[index-1])
                        target = target[index:]
                        target_len = len(target)
                        index = 1

                else:
                    result += "{}{}".format(index, target[index-1])
                    break
            self.base_term[i] = result

            print("{}: {}".format(i, result))

    def countAndSay(self, n: int) -> str:
        return self.base_term[n]


if __name__ == '__main__':
    solution = Solution()
