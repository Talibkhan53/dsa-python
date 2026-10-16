# Valid Palindrome

**Platform:** LeetCode  
**Topic:** Strings  
**Pattern:** Two Pointers  
**Difficulty:** Easy

## 1. Problem Understanding

Given a string, determine whether it is a palindrome after converting uppercase letters to lowercase and removing all non-alphanumeric characters.

A palindrome reads the same forward and backward.

Example:

- Input: `"A man, a plan, a canal: Panama"`
- Cleaned string: `"amanaplanacanalpanama"`
- Output: `True`

## 2. My Approaches

### Approach 1: Manual Filtering

1. Convert the string to lowercase.
2. Create a list of punctuation and symbols to remove.
3. Build a cleaned string by excluding characters in that list.
4. Use two pointers to compare characters from opposite ends.
5. Return `False` if any pair differs; otherwise, return `True`.

Limitation:The list may not include every possible symbol or punctuation character.

### Approach 2: Built-in Filtering

1. Convert the string to lowercase.
2. Use Python's `isalnum()` method to retain only letters and digits.
3. Use two pointers to compare characters from both ends.
4. Return `False` if a mismatch occurs; otherwise, return `True`.

Advantage:This avoids manually maintaining a list of symbols.

## 3. Two-Pointer Logic

- `i` starts at the beginning of the cleaned string.
- `j` starts at the end.
- Compare `new_str[i]` with `new_str[j]`.
- If they differ, the string is not a palindrome.
- Otherwise, increment `i` and decrement `j`.
- Stop when `i >= j`.

Why this works: Every pair of characters equidistant from opposite ends must match for the string to be a palindrome.

## 4. Complexity Analysis

Let `n` be the length of the input string.

For both approaches:

- Time:O(n), assuming a fixed-size character alphabet for the manual list.
- Auxiliary space:O(n), for the cleaned string.

The two-pointer comparison itself takes O(n) time and O(1) extra space.

## 5. What I Learned

- How to use the two-pointer technique for palindrome checking.
- Why string preprocessing is useful.
- How `isalnum()` identifies letters and digits.
- Why built-in methods can be more reliable than manually listing symbols.
- How to separate preprocessing from the core algorithm.


