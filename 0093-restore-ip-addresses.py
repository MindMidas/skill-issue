# 93. Restore IP Addresses
# Problem: https://leetcode.com/problems/restore-ip-addresses/
# Submitted: 2026-11-18 19:09 EST
# Intuition: Each of the four IP address parts contains one to three digits.
# Approach: Try all lengths for the first three parts, then validate all four
# parts for length, leading zeros, and values at most 255.
# Complexity: O(n) time and O(n) temporary space due to slicing the remainder
# for each of the fixed 27 candidates. Valid IPv4 outputs have bounded length.


class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        def valid(part):
            if not part or len(part) > 3:
                return False
            elif len(part) > 1 and part[0] == "0":
                return False
            elif int(part) > 255:
                return False
            else:
                return True

        n = len(s)
        ans = []
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    a = s[:i]
                    b = s[i:i + j]
                    c = s[i + j:i + j + k]
                    d = s[i + j + k:]
                    if all(valid(part) for part in [a, b, c, d]):
                        ans.append(".".join([a, b, c, d]))
        return ans
