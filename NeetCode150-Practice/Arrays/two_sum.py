class Solution:
    # Brute force approach to solve the two-sum problem
    # This method iterates through the list twice, comparing every pair of numbers
    # It checks if the sum of two distinct numbers equals the target value.
    # Time complexity: O(n^2) due to the nested loops
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range (len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]
        return []