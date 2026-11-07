# 1152. Analyze User Website Visit Pattern
# Problem: https://leetcode.com/problems/analyze-user-website-visit-pattern/
# Submitted: 2026-11-07 14:37 EST
# Intuition: Each user contributes at most one point to each ordered three-website pattern.
# Approach: Sort visits by timestamp, group them by user, enumerate each user's distinct triplets, and choose the highest score with lexicographic tie-breaking.
# Complexity: O(n log n + sum(m_u^3)) time and O(n + P + max(m_u^3)) space, where m_u is a user's visit count and P is the number of distinct patterns.

class Solution:
    def mostVisitedPattern(self, username: list[str], timestamp: list[int], website: list[str]) -> list[str]:

        # zip all three and sort by timestamp
        records = sorted(zip(timestamp, website, username))

        # gen user visits array that stores websites visited by user in order
        user_visits = {}
        for t, w, u in records:
            if u not in user_visits:
                user_visits[u] = []
            user_visits[u].append(w)

        # gen valid triplet visits per user given website order
        scores = {}
        for user, sites in user_visits.items():
            patterns = set()

            # add possible permutation
            for i in range(len(sites)):
                for j in range(i + 1, len(sites)):
                    for k in range(j + 1, len(sites)):
                        patterns.add((sites[i], sites[j], sites[k]))

            # increment score once per user
            for pattern in patterns:
                scores[pattern] = scores.get(pattern, 0) + 1

        # get best score (count and if then lexicographically smallest)
        best = min(scores, key=lambda p: (-scores[p], p))

        return list(best)
