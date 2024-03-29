# https://www.youtube.com/watch?v=1pkOgXD63yU&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=2

class Solution:
  def maxProfit(self, prices):
    l,r = 0, 1
    maxProfit = 0

    while r < len(prices):
      if prices[l] < prices[r]:
        profit = prices[r] - prices[l]
        
        if (profit > maxProfit):
          maxProfit = profit
      
      else:
        l = r
      r += 1

    return maxProfit