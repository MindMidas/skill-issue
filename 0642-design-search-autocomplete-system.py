# 642. Design Search Autocomplete System
# Problem: https://leetcode.com/problems/design-search-autocomplete-system/
# Submitted: 2026-11-07 12:20 EST
# Intuition: Keep each sentence's frequency, then rank the sentences matching the current prefix.
# Approach: Append input characters until '#', scan the stored sentences for prefix matches, and sort the best three by frequency then lexicographic order.
# Complexity: Each input is O(S + r log r) time, where S is the total stored text and r is the number of matches. Storage is O(S).

class AutocompleteSystem:

    def __init__(self, sentences: list[str], times: list[int]):
        self.curr_sentence = ""
        self.freq = {}

        for i, s in enumerate(sentences):
            self.freq[s] = times[i]

    def input(self, c: str) -> list[str]:

        # end of sentence, store it
        if c == "#":
            self.freq[self.curr_sentence] = self.freq.get(self.curr_sentence, 0) + 1
            self.curr_sentence = ""
            return []
        else:
            # add char to current sentence
            self.curr_sentence += c

            # get matches
            matches = []
            for sentence in self.freq:
                if sentence.startswith(self.curr_sentence):
                    matches.append(sentence)

            # sort by descending frequency, breaking ties lexicographically
            matches.sort(key=lambda s: (-self.freq[s], s))

            return matches[:3]
