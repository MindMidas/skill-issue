#!/bin/python3
# HackerRank - QHEAP1
# Problem: https://www.hackerrank.com/challenges/qheap1/problem
# Intuition: A min-heap only needs to discard deleted entries when they reach the top.
# Approach: Count pending deletions by value. Before printing the minimum, pop
# stale entries from the top and decrement their pending counts.
# Complexity: O(q log q) total time and O(q) space for q queries. Each entry
# is pushed once and popped at most once.

import heapq

n = int(input())
heap = []
deleted = {}

for _ in range(n):
    data = input().split()
    op = data[0]
    val = int(data[1]) if len(data) > 1 else None

    if op == "1":
        heapq.heappush(heap, val)
    elif op == "2":
        deleted[val] = deleted.get(val, 0) + 1
    else:
        while heap and heap[0] in deleted and deleted[heap[0]] != 0:
            key = heapq.heappop(heap)
            deleted[key] -= 1

        print(heap[0])
