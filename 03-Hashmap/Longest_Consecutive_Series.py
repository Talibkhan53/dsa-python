# LeetCode 128 — Longest Consecutive Sequence

## Problem Statement

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.

### Example

```python
Input:  nums = [0, 3, 2, 5, 4, 6, 1, 1]
Output: 7
```

Explanation: The longest consecutive sequence is `[0, 1, 2, 3, 4, 5, 6]`, which has a length of 7.

## Approach: Hash Set

### Code

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        ns = set(nums)
        max_length = 0

        for i in ns:
            length = 0

            # Check if i is the beginning of a sequence
            if i - 1 not in ns:

                # Count consecutive numbers
                while (i + length) in ns:
                    length += 1

                max_length = max(length, max_length)

        return max_length
```

### Intuition

The main idea is to use a **Set** to efficiently check whether a number exists in the array.

A set provides average `O(1)` lookup time, which makes checking consecutive numbers much faster than searching through the original array.

**1. Convert the array into a Set**

```python
ns = set(nums)
```

This removes duplicate elements and allows efficient membership checking.

**2. Identify the beginning of a sequence**

```python
if i - 1 not in ns:
```

Before counting a sequence, we check whether the previous number exists.

If `i - 1` does not exist, `i` must be the starting point of a consecutive sequence.

For example:

```python
nums = [1, 2, 3, 4, 5]
```

Only `1` is the starting point because `0` does not exist.

**3. Count consecutive numbers**

```python
while (i + length) in ns:
    length += 1
```

Starting from `i`, we keep checking whether the next consecutive number exists.

Whenever a number exists, we increase the length.

**4. Update the maximum length**

```python
max_length = max(length, max_length)
```

Compare the current sequence length with the previously recorded maximum.

## Dry Run

Input:

```python
nums = [0, 3, 2, 5, 4, 6, 1, 1]
```

After converting into a set:

```python
ns = {0, 1, 2, 3, 4, 5, 6}
```

| Starting Number | Previous Exists? | Sequence | Length |
|---:|---|---|---:|
| 0 | No | 0, 1, 2, 3, 4, 5, 6 | 7 |
| 1 | Yes | Skipped | - |
| 2 | Yes | Skipped | - |
| 3 | Yes | Skipped | - |
| 4 | Yes | Skipped | - |
| 5 | Yes | Skipped | - |
| 6 | Yes | Skipped | - |

Final Output:

```python
7
```

## Complexity Analysis

Let `n` be the number of elements in the input array.

- **Time Complexity:** `O(n)` average — converting the array into a set takes `O(n)`. Each sequence is counted only from its starting number, so numbers are not repeatedly traversed across different sequences.
- **Auxiliary Space Complexity:** `O(n)` — the set stores the unique elements from the input array.

## Important Observations

1. **Why use a Set?** It provides average `O(1)` lookup time, making membership checks efficient.
2. **Why check `i - 1`?** It prevents counting the same sequence multiple times.
3. **Why remove duplicates?** Duplicate numbers do not affect consecutive sequence length.
4. **Why not sort the array?** Sorting would take `O(n log n)`, violating the required `O(n)` time complexity.
5. **Why use `max()`?** It keeps track of the longest sequence encountered so far.

## Summary

The Hash Set approach finds the longest consecutive sequence in average `O(n)` time by identifying sequence starting points and counting consecutive numbers.

**Use:** This technique is useful in problems involving fast membership checking, duplicate removal, consecutive elements, and sequence detection.
