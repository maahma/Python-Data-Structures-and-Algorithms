# Python DS&A
This is my study plan to practice data structures and algorithms using Python for coding interviews

### Table of Contents
- **[🦋 Study Resources](#-study-resources)<br>**
- **[🐝 Study Progress](#-study-progress)<br>**
- **[🍓 Learning Materials](#-learning-materials)<br>**
  - **[Week 1](#week-1)<br>**
  <!-- - **[Week 2](#week-2)<br>**
  - **[Week 3](#week-3)<br>** -->
- **[✨ Practice Questions ✨](#-practice-questions-)<br>**
  - **[Week 1 List](#week-1-list)<br>**

### 🦋 Resources
I used the following resources to form my study plan:
- [Coding Interview Univeristy by John Washam](https://github.com/jwasham/coding-interview-university)
- [Study Plan for the week by Ramiro Richmand](https://github.com/ramirorichmand/RR10_MyStudyPlan/tree/main)
- [NeetCode 150 Practice Questions](https://neetcode.io/practice?tab=neetcode150)
- [NeetCode 150 Roadmap](https://neetcode.io/roadmap)
- [Elements of Programming Interviews in Python by Adnan Aziz, Tsung-Hsien Lee, Amit Prakash](https://elementsofprogramminginterviews.com)

## 🐝 Study Progress
| Week | Dates | Leetcode Solved (Easy/Med/Hard) | Topics Covered | Mock Interviews | Notes | Hours spent | 
| ---- | ----- | ------------------------------- | -------------- | --------------- | ----- | ----------- |
| 1    | 03/02/25 - 09/02/25 | - | - | - | - | - |
| 2    | 10/02/25 - 16/02/25 | - | - | - | - | - |
| 3    | 17/02/25 - 23/02/25 | - | - | - | - | - |
| 4    | 24/02/25 - 02/03/25 | - | - | - | - | - |


## 🍓 Learning Materials
I study the learning materials on the weekend to prepare for solving problems during the weekdays
### Week 1
- ### Arrays
    - [x] About Arrays:
      - [Arrays (video)](https://www.coursera.org/lecture/data-structures/arrays-OsBSF)
      - [Dynamic Arrays (video)](https://www.coursera.org/lecture/data-structures/dynamic-arrays-EwbnV)
    - [ ] Implement a vector (mutable array with automatic resizing):
        - [ ] Practice coding using arrays and pointers, and pointer math to jump to an index instead of using indexing.
        - [ ] New raw data array with allocated memory
            - can allocate int array under the hood, just not use its features
            - start with 16, or if the starting number is greater, use power of 2 - 16, 32, 64, 128
        - [ ] size() - number of items
        - [ ] capacity() - number of items it can hold
        - [ ] is_empty()
        - [ ] at(index) - returns the item at a given index, blows up if index out of bounds
        - [ ] push(item)
        - [ ] insert(index, item) - inserts item at index, shifts that index's value and trailing elements to the right
        - [ ] prepend(item) - can use insert above at index 0
        - [ ] pop() - remove from end, return value
        - [ ] delete(index) - delete item at index, shifting all trailing elements left
        - [ ] remove(item) - looks for value and removes index holding it (even if in multiple places)
        - [ ] find(item) - looks for value and returns first index with that value, -1 if not found
        - [ ] resize(new_capacity) // private function
            - when you reach capacity, resize to double the size
            - when popping an item, if the size is 1/4 of capacity, resize to half
    - [ ] Time
        - O(1) to add/remove at end (amortized for allocations for more space), index, or update
        - O(n) to insert/remove elsewhere
    - [ ] Space
        - contiguous in memory, so proximity helps performance
        - space needed = (array capacity, which is >= n) * size of item, but even if 2n, still O(n)

- ### Linked Lists
    - [x] Description:
        - [x] [Singly Linked Lists (video)](https://www.coursera.org/lecture/data-structures/singly-linked-lists-kHhgK)
        - [ ] [Doubly-linked List](https://www.coursera.org/lecture/data-structures/doubly-linked-lists-jpGKD)
    - [ ] Linked List vs Arrays:
        - [Core Linked Lists Vs Arrays (video)](https://www.coursera.org/lecture/data-structures-optimizing-performance/core-linked-lists-vs-arrays-rjBs9)
        - [In The Real World Linked Lists Vs Arrays (video)](https://www.coursera.org/lecture/data-structures-optimizing-performance/in-the-real-world-lists-vs-arrays-QUaUd)
    - [ ] [Why you should avoid linked lists (video)](https://www.youtube.com/watch?v=YQs6IC-vgmo)
    - [ ] Implement (I did with tail pointer & without):
        - [ ] size() - returns the number of data elements in the list
        - [ ] empty() - bool returns true if empty
        - [ ] value_at(index) - returns the value of the nth item (starting at 0 for first)
        - [ ] push_front(value) - adds an item to the front of the list
        - [ ] pop_front() - remove the front item and return its value
        - [ ] push_back(value) - adds an item at the end
        - [ ] pop_back() - removes end item and returns its value
        - [ ] front() - get the value of the front item
        - [ ] back() - get the value of the end item
        - [ ] insert(index, value) - insert value at index, so the current item at that index is pointed to by the new item at the index
        - [ ] erase(index) - removes node at given index
        - [ ] value_n_from_end(n) - returns the value of the node at the nth position from the end of the list
        - [ ] reverse() - reverses the list
        - [ ] remove_value(value) - removes the first item in the list with this value

- ### Stack
    - [ ] [Stacks (video)](https://www.coursera.org/lecture/data-structures/stacks-UdKzQ)
    - [ ] [Another video](https://www.youtube.com/watch?v=stD5O9YnM04&list=PLUITAQK78D8MpbhXccWtEoDbGpv77P8XX&index=4)

- ### Hashing
    - [x] [Hasmaps (video)](https://www.youtube.com/watch?v=RcZsTI5h0kg)
    - [ ] [Hash Functions, Sets and Maps(video)](https://www.youtube.com/watch?v=iZyxNEBpqFY)

- ### Two Pointers
    - [ ] [Two Pointers (video)](https://www.youtube.com/watch?v=syTs9_w-pwA)
    - [ ] [Another Two Pointers video](https://www.youtube.com/watch?v=-gjxg6Pln50)

<!--- ### Week 2
#### take resources from coding university and add here ------------------------------------
#### Binary Search
#### Sliding Window
#### Recursion
#### Binary Tree

### Week 3
#### Dynamic Programming
#### Graph
#### Heap
#### Tries 

### Week 4
#### Intervals
#### Greedy Algorithms
#### Bit Manipulation
#### Advanced Graphs--->

## ✨ Practice Questions ✨
### Week 1 List
| #  | Problem | Difficulty | Time to Solve | Topic | Status |
|----|------------- | ---------- | -------------- | ----- | ------ |
| 1  | [Two Sum](https://leetcode.com/problems/two-sum/) | ![Easy](https://img.shields.io/badge/-Easy-success?style=flat-square) | 10 mins | Array | ❌ |
| 2  | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | ![Easy](https://img.shields.io/badge/-Easy-success?style=flat-square) | 10 mins | Stack | ❌ |
| 3  | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | ![Easy](https://img.shields.io/badge/-Easy-success?style=flat-square) | 10 mins | Linked List | ❌ |
| 4  | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | ![Easy](https://img.shields.io/badge/-Easy-success?style=flat-square) | 10 mins | Array | ❌ |
| 5  | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | ![Easy](https://img.shields.io/badge/-Easy-success?style=flat-square) | 10 mins | String | ❌ |
| 6  | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | ![Easy](https://img.shields.io/badge/-Easy-success?style=flat-square) | 10 mins | String | ❌ |
| 7  | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | ![Easy](https://img.shields.io/badge/-Easy-success?style=flat-square) | 10 mins | Linked List | ❌ |
| 8  | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks) | ![Easy](https://img.shields.io/badge/-Easy-success?style=flat-square) | 10 mins | Stack | ❌ |
| 9  | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | ![Easy](https://img.shields.io/badge/-Easy-success?style=flat-square) | 10 mins | Linked List | ❌ |
| 10 | [Longest Palindrome](https://leetcode.com/problems/longest-palindrome/) | ![Easy](https://img.shields.io/badge/-Easy-success?style=flat-square) | 10 mins | String | ❌ |
| 11 | [Contains Duplicates](https://leetcode.com/problems/contains-duplicate/) | ![Easy](https://img.shields.io/badge/-Easy-success?style=flat-square) | 10 mins | Array  | ❌ |
| 12 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | ![Easy](https://img.shields.io/badge/-Easy-success?style=flat-square) | 10 mins | Array  | ❌ |
| 13 | [Implement Stacks using Queues](https://leetcode.com/problems/implement-stack-using-queues/) | ![Easy](https://img.shields.io/badge/-Easy-success?style=flat-square) | 10 mins | Stacks  | ❌ |
| 14 | [Baseball Game](https://leetcode.com/problems/baseball-game/) | ![Easy](https://img.shields.io/badge/-Easy-success?style=flat-square) | 25 mins | Stacks  | ❌ |
| 15 | [Insert Interval](https://leetcode.com/problems/insert-interval/description/) | ![Medium](https://img.shields.io/badge/-Medium-yellow?style=flat-square) | 25 mins | Array | ❌ |
| 16 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/) | ![Medium](https://img.shields.io/badge/-Medium-yellow?style=flat-square) | 25 mins | String | ❌ |
| 17 | [3Sum](https://leetcode.com/problems/3sum/) | ![Medium](https://img.shields.io/badge/-Medium-yellow?style=flat-square) | 25 mins | Array | ❌ |
| 18 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/) | ![Medium](https://img.shields.io/badge/-Medium-yellow?style=flat-square) | 25 mins | Stack | ❌ |
| 19 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/) | ![Medium](https://img.shields.io/badge/-Medium-yellow?style=flat-square) | 25 mins | Array | ❌ |
| 20 | [Min Stack](https://leetcode.com/problems/min-stack/description/) | ![Medium](https://img.shields.io/badge/-Medium-yellow?style=flat-square) | 25 mins | Stack | ❌ |
| 21 | [Combination Sum](https://leetcode.com/problems/combination-sum/) | ![Medium](https://img.shields.io/badge/-Medium-yellow?style=flat-square) | 25 mins | Array | ❌ |
| 22 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | ![Medium](https://img.shields.io/badge/-Medium-yellow?style=flat-square) | 25 mins | Array | ❌ |
| 23 | [Reorder List](https://leetcode.com/problems/reorder-list/) | ![Medium](https://img.shields.io/badge/-Medium-yellow?style=flat-square) | 45 mins | Linked List | ❌ |
| 24 | [Remove Nth Node From End of List ](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | ![Medium](https://img.shields.io/badge/-Medium-yellow?style=flat-square) | 45 mins | Linked List | ❌ |
| 25 | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | ![Medium](https://img.shields.io/badge/-Medium-yellow?style=flat-square) | 25 mins | String | ❌ |
| 26 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | ![Medium](https://img.shields.io/badge/-Medium-yellow?style=flat-square) | 45 mins | Linked List | ❌ |
| 27 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | ![Medium](https://img.shields.io/badge/-Medium-yellow?style=flat-square) | 25 mins | Stack | ❌ |
| 28 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | ![Hard](https://img.shields.io/badge/-Hard-red?style=flat-square) | 45 mins | String | ❌ |
| 29 | [Merge K sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | ![Hard](https://img.shields.io/badge/-Hard-red?style=flat-square) | 45 mins | Linked List | ❌ |
| 30 | [Reverse Nodes In K Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | ![Hard](https://img.shields.io/badge/-Hard-red?style=flat-square) | 45 mins | Linked List | ❌ |
| 31 | [Maximum Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack/) | ![Hard](https://img.shields.io/badge/-Hard-red?style=flat-square) | 45 mins | Stack | ❌ |
| 32 | [Largest Rectangle In Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | ![Hard](https://img.shields.io/badge/-Hard-red?style=flat-square) | 45 mins | Stack | ❌ |
| 33 | [First Missing Positive](https://leetcode.com/problems/first-missing-positive/) | ![Hard](https://img.shields.io/badge/-Hard-red?style=flat-square) | 45 mins | Array | ❌ |


#### Total for Week 1
| Topics | Easy | Medium | Hard |
| ------ | ---- | ------ | ---- |
| Arrays | 4 | 5 | 1 |
| Strings | 3 | 2 | 1 |
| Linked List | 3 | 3 | 2 |
| Stacks | 4 | 3 | 2 |


