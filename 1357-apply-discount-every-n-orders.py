# 1357. Apply Discount Every n Orders
# Problem: https://leetcode.com/problems/apply-discount-every-n-orders/
# Submitted: 2026-11-12 14:25 EST
# Intuition: Map product IDs to prices and use an order counter to identify discount orders.
# Approach: Sum the price times quantity for each item, then apply the discount when the order count is divisible by n.
# Complexity: O(p) initialization time and space for p products, and O(k) time and O(1) extra space per bill with k items.

class Cashier:
    def __init__(self, n: int, discount: int, products: list[int], prices: list[int]):
        self.prices = {}
        self.count = 0
        self.discount = discount
        self.n = n

        for i, p in enumerate(products):
            self.prices[p] = prices[i]

    def getBill(self, product: list[int], amount: list[int]) -> float:
        self.count += 1
        total = 0

        for i, p in enumerate(product):
            total += self.prices[p] * amount[i]

        if self.count % self.n == 0:
            total = total * ((100 - self.discount) / 100)

        return total


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
