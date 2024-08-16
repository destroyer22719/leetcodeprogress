
class Solution:
  def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    startX = max([ax1, bx1])
    endX = min([ax2, bx2])

    print(startX, endX)

    startY = max([ay1, by1])
    endY = min([ay2, by2])

    print(startY, endY)

    intersection = 0 if startX > endX or startY > endY else (endY-startY)*(endX-startX)
    intersection = intersection if intersection >= 0 else -intersection
    area = ((ax2-ax1)*(ay2-ay1)+(bx2-bx1)*(by2-by1))-intersection
    return area
      
sol = Solution()
a = sol.computeArea(-3,0,3,4,0,-1,9,2)
print(a)