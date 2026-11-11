# 811. Subdomain Visit Count
# Problem: https://leetcode.com/problems/subdomain-visit-count/
# Submitted: 2026-11-11 15:18 EST
# Intuition: Each visit also counts toward every domain suffix formed by dropping leading labels.
# Approach: Split each entry into its count and domain labels, add the count to each suffix, and format the totals.
# Complexity: O(L + S) average time and O(L + S) space, where L is total input length and S is the combined length of the generated suffixes.

class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        counts = {}

        for cpdomain in cpdomains:
            data = cpdomain.split(" ")
            visits = int(data[0])
            domains = data[1].split(".")

            for i in range(len(domains)):
                key = ".".join(domains[i:])
                if key not in counts:
                    counts[key] = 0
                counts[key] += visits

        return [f"{visits} {domain}" for domain, visits in counts.items()]
