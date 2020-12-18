'''
=========================================================
169. Majority Element
링크: https://leetcode.com/problems/majority-element/
level: easy
=========================================================
'''

# sorted 함수 - O(nlog(n)), fail
class Solution:
    def majorityElement(self, nums) -> int:
        answer = sorted(nums, key=nums.count, reverse=True)
        return answer[0]


# 2중 for문 - O(n^2)
class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num

# Hashmap O(n), O(n) - pass
import collections
class Solution2:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


if __name__ == '__main__':
    nums = [3,2,3]
    solution = Solution()
    print(solution.majorityElement(nums))

    solution = Solution2()
    print(solution.majorityElement(nums))

