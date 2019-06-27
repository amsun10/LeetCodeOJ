class Solution(object):
    """
    https://leetcode.com/problems/distinct-subsequences/
    """
    counter = {}
    def find_all_index(self, s, t):
        index_list = []
        target = s
        index = 0
        while target.rfind(t, index) != -1:
            index = target.find(t, index)
            index_list.append(index)
            index = index + 1
        return index_list

    def combine_list(self, a, b):
        combined = []
        couter_temp = {}

        for j in b:
            i = 0
            sum = 0
            flag = False
            while j > a[i]:
                flag = True
                if self.counter.get(a[i]):
                    sum += self.counter.get(a[i])
                else:
                    sum += 1
                i += 1
                # combined.append(j)
                if j not in combined:
                    combined.append(j)
                if i == len(a):
                    break
            if flag is True:
                couter_temp[j] = sum

        remove_list = []
        for item in couter_temp.keys():
            if item not in combined:
                remove_list.append(item)

        for item in remove_list:
            self.counter.pop(item)

        self.counter = couter_temp

        print("Combined: {}: {}".format(combined, self.counter))

        return combined

    def numDistinct(self, s="", t=""):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if s == t:
            return 1

        if len(s) < len(t):
            return 0

        index_list = []
        j = 0

        while s:
            index_j = self.find_all_index(s, t[j])
            if not index_j:
                return 0

            index_list.append(index_j)
            j += 1
            if j == len(t):
                break

        for item in index_list:
            print(item)

        if not index_list:
            return 0
        if len(index_list) == 1:
            return len(index_list[0])

        while len(index_list) > 1:
            index_list[1] = self.combine_list(index_list[0], index_list[1])
            if not index_list[1]:
                return 0
            index_list.pop(0)
        # print(len(index_list[0]))
        count = sum([self.counter[i] for i in index_list[0]])
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.numDistinct("adbdadeecadeadeccaeaabdabdbcdabddddabcaaadbabaaedeeddeaeebcdeabcaaaeeaeeabcddcebddebeebedaecccbdcbcedbdaeaedcdebeecdaaedaacadbdccabddaddacdddc"
                               , "bcddceeeebecbc"))
    print(solution.numDistinct("rabbbit"
                               , "rabbit"))
    print(solution.numDistinct("babgbag"
                               , "bag"))
    print(solution.numDistinct("aaaaaaaaaaaaa", "aa"))
