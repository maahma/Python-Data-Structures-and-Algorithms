class Solution:
    # Brute-force approach to check for duplicates in a list
    # Time complexity: O(n^2) due to nested loops
    def hasDuplicate1(self, nums: List[int]) -> bool:

        # Iterate over all pairs of indices in the list
        for i in range(len(nums)):
            for j in range(len(nums)):
                # Check if elements at indices i and j are the same but indices are different
                if nums[i] == nums[j] and i != j:
                    return True # Duplicate found
        return False  # No duplicate found
    
    # Optimized approach uses a sorted list
    # Time complexity: O(n log n) due to the sorting operation
    def hasDuplicate2(self, nums: List[int]) -> bool:
        
        # Sort the list in-place
        nums.sort()  

        # Compare each element with its previous element
        for i in range(1, len(nums)):  # Start from index 1 to avoid out-of-range errors
            if nums[i] == nums[i-1]:   # If consecutive elements are the same, a duplicate exists
                return True
        return False                    # No duplicates found
    


    # Most efficient approach using a hash set since it does not allow duplicates to be stored
    # Time complexity: O(n), as set operations (add and lookup) are O(1) on average
    def hasDuplicate2(self, nums: List[int]) -> bool:
        
        # Initialize an empty set to store unique elements
        hash_set  = set()

        # Iterate through the list
        for num in nums: 
            # Check if the current number is already in the set
            if num in hash_set:
                return True      # Duplicate found
            hash_set.add(num)    # Add the number to the set if it doesn't already exist in the set
        
        return False