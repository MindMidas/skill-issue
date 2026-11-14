# 1670. Design Front Middle Back Queue
# Problem: https://leetcode.com/problems/design-front-middle-back-queue/
# Submitted: 2026-11-14 12:12 EST
# Intuition: A doubly linked list gives direct access to each insertion and removal point.
# Approach: Track the head, tail, and frontmost middle node. Use the size before
# each operation to decide whether the middle pointer moves left or right.
# Complexity: O(1) time per operation and O(n) space for n queued elements.


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class FrontMiddleBackQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.mid = None
        self.size = 0

    def pushFront(self, val: int) -> None:
        new_node = Node(val)

        if not self.head:
            self.head = self.mid = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

            if self.size % 2 == 1:
                self.mid = self.mid.prev

        self.size += 1

    def pushMiddle(self, val: int) -> None:
        new_node = Node(val)

        if not self.head:
            self.head = self.mid = self.tail = new_node
        else:
            if self.size == 1:
                self.mid.prev = new_node
                new_node.next = self.mid
                self.mid = self.head = new_node
            elif self.size % 2 == 1:
                self.mid.prev.next = new_node
                new_node.prev = self.mid.prev
                new_node.next = self.mid
                self.mid.prev = new_node
                self.mid = new_node
            else:
                self.mid.next.prev = new_node
                new_node.next = self.mid.next
                new_node.prev = self.mid
                self.mid.next = new_node
                self.mid = new_node

        self.size += 1

    def pushBack(self, val: int) -> None:
        new_node = Node(val)

        if not self.head:
            self.head = self.mid = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

            if self.size % 2 == 0:
                self.mid = self.mid.next

        self.size += 1

    def popFront(self) -> int:
        if self.size == 0:
            return -1

        val = self.head.val
        if self.size == 1:
            self.head = self.mid = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

            if self.size % 2 == 0:
                self.mid = self.mid.next

        self.size -= 1
        return val

    def popMiddle(self) -> int:
        if self.size == 0:
            return -1

        val = self.mid.val
        if self.size == 1:
            self.head = self.mid = self.tail = None
        elif self.size == 2:
            self.head = self.head.next
            self.head.prev = None
            self.mid = self.head
        else:
            self.mid.prev.next = self.mid.next
            self.mid.next.prev = self.mid.prev

            if self.size % 2 == 1:
                self.mid = self.mid.prev
            else:
                self.mid = self.mid.next

        self.size -= 1
        return val

    def popBack(self) -> int:
        if self.size == 0:
            return -1

        val = self.tail.val
        if self.size == 1:
            self.head = self.mid = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

            if self.size % 2 == 1:
                self.mid = self.mid.prev

        self.size -= 1
        return val
