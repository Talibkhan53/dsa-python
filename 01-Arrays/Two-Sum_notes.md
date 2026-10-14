# Two Sum
Platform:LeetCode  
Topic: Arrays  
Pattern:Hash Map  
Implementation:Python Dictionary (`dict`)  
Difficulty: Easy

## Problem Understanding

Given an array of integers `nums` and an integer `target`, return the indices of two numbers whose sum equals the target.

## My Approach

1. Create an empty dictionary called `seen` to store numbers and their indices.
2. Iterate through the array using `enumerate()`.
3. For each number, calculate the complement: `target - num`.
4. Check whether the complement already exists in `seen`.
5. If it exists, return the index of the complement and the current index.
6. Otherwise, store the current number and its index in the dictionary.

## Why This Works
Instead of checking every possible pair, I use a hash map to look up the required complement efficiently.

Python's `dict` implements a hash map, allowing average-case O(1) lookups and insertions.

## Complexity Analysis

- Time:O(n) average — each element is processed once.
- Auxiliary Space: O(n) — the dictionary may store up to n elements.

## What I Learned

- A Python dictionary (`dict`) implements the hash map concept.
- Hash maps help reduce repeated searching.
- Storing previously visited numbers allows an O(n) average-time solution instead of the O(n²) brute-force approach.
