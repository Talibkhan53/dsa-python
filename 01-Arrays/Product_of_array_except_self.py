# LeetCode 238 — Product of Array Except Self

## Problem Statement

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all elements of `nums` except `nums[i]`.

You must solve the problem without using division and in `O(n)` time complexity.

### Example

```python
Input:  nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
```

## Approach: Prefix and Postfix Products

### Code

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        result = [1] * len(nums)

        prefixV = 1
        postfixV = 1

        # Calculate prefix products
        for i in range(len(nums)):
            prefixV *= nums[i]
            prefix[i] = prefixV

        # Calculate postfix products
        for i in reversed(range(len(nums))):
            postfixV *= nums[i]
            postfix[i] = postfixV

        # Calculate product except self
        for i in range(len(nums)):
            pre = prefix[i - 1] if i > 0 else 1
            post = postfix[i + 1] if i < len(nums) - 1 else 1

            result[i] = pre * post

        return result
```

### Intuition

The main idea is to calculate the product of all elements before and after the current index.

We use two arrays:

**1. Prefix Array**

Stores the product of all elements from the beginning up to the current index.

For:

```python
nums = [1, 2, 3, 4]
prefix = [1, 2, 6, 24]
```

**2. Postfix Array**

Stores the product of all elements from the end up to the current index.

```python
postfix = [24, 24, 12, 4]
```

**3. Result Array**

For every index:

```python
result[i] = prefix[i - 1] * postfix[i + 1]
```

In simple words:

- Prefix gives the product of elements on the left.
- Postfix gives the product of elements on the right.
- Multiplying both gives the product of everything except the current element.

We use `1` when there is no left or right element because multiplying by 1 does not change the result.

### Dry Run

Input:

```python
nums = [1, 2, 3, 4]
```

Prefix:

```python
[1, 2, 6, 24]
```

Postfix:

```python
[24, 24, 12, 4]
```

| Index | Left Product | Right Product | Result |
|---:|---:|---:|---:|
| 0 | 1 | 24 | 24 |
| 1 | 1 | 12 | 12 |
| 2 | 2 | 4 | 8 |
| 3 | 6 | 1 | 6 |

Final Output:

```python
[24, 12, 8, 6]
```

## Complexity Analysis

Let `n` be the length of the input array.

- **Time Complexity:** `O(n)` — three separate traversals, each taking linear time.
- **Auxiliary Space Complexity:** `O(n)` — prefix, postfix, and result arrays require additional space.

## Important Observations

1. **Why Prefix and Postfix?** They allow us to calculate the product excluding the current element without division.
2. **Why initialize arrays with 1?** One is the multiplicative identity, making boundary calculations easier.
3. **Why use `reversed(range(len(nums)))`?** It allows us to calculate postfix products from right to left.
4. **Handles zeros:** This approach works even when the input contains zero or multiple zeros.
5. **No division required:** The solution follows the problem's main constraint.

## Summary

The Prefix and Postfix approach calculates the product of elements on both sides of each index and multiplies them to obtain the final answer.

**Use:** This technique is useful in array problems involving cumulative products, running calculations, and finding values based on elements before and after a particular index.
