__author__ = 'xizhang'
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum = num
        while sum >= 10:
            sum = self.get_sum(sum)
        return sum

    def get_sum(self, num):
        sum = 0
        while num >= 10:
            sum += num % 10
            num = int(num/10)
        sum += num
        return sum

if __name__ == '__main__':
    solu = Solution()
    print solu.addDigits(38)
    print solu.addDigits(10)