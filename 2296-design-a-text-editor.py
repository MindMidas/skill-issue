# 2296. Design a Text Editor
# Problem: https://leetcode.com/problems/design-a-text-editor/
# Submitted: 2026-11-14 13:45 EST
# Intuition: A doubly linked list allows edits and cursor movement one character at a time.
# Approach: Track the nodes on either side of the cursor and the number of
# characters to its left. Relink at the cursor after edits and read up to ten
# characters backward after a cursor move.
# Complexity: O(len(text)) time to add text. Deletion and cursor movement take
# O(k) time, with at most ten extra steps to produce the preview. O(n) space for n characters.


class Node:
    def __init__(self, char):
        self.char = char
        self.next = None
        self.prev = None


class TextEditor:
    def __init__(self):
        self.cursor = Node(None)
        self.k_left = 0

    def addText(self, text: str) -> None:
        for char in text:
            new_node = Node(char)

            if self.cursor.prev:
                self.cursor.prev.next = new_node
            new_node.prev = self.cursor.prev
            self.cursor.prev = new_node

        # Connect the inserted text to the suffix.
        self.cursor.prev.next = self.cursor.next
        if self.cursor.next:
            self.cursor.next.prev = self.cursor.prev

        self.k_left += len(text)

    def deleteText(self, k: int) -> int:
        delete = min(k, self.k_left)
        self.k_left -= delete
        i = 0

        while i != delete:
            if self.cursor.prev.prev:
                self.cursor.prev = self.cursor.prev.prev
            else:
                self.cursor.prev = None
            i += 1

        # Reconnect the text on either side of the deletion.
        if self.cursor.prev:
            self.cursor.prev.next = self.cursor.next
        if self.cursor.next:
            self.cursor.next.prev = self.cursor.prev

        return delete

    def cursorLeft(self, k: int) -> str:
        moves = min(k, self.k_left)
        self.k_left -= moves
        i = 0

        while i < moves:
            self.cursor.next = self.cursor.prev
            self.cursor.prev = self.cursor.prev.prev
            i += 1

        lefttext = ""
        lefttext_len = min(10, self.k_left)
        dummy = self.cursor.prev

        for _ in range(lefttext_len):
            if dummy:
                lefttext += dummy.char
                dummy = dummy.prev
            else:
                break

        return lefttext[::-1]

    def cursorRight(self, k: int) -> str:
        moves = 0

        while moves < k and self.cursor.next:
            self.cursor.prev = self.cursor.next
            self.cursor.next = self.cursor.next.next
            moves += 1
        self.k_left += moves

        lefttext = ""
        lefttext_len = min(10, self.k_left)
        dummy = self.cursor.prev

        for _ in range(lefttext_len):
            if dummy:
                lefttext += dummy.char
                dummy = dummy.prev
            else:
                break

        return lefttext[::-1]
