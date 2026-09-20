# 2043. Simple Bank System
# Problem: https://leetcode.com/problems/simple-bank-system/
# Submitted: 2026-09-20 13:55 EDT
# Intuition: An operation is valid only when accounts exist and the sender has enough money.
# Approach: Keep the supplied balance list and validate before updating its entries.
# Complexity: O(1) time per operation, O(1) extra space; the supplied balance list is reused.

class Bank:

    def __init__(self, balance: list[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        
        if not (1 <= account1 <= len(self.balance)) or self.balance[account1-1] < money:
            return False
        if not (1 <= account2 <= len(self.balance)):
            return False
        
        self.balance[account1-1] -= money
        self.balance[account2-1] += money

        return True
      

    def deposit(self, account: int, money: int) -> bool:
        if not (1 <= account <= len(self.balance)):
            return False
        self.balance[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        
        if not (1 <= account <= len(self.balance)) or self.balance[account-1] < money:
            return False
        
        self.balance[account-1] -= money
        return True

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)