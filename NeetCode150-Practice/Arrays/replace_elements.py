class Solution(object):
    # Brute force approach to replace each element in the array with the greatest element to its right
    # Time Complexity: O(n^2)
    def replaceElements1(self, arr):

        # Initialize a new array to store the results
        new_arr = []

        # Iterate through each element in the input array
        for i in range(len(arr)):        # Outer loop: O(n)

            # Create a slice of the array starting from the next element to the end
            sliced = arr[i+1:len(arr)]  # Slicing: O(k), where k is the size of the slice.
                                        # As i increases, the size of the slice decreases, so O(k) = O(n) + O(n-1) + O(n-2) + ... + O(n(n+1)/2) = O(n^2)
                                        # So slicing : O(n^2)
            
            # Find the maximum value in the sliced portion
            if sliced:
                max_num = max(sliced)   # max() function operates on the slice: O(k). 
                                        # # Over all iterations, this adds up to O(n^2), same as slicing
            else :
                # If the slice is empty (i.e., last element), set the value to -1
                max_num = -1
            
            # Append the maximum value (or -1 for the last element) to the result array
            new_arr.append(max_num)      # Append operation: O(1) per call, O(n) total for n iterations
        
        # Return the final transformed array
        return new_arr                   # Overall time complexity = O(n + n + n^2 + n^2) = O(n^2)
    
    # Better approach is to start traversing from the end of the list
    # Time Complexity: O(n), as we traverse the array once from right to left.
    def replaceElements2(self, arr):
        
        # Initialize max_val to -1, as the last element should always be replaced with -1.
        max_val = -1
        
        # Traverse the array from right to left (starting from the last element).
        for i in range(len(arr) - 1, -1, -1):  # Reverse traversal: O(n)
            
            # Store the current max_val (this will replace the current element).
            new_val = max_val
            
            # Update max_val to the maximum of the current element and max_val.
            max_val = max(max_val, arr[i])
            
            # Replace the current element with the stored max_val (greatest element to its right).
            arr[i] = new_val
        
        # Return the modified array.
        return arr

