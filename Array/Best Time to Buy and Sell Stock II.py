
"""


    # Examples 
    Input: prices = [7,1,5,3,6,4]
    Output: 7
    Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
    Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
    Total profit is 4 + 3 = 7.

    Key Ideas:
    1. We are interested in only positive movements (Refer to the image from Leetcode)
    2. Tricky case is consecutive positive movement but this concern can be disregarded as we collect each positive movement anyway

        Ex: [1, 2, 3]
            Day 1 profit: 2 - 1 = 1
            Day 2 profit: 3 - 2 = 1
            Total: 2
    PS. Alternate way would be keeping 'l' stay for every positive movements 
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        l = 0
        for r, price in enumerate(prices):
            if r == 0:
                continue

            if prices[l] <= prices[r]:
                total += prices[r] - prices[l]
                l = r
            else:  
                l += 1
        return total

        