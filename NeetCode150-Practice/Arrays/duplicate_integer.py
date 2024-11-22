class Solution:
    # brute force approach
    # time complexity: O(n^2)
    def hasDuplicate1(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i != j:
                    return True
        return 
    
    # better approach uses a sorted list
    # compares a number in the list with the number before it
    # this way it avoids out of index out of range error, and checks for duplicates in O(n logn) time
    def hasDuplicate2(self, nums: List[int]) -> bool:
        
        nums.sort()  # sorts the original list and doesn't assign it to a new variable, saving space

        for i in range(1, len(nums)):  # starts from index 1
            if nums[i] == nums[i-1]:
                return True
        return False
    


    # the best approach uses a hash list
    # a hash set does not allow duplicates 
    # the function iterates over the numbers in the list and checks if the set contains the number
    # if the number exists in the set, the function returns true, otherwise it returns false
    # time complexity is O(n)
    def hasDuplicate2(self, nums: List[int]) -> bool:
        
        hash_list = set()  # makes a hashlist

        for num in nums: 
            if num in hash_list:
                return True
            hash_list.add(num)
        return False