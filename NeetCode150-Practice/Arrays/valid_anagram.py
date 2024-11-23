class Solution:
    # Brute-force approach to check if two strings are anagrams
    # Time complexity: O(n log n + m log m), where nlogn is time complexity for sorting string s
    def isAnagram1(self, s: str, t: str) -> bool:

        # Step 1: Check if the lengths of the two strings are different
        # If the lengths differ, they cannot be anagrams
        if len(s) != len(t):   # O(1)
            return False
        
        # Step 2: Sort both strings and compare their sorted versions
        # Convert the strings into lists, sort them, and check for equality.
        # Sorting ensures that characters appear in the same order in both strings, 
        # making it easy to verify if they contain the same characters in the same frequency.
        # Sorting time complexity: O(n log n) for string s and O(m log m) for string t
        if list(s).sort() == list(t).sort():  
            return True

        # If the sorted strings do not match, they are not anagrams.
        return False


    # Better approach uses hashmaps
    # Time complexity : O(n+m) where n = length of string s, m = length of string t
    def isAnagram1(self, s: str, t: str) -> bool:

        # Step 1: Check if the lengths of the two strings are different
        # If the lengths differ, they cannot be anagrams
        if len(s) != len(t):   # Time complexity: O(1) for comparison
            return False
        
        # Step 2: Initialize two hashmaps to store character frequencies
        hashmap_S, hashmap_T = {}, {}

        # Step 3: Populate the hashmaps
        # Hashmaps store key value pairs
        # For each character in the strings, update its frequency in the corresponding hashmap
        # Key: character; Value: frequency in the string
        for i in range(len(s)): # time complexity = O(n)
            hashmap_S[s[i]] = 1 + hashmap_S.get(s[i], 0)   # Update frequency for 's[i]', time complexity = O(n) to construct the hashmap
            hashmap_T[t[i]] = 1 + hashmap_T.get(t[i], 0)   # Update frequency for 't[i]', time complexity = O(m) to construct the hashmap

        # Example:
        # For s = "racecar" and t = "carrace":
        # After the loop:
        # hashmap_S = {'r': 2, 'a': 2, 'c': 2, 'e': 1}
        # hashmap_T = {'c': 2, 'a': 2, 'r': 2, 'e': 1}

        # Step 4: Compare the two hashmaps
        # If they are identical, the strings are anagrams
        return hashmap_S == hashmap_T  # Time Complexity: O(1) for comparison, depends on how many characters there are in the hashmap