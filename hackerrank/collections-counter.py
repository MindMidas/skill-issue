#!/bin/python3
# HackerRank - collections.Counter()
# Problem: https://www.hackerrank.com/challenges/collections-counter/problem
# Intuition: The count for each shoe size tells us whether a sale can go through.
# Approach: Count the initial stock by size, then process customers in order.
# For each sale, decrement that size's stock and add the price to the total.
# Complexity: O(n + m) expected time for n shoes and m customers. The counter
# stores O(d) distinct sizes, and splitting the shoe input uses O(n) space.

from collections import Counter

int(input())  # Number of shoes
available = Counter(map(int, input().split()))
customers = int(input())

earned = 0
for _ in range(customers):
    want_size, want_price = map(int, input().split())
    if available[want_size] > 0:
        available[want_size] -= 1
        earned += want_price

print(earned)
