class Solution:
    # Brute force approach to solve the two-sum problem
    # This method iterates through the list twice, comparing every pair of numbers
    # It checks if the sum of two distinct numbers equals the target value.
    # Time complexity: O(n^2) due to the nested loops
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range (len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]
        return []
    
    # Better approach is to use sorting 
    # Time Complexity = O(n logn) because of sorting 
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        # Create a 2D array to store each number along with its original index
        new_arr = []
        for i, num in enumerate(nums):
            new_arr = [num, i]
        
        # Sort the 2D array by the numbers (first element of each pair)
        # Sorting ensures that we can use a two-pointer approach
        new_arr.sort()

        # Initialize two pointers
        i = 0                # Start pointer, beginning of the array
        j = len(nums) - 1    # End pointer, end of the array

        while i < j:
            # Calculate the sum of the numbers at the two pointers
            sum_nums = new_arr[i][0] + new_arr[j][0]

            # If the sum matches the target, return their original indices
            if sum_nums == target:
                min_index = min(new_arr[i][1], new_arr[j][1])  # Smaller index first
                max_index = max(new_arr[i][1], new_arr[j][1])  # Larger index second
                return [min_index, max_index]
            
            # If the sum is less than the target, move the start pointer up to increase the sum
            elif sum_nums < target:
                i += 1
            
            # If the sum is greater than the target, move the end pointer down to decrease the sum
            else:
                j -= 1

        # If no solution is found, return an empty list
        return []