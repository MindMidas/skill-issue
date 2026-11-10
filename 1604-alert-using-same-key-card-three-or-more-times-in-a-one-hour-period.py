# 1604. Alert Using Same Key-Card Three or More Times in a One Hour Period
# Problem: https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/
# Submitted: 2026-11-10 17:25 EST
# Intuition: After sorting an employee's swipes, any qualifying hour contains three consecutive swipes.
# Approach: Group swipe times by employee and convert them to minutes. Sort each group and slide a window of three, then return the alerted names in alphabetical order.
# Complexity: O(n log n) time and O(n) space, where n is the number of swipes.

class Solution:
    def alertNames(self, keyName: list[str], keyTime: list[str]) -> list[str]:

        # intuition: create a dict by employee name where we store the
        # times for key card converted to total mins. We can then use a
        # 3 item sliding window to see if it overlaps

        names = set(keyName)
        access_time = {}
        result = []

        # populate dict
        for i, name in enumerate(keyName):
            if name not in access_time:
                access_time[name] = []
            hours, mins = map(int, keyTime[i].split(':'))
            access_time[name].append(60*hours + mins)

        # sliding window on sorted access_time for name
        for name in names:

            access_time[name].sort()

            left = 0
            right = min(2, len(access_time[name]) - 1)

            if right - left < 2:
                continue

            while right < len(access_time[name]):
                if access_time[name][right] - access_time[name][left] <= 60:
                    result.append(name)
                    break

                right += 1
                left += 1

        return sorted(result)
