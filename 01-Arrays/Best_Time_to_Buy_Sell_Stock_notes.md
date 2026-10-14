# Best Time to Buy and Sell Stock

Platform:LeetCode  
Topic:Arrays  
Pattern:Running Minimum / Greedy  
Implementation:Python  
Difficulty: Easy

## Problem Understanding

Given an array of stock prices, find the maximum profit by buying on one day and selling on a later day. If no profit is possible, return `0`.

## My Approach

1. Initialize `min_price` with the first price.
2. Iterate through the remaining prices.
3. Calculate the potential profit by selling at the current price: `price - min_price`.
4. Update `max_profit` if the current profit is greater.
5. Update `min_price` if the current price is lower.
6. Return `max_profit`.

## Why This Works

For each selling day, the best buying price is the minimum price seen before that day. Tracking this minimum avoids checking every possible buy-and-sell pair.

## Complexity Analysis

- Time:O(n) — one traversal of the prices.
- Auxiliary Space:O(1) — only a fixed number of variables.

## What I Learned

- A running minimum can eliminate the need for nested loops.
- The buying day must occur before the selling day.
- Updating the minimum price as I iterate helps find the maximum profit efficiently.
