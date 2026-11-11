# 2034. Stock Price Fluctuation
# Problem: https://leetcode.com/problems/stock-price-fluctuation/
# Submitted: 2026-11-11 14:10 EST
# Intuition: The price map holds the latest value for each timestamp, so heap entries can be checked against it.
# Approach: Track the latest timestamp and keep min and max heaps. Discard outdated entries when querying either extreme.
# Complexity: O(log u) per update, O(1) for current, O(1 + k log u) per extreme query that removes k entries, and O(u) space for u updates.

import heapq


class StockPrice:
    def __init__(self):
        self.prices = {}
        self.minimum_price = []
        self.maximum_price = []
        self.latest_timestamp = None

    def update(self, timestamp: int, price: int) -> None:
        self.prices[timestamp] = price
        heapq.heappush(self.maximum_price, (-price, timestamp))
        heapq.heappush(self.minimum_price, (price, timestamp))

        if not self.latest_timestamp or timestamp > self.latest_timestamp:
            self.latest_timestamp = timestamp

    def current(self) -> int:
        return self.prices[self.latest_timestamp] if self.latest_timestamp else None

    def maximum(self) -> int:
        while self.maximum_price and self.prices[self.maximum_price[0][1]] != -self.maximum_price[0][0]:
            heapq.heappop(self.maximum_price)
        return -self.maximum_price[0][0]

    def minimum(self) -> int:
        while self.minimum_price and self.prices[self.minimum_price[0][1]] != self.minimum_price[0][0]:
            heapq.heappop(self.minimum_price)
        return self.minimum_price[0][0]
