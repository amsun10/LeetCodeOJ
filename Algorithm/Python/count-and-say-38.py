# https://leetcode.com/problems/count-and-say/
# TODO:

class Solution:
    base_term : {
        1 : '1',
        2 : '11',
        3 : '21',
        4 : '1211',
        5 : '111221',
    }

    def __init__(self):
        for i in range(6, 31):
            target = "" #self.base_term[i-1]
            result = ""
            while target:
                if target.startswith("11"):
                    result += "21"
                    target = target[2:]
                    continue

                if target.startswith("1"):
                    result += '1'
                    target = target[1:]
                    continue




    def countAndSay(self, n: int) -> str:
