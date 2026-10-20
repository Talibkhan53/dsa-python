# LeetCode 53: Maximum Subarray

## Problem
Given an integer array `nums`, find the subarray with the largest sum and return its sum.

A subarray is a contiguous, non-empty sequence of elements.

## Approach: Kadane's Algorithm

The idea is to decide whether to extend the current subarray or start a new one at each element.

- `current_sum`: The maximum sum of a subarray ending at the current position.
- `max_sum`: The maximum subarray sum found so far.

For each element, calculate:

`current_sum = max(nums[i], current_sum + nums[i])`

Then update the overall maximum.

## Python Solution

```python
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
```

## Example

**Input:**
```python
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

**Output:**
```python
6
```

Explanation:

The subarray `[4, -1, 2, 1]` has the maximum sum:

`4 + (-1) + 2 + 1 = 6`

## Complexity Analysis

- **Time Complexity:** `O(n)` — Each array element is processed once.
- **Space Complexity:** `O(1)` — Only two variables are used, regardless of the input size.

## Key Takeaway

Kadane's Algorithm efficiently solves the Maximum Subarray problem without generating every possible subarray. Initializing both sums with `nums[0]` also allows the algorithm to handle arrays containing only negative numbers.

**Topics:** Arrays, Dynamic Programming, Kadane's Algorithm
