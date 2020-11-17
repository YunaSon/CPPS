from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        c = Counter(s)
        sumNum = 0
        ood = 0
        for i in c:
            number = c[i]
            if number % 2 == 0:
                sumNum += number
            else:
                sumNum += number -1
                ood = 1
        return sumNum + ood
