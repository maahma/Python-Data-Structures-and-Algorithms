# https://leetcode.com/problems/two-sum/description/

from collections import defaultdict
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        diff_dict = defaultdict(list)
        diff = 0

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in diff_dict:
                return [diff_dict[diff], i]

            diff_dict[nums[i]] = i
    
        return []