# 721. Accounts Merge
# Problem: https://leetcode.com/problems/accounts-merge/
# Submitted: 2026-11-19 14:40 EST
# Intuition: Accounts sharing an email belong to the same connected component.
# Approach: Connect each account's emails to its first email, then use DFS to
# collect components and return their sorted emails with the account name.
# Complexity: O(E + U log U) time and O(E + U) space for E email occurrences
# and U unique emails, treating string operations as bounded.

from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        g = defaultdict(list)
        email_to_name = {}

        for account in accounts:
            emails = account[1:]
            name = account[0]
            g[emails[0]]
            email_to_name[emails[0]] = name
            for email in emails[1:]:
                g[emails[0]].append(email)
                g[email].append(emails[0])
                email_to_name[email] = name

        seen = set()
        ans = []

        def dfs(email, group):
            seen.add(email)
            group.append(email)
            for neighbor in g[email]:
                if neighbor not in seen:
                    dfs(neighbor, group)

        for email in g:
            if email not in seen:
                group = []
                dfs(email, group)
                ans.append([email_to_name[email]] + sorted(group))

        return ans
