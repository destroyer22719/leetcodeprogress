from typing import List


class Solution:
  def calculateArea(self, height, l, r):
    return (r - l)*(min(height[l],height[r]))
  
  def maxArea(self, height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    maxArea = 0

    while (left <= right):
      currArea = self.calculateArea(height, left, right)

      if (currArea > maxArea):
        maxArea = currArea
      
      if (height[left] < height[right]):
        left += 1
      else:
        right -= 1
    return maxArea
  
sol = Solution()

print(sol.maxArea([1,1]))