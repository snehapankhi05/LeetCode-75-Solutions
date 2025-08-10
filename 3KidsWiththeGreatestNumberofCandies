class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        res = []
        for i in candies:
            if (i + extraCandies) >= maxCandies:
                res.append(True)
            else:
                res.append(False)
        return res  # Moved outside the loop
