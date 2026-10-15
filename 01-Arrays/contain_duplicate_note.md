# Contains Duplicate

Platform:LeetCode  
Topic:Arrays  
Pattern:Hashing / Duplicate Detection  
Implementation: Python Dictionary (`dict`)  
Difficulty:Easy

## Problem Understanding

Determine whether an array contains any value that appears at least twice. Return `True` if a duplicate exists; otherwise, return `False`.

## My Approach

1. Create an empty dictionary.
2. Iterate through the array.
3. Check whether the current number is already in the dictionary.
4. If it exists, return `True`.
5. Otherwise, store the number.
6. If the loop finishes without finding a duplicate, return `False`.

## Why This Works

The dictionary stores previously encountered numbers. If a number appears again, it must already be present in the dictionary.

## Complexity Analysis

- Time:O(n) average.
- Auxiliary Space: O(n).

## What I Learned

- A hash map can detect duplicates efficiently.
- A set is a simpler alternative when only membership matters.
- A dictionary is useful when additional information, such as an index or frequency, must be stored.


