# 716. Max Stack
# Problem: https://leetcode.com/problems/max-stack/
# Submitted: 2026-10-29 14:58 EDT
# Intuition: A linked list handles stack order, while a max-heap finds the largest value and favors the latest equal value.
# Approach: Share nodes between both structures, unlink popped nodes, and lazily discard inactive heap entries.
# Complexity: O(1) top/pop, O(log p) amortized push/peekMax/popMax, O(p) space; p is total pushes.

import heapq

class Node:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val
        self.active = True

class MaxStack:

    def __init__(self):
        # dummy ends avoid special cases when linking nodes
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.max_heap = []
        self.counter = 0

    def pushNodeStack(self, node):
        # insert just before tail, which is the top of the stack
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
    
    def popNodeStack(self, node):
        # unlink from stack and mark the heap entry as removed
        node.prev.next = node.next
        node.next.prev = node.prev
        node.active = False
        return node.val

    def pushNodeHeap(self, node):
        # largest value first; newest node wins ties
        heapq.heappush(self.max_heap, (-node.val, -self.counter, node))
        self.counter += 1

    def popMaxHeap(self):
        # discard heap entries for nodes already popped from stack
        while not self.max_heap[0][2].active:
            heapq.heappop(self.max_heap)
        
        return heapq.heappop(self.max_heap)[2]

    def push(self, x: int) -> None:
        node = Node(x)
        self.pushNodeStack(node)
        self.pushNodeHeap(node)

    def pop(self) -> int:
        return self.popNodeStack(self.tail.prev)

    def top(self) -> int:
        return self.tail.prev.val

    def peekMax(self) -> int:
        # discard heap entries for nodes already popped from stack
        while not self.max_heap[0][2].active:
            heapq.heappop(self.max_heap)
        
        return -self.max_heap[0][0]

    def popMax(self) -> int:
        # remove max from heap, then unlink the same node from stack
        node = self.popMaxHeap()
        self.popNodeStack(node)

        return node.val
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()