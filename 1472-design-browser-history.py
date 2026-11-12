# 1472. Design Browser History
# Problem: https://leetcode.com/problems/design-browser-history/
# Submitted: 2026-11-12 12:17 EST
# Intuition: Each page links to the previous and next pages, and a cursor tracks the current page.
# Approach: Replace the current page's next link on each visit to discard forward history. Follow links for back and forward until the requested steps are exhausted or the end is reached.
# Complexity: O(1) link updates per visit and O(steps) time for back or forward, bounded by the available history. Space is O(h) for h pages in the history.

class website:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = website(homepage)

    def visit(self, url: str) -> None:
        self.curr.next = website(url)
        self.curr.next.prev = self.curr
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while steps != 0 and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1

        return self.curr.url

    def forward(self, steps: int) -> str:
        while steps != 0 and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
