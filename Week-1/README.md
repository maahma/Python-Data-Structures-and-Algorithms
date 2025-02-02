Some notes :
### Two Sum
    - The brute-force approach iterates through the list, checking all pairs to find the target sum, resulting in a time complexity of $O(n^2)$
    - The goal is to find an optimal solution with a time complexity of $O(n)$

    - Clarifying questions to ask the interviewer: 
        1. What does the input look like (e.g., sorted/unsorted, list size constraints)?
        2. Do I need to handle null or invalid inputs?
        3. Can the sum cause an integer overflow?
        4. What is the expected runtime complexity for the solution?
    
    - To find a solution: 
        - Find insights from the problem statement
        - Ask interviewer for a hint
        - Find suitable algorithms based on the desired runtime complexity:
            - An improvement from $O(n^2)$ would be $O(n log n)$ and usually $O(n log n)$ solutions involve sorting an array and scaning through it to find the answer. 
            - If the array is already sorted, we can use binary search($O(log n)$) on n items, resulting in $O(n log n)$ run time
            - A further optimization would be a linear-time solution $O(n)$, achievable using the two-pointer approach if the list is already sorted ([Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/))
            - If the list is unsorted, a hashmap can be used instead
    
    - [Using a hashmap](https://www.youtube.com/watch?v=luicuNOBTAI) :
        1. Iterate through the list of numbers
        2. Calculate the difference between the target and the current number
        3. Check if the difference exists in the hashmap:
            - If it does, return the stored index and the current index
            - If it doesn’t, store the current number as the key and its index as the value
    
    - Draw the solution to visualize it better

- If a list is already sorted, think about Binary Search or Two Pointers