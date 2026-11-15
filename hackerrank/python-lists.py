#!/bin/python3
# HackerRank - Lists
# Problem: https://www.hackerrank.com/challenges/python-lists/problem
# Intuition: Each command maps to a built-in Python list operation or print.
# Approach: Read commands in order and convert their arguments to integers
# before applying each operation to the list.
# Complexity: Append and tail pop take amortized O(1) time. Insert, remove,
# reverse, and print take O(n) time, and sort takes O(n log n) in the worst
# case, where n is the current list length. Space is O(n).

if __name__ == "__main__":
    N = int(input())
    nums = []

    for _ in range(N):
        instruction = input().split()
        op = instruction[0]
        value1 = instruction[1] if len(instruction) > 1 else None
        value2 = instruction[2] if len(instruction) > 2 else None

        if op == "insert":
            nums.insert(int(value1), int(value2))
        elif op == "print":
            print(nums)
        elif op == "remove":
            nums.remove(int(value1))
        elif op == "append":
            nums.append(int(value1))
        elif op == "sort":
            nums.sort()
        elif op == "pop":
            nums.pop()
        else:
            nums.reverse()
