# LeetCode 344 — Reverse String

## Problem Statement

Write a function that reverses a list of characters `s` in-place.

You must modify the original list without returning anything.

### Example

```python
Input:  s = ["h", "e", "l", "l", "o"]
Output: ["o", "l", "l", "e", "h"]
```

## Approach: Two Pointers

### Code

```python
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Modify s in-place instead of returning a new list.
        """
        n = len(s)
        i = 0
        j = n - 1

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
```

### Intuition

Use two pointers:

- `i` starts at the beginning of the list.
- `j` starts at the end of the list.

Swap the characters at both pointers, then move `i` one step forward and `j` one step backward. Repeat until the pointers meet or cross.

### Dry Run

Input:

```python
s = ["h", "e", "l", "l", "o"]
```

| Step | `i` | `j` | List after swapping |
|---|---:|---:|---|
| 1 | 0 | 4 | `["o", "e", "l", "l", "h"]` |
| 2 | 1 | 3 | `["o", "l", "l", "e", "h"]` |
| Stop | 2 | 2 | Pointers meet |

Final output:

```python
["o", "l", "l", "e", "h"]
```

## Complexity Analysis

- **Time complexity:** `O(n)` — each pair of characters is swapped once.
- **Auxiliary space complexity:** `O(1)` — only two pointers and a temporary swap are needed.

## Important Observations

1. The condition `i < j` prevents unnecessary swaps when the pointers meet.
2. Python's tuple assignment allows swapping two elements without an explicit temporary variable.
3. Only half the list needs to be traversed because each swap fixes two positions.

## Summary

The two-pointer approach reverses a list efficiently in-place using `O(n)` time and `O(1)` auxiliary space.

**Use:** This technique is useful in array reversal, palindrome checks, and other problems where elements at opposite ends must be compared or swapped.
