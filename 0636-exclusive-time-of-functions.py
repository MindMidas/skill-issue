# 636. Exclusive Time of Functions
# Problem: https://leetcode.com/problems/exclusive-time-of-functions/
# Submitted: 2026-09-21 18:53 EDT
# Intuition: A function's exclusive time excludes the time spent in its nested calls.
# Approach: Stack each call's start and child duration; subtract child time when it ends.
# Complexity: O(L) time, O(n + D) space; L is total log text length, D is nesting depth.

class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        
        stack = []
        result = [0] * n
        
        for log in logs:
            
            fid,event,time = log.split(":")

            fid = int(fid)
            time = int(time)

            if event == "start":
                stack.append([fid, time, 0])
            else:
                _, start_time, child_time = stack.pop()
                duration = time - start_time + 1
                result[fid] += duration - child_time

                if stack:
                    stack[-1][2] += duration
        
        return result
                