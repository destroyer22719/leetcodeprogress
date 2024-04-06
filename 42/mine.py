from typing import List


# class Solution:
#   def trap(self, height: List[int]) -> int:
    # total = 0

    # pairs = []
    # unpaired = []

    # starting_pillar = None

    # isDecreasing = None

    # for i in range(1, len(height)):
    #   if (height[i-1] > height[i]):
    #     unpaired.append(i)
    #     isDecreasing = True

    #     if (starting_pillar == None):
    #       starting_pillar = i
    #   else:
    #     isDecreasing = False
      
    #   if isDecreasing == False:
        