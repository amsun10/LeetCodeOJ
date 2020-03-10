# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.


class Solution:
    def __init__(self):
        pass

    def intToRoman(self, num: int) -> str:
        result = ""
        bit_4 = int(num / 1000)
        bit_3 = int(num % 1000 / 100)
        bit_2 = int((num % 100) / 10)
        bit_1 = int(num % 10)

        print(bit_4, bit_3, bit_2, bit_1)

        if bit_4 != 0:
            result += "M" * bit_4

        if bit_3 != 0:
            if bit_3 in [5, 4, 9]:
                if bit_3 == 5:
                    result += "D"
                elif bit_3 == 4:
                    result += "CD"
                else:
                    result += "CM"
            else:
                if bit_3 > 5:
                    result += "D" + "C" * abs(bit_3 - 5)
                else:
                    result += "C" * bit_3

        if bit_2 != 0:
            if bit_2 in [5, 4, 9]:
                if bit_2 == 5:
                    result += "L"
                elif bit_2 == 4:
                    result += "XL"
                else:
                    result += "XC"
            else:
                if bit_2 > 5:
                    result += "L" + "X" * abs(bit_2 - 5)
                else:
                    result += "X" * bit_2

        if bit_1 != 0:
            if bit_1 in [5, 4, 9]:
                if bit_1 == 5:
                    result += "V"
                elif bit_1 == 4:
                    result += "IV"
                else:
                    result += "IX"
            else:
                if bit_1 > 5:
                    result += "V" + "I" * abs(bit_1 - 5)
                else:
                    result += "I" * bit_1

        print(result)
        return result


if __name__ == '__main__':
    solution = Solution()
    solution.intToRoman(3999)
    solution.intToRoman(999)
    solution.intToRoman(99)
    solution.intToRoman(9)
    solution.intToRoman(2999)
    solution.intToRoman(2543)
    solution.intToRoman(2743)
    solution.intToRoman(2220)
    solution.intToRoman(1994)
    solution.intToRoman(500)

