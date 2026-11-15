#!/bin/python3
# HackerRank - Simple Text Editor
# Problem: https://www.hackerrank.com/challenges/simple-text-editor/problem
# Intuition: Save the inverse of each edit so undo can reverse it directly.
# Approach: Keep the text in a list of characters and push inverse operations
# onto a stack. Undo pops the last inverse and applies it without recording it.
# Complexity: O(k) time for an edit or undo touching k characters, and O(1)
# per print. Space is linear in the current text and the stored undo history.

curr = []
stack = []


def append(s, record=True):
    for c in s:
        curr.append(c)
    if record:
        stack.append((2, len(s)))


def delete(n, record=True):
    deleted = []
    for _ in range(n):
        c = curr.pop()
        deleted.append(c)
    if record:
        stack.append((1, "".join(deleted[::-1])))


def undo():
    op, value = stack.pop()
    if op == 1:
        append(value, False)
    else:
        delete(value, False)


q = int(input())
for _ in range(q):
    instruction = input().split()
    op = int(instruction[0])
    value = instruction[1] if len(instruction) > 1 else None

    if op == 1:
        append(value)
    elif op == 2:
        delete(int(value))
    elif op == 3:
        print(curr[int(value) - 1])
    else:
        undo()
