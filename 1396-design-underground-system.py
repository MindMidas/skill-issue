# 1396. Design Underground System
# Problem: https://leetcode.com/problems/design-underground-system/
# Submitted: 2026-11-11 11:21 EST
# Intuition: An average travel time needs only the total duration and number of completed trips for each route.
# Approach: Record check-ins by customer ID and accumulate duration and count at checkout for each ordered station pair.
# Complexity: O(1) average time per operation and O(c + r) space for c distinct customers and r routes.

class UndergroundSystem:
    # goal: return avg time taken to travel from station A to B
    # thought-process: we can have a customer start time dict where cid is used as key
    # to keep track of when a customer checks-in, in which case we add station A to B
    # travel time when the user checks-out to travel time dict where key is station (A, B)

    def __init__(self):
        self.start_time = {}
        self.travel_time = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start_time[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:

        # get start station and time
        station_a, time_a = self.start_time[id]

        # add time taken to travel_time
        key = (station_a, stationName)
        time_taken = t - time_a
        if key not in self.travel_time:
            self.travel_time[key] = (time_taken, 1)
        else:
            prev_total = self.travel_time[key][0]
            prev_count = self.travel_time[key][1]
            self.travel_time[key] = (prev_total + time_taken, prev_count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:

        key = (startStation, endStation)
        return self.travel_time[key][0] / self.travel_time[key][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
