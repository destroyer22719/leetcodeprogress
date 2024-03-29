# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution(object):
  def maxProfit(self, prices):
    maxProfit = 0

    for i in range(len(prices) - 1):
      sellPrices = prices[i + 1:]
      highest = max(sellPrices)
      profit = highest - prices[i] 

      if (profit > maxProfit):
        maxProfit = profit
    return maxProfit
  
answer = Solution()
answer = answer.maxProfit([7,1,5,3,6,4])

print(answer)