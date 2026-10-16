# Valid Anagram
Platform:LeetCode  
Topic:Strings  
Pattern:Hash Map / Frequency Counting / Sorting  
Difficulty:Easy

## 1. Problem Understanding

Given two strings `s` and `t`, determine whether `t` is an anagram of `s`.

Two strings are anagrams if they contain exactly the same characters with the same frequencies, regardless of order.

Example:

- Input: `s = "anagram"`, `t = "nagaram"`
- Output: `True`

- Input: `s = "rat"`, `t = "car"`
- Output: `False`

## 2. Approach 1: Two Dictionaries

### Logic

1. If the strings have different lengths, return `False`.
2. Create two dictionaries to count character frequencies.
3. Compare both dictionaries.
4. If their contents match, return `True`.

### Why it works

Both dictionaries represent the frequency of each character. Equal frequency dictionaries mean the strings contain the same characters in the same quantities.

### Complexity

- Time: O(n) average.
- Auxiliary space: O(k), where k is the number of distinct characters.

## 3. Approach 2: Sorting

### Logic

1. Check whether the string lengths are equal.
2. Sort both strings.
3. Compare the sorted results.
4. If they match, return `True`.

### Why it works

Sorting puts identical characters in the same order. If the sorted strings are equal, their original character frequencies must also match.

### Complexity

- Time: O(n log n).
- Auxiliary space: O(n) for the sorted lists.

## 4. Approach 3: One Dictionary

### Logic

1. Check whether the string lengths are equal.
2. Count each character in the first string.
3. Decrease the count for each character in the second string.
4. Return `False` if a character is missing from the dictionary.
5. Check that every remaining frequency is zero.

### Why it works

Characters shared by both strings cancel out through incrementing and decrementing. If every count reaches zero, all character frequencies match.

### Complexity

- Time: O(n) average.
- Auxiliary space: O(k), where k is the number of distinct characters.

## 5. Comparison of Approaches

| Approach | Time | Auxiliary Space | Main Idea |
|---|---|---|---|
| Two dictionaries | O(n) average | O(k) | Compare frequency counts |
| Sorting | O(n log n) | O(n) | Compare sorted characters |
| One dictionary | O(n) average | O(k) | Increment and decrement counts |

Here, `n` is the string length and `k` is the number of distinct characters.

## 6. What I Learned

- Dictionaries can efficiently count character frequencies.
- Sorting can simplify comparisons when order does not matter.
- A single dictionary can track frequency differences.
- Equal string lengths are a useful early check.
- The best approach depends on the problem and its constraints.

