# 1169. Invalid Transactions
# Problem: https://leetcode.com/problems/invalid-transactions/
# Submitted: 2026-11-09 12:44 EST
# Intuition: Only transactions sharing a name can invalidate each other, and original indices preserve duplicate transactions.
# Approach: Group parsed transactions by name, flag amounts over 1000, and compare pairs within each group for different cities within 60 minutes. Return transactions at flagged indices.
# Complexity: O(n^2) worst-case time and O(n) space, treating transaction string lengths as bounded.

class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:

        # Goal: return invalid transactions, order doesn't matter
        # Invalid criteria: within 60m of other txs in diff city with same name OR value exceeds $1000
        # Intuition: we could process each and store them in a dict by name since the overlaps has that as a clause, and then find overlaps. Could also do just two for loops and brute force compare which is same time complexity but idk i found the dict cleaner

        tx_by_name = {}
        invalid = set()

        for i, tx in enumerate(transactions):

            # unpack values
            data = tx.split(',')
            processed_tx = (data[0], int(data[1]), int(data[2]), data[3], i)

            # greater than 1000 is invalid
            if processed_tx[2] > 1000:
                invalid.add(i)

            # add tx by name to dict
            if processed_tx[0] not in tx_by_name:
                tx_by_name[processed_tx[0]] = []
            tx_by_name[processed_tx[0]].append(processed_tx)

        # iterate over txs for each name
        # and check for any time overlap with diff city name
        for key, txs in tx_by_name.items():

            for i in range(len(txs)):
                for j in range(i + 1, len(txs)):

                    # check if it overlaps with different city name
                    if abs(txs[i][1] - txs[j][1]) <= 60 and txs[i][3] != txs[j][3]:
                        invalid.add(txs[i][4])
                        invalid.add(txs[j][4])

        return [transactions[i] for i in range(len(transactions)) if i in invalid]
