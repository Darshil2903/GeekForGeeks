# GeeksforGeeks Practice (Python)

My early data-structures and algorithms practice: solutions to **GeeksforGeeks** problems written in Python while I was learning the language. Each problem statement is pasted above its solution as a comment in [`Geeks for Geeks.py`](Geeks%20for%20Geeks.py).

## Problems covered

**Arrays and lists**
- Swap two elements in a list by position
- Swap the first and last element of a list
- Reverse a list (manually, and with `list.reverse()`)
- Count the intersection of two arrays
- Three-sum closest to a target
- Maximum element in a bitonic (increasing, then decreasing) array
- Count the triangles that can be formed from array elements
- Product array (product of all elements except self)
- Rotate an array by D positions
- Add one to a number stored as an array of digits
- First and last occurrence of X in a sorted array
- Find the element that appears once in a sorted array (all others appear twice)
- Merge K sorted arrays
- Maximize the array sum after K negations
- Burst balloons: maximum points on a line from a set of coordinates

**Math**
- Trailing zeroes in N!
- Convert a fraction to its decimal representation
- Nth natural number after removing every number containing the digit 9

**Stacks, queues and linked lists**
- Implement a queue using two stacks
- Reverse a string using a stack
- Add two numbers represented by linked lists
- Longest valid parentheses substring

**Greedy**
- Stock buy and sell: find every buy/sell day pair that makes a profit

## How to use

The solutions are commented out so the file doesn't run every exercise at once. Uncomment the block you want and run:

```bash
python "Geeks for Geeks.py"
```

## Looking back

These were written early on, so many use brute force (nested loops). Revisiting them is a good way to see progress. For example, three-sum closest drops from O(n³) to O(n²) with sorting plus two pointers, and "find the single element" can be solved in O(log n) with binary search.
