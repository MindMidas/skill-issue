# 2353. Design a Food Rating System
# Problem: https://leetcode.com/problems/design-a-food-rating-system/
# Submitted: 2026-11-11 14:53 EST
# Intuition: A heap ordered by negative rating and food name gives the best food and breaks ties alphabetically.
# Approach: Keep a heap for each cuisine and a map of current ratings. Push each new rating and discard stale heap entries when querying.
# Complexity: O(n log n) initialization, O(log h) per update, O(1 + k log h) per query that removes k entries, and O(h) total space, where h is the total number of heap entries.

import heapq


class FoodRatings:
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.ratings = {}
        self.cuisine_food = {}
        self.food_cuisine = {}
        self.highest_rating = {}

        for i, f in enumerate(foods):
            c = cuisines[i]
            r = ratings[i]

            if c not in self.cuisine_food:
                self.cuisine_food[c] = []
            self.cuisine_food[c].append(f)
            self.food_cuisine[f] = c
            self.ratings[f] = r

            if c not in self.highest_rating:
                self.highest_rating[c] = []
            heapq.heappush(self.highest_rating[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        if food in self.ratings:
            c = self.food_cuisine[food]
            self.ratings[food] = newRating
            heapq.heappush(self.highest_rating[c], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.highest_rating[cuisine]:
            r, f = self.highest_rating[cuisine][0]
            if self.ratings[f] == -r:
                break
            heapq.heappop(self.highest_rating[cuisine])

        return self.highest_rating[cuisine][0][1]
