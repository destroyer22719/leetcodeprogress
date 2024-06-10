from typing import List

class Solution:
  def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    result = []

    def bs_insert(v, l):
      left = 0
      right = len(l) - 1

      if l == []:
        l.append(v)

      while left <= right:
        mid = (left+right) // 2

        if l[mid] == v:
          l.insert(mid, v)
          return
        elif (mid == len(l) - 1 and l[mid] < v) or (mid != len(l) - 1 and l[mid] <= v and v <= l[mid + 1]):
          l.insert(mid+1, v)
          return
        elif (mid == 0 and v < l[mid]) or (mid != 0 and l[mid-1] <= v and v <= l[mid]):
          l.insert(mid, v)
          return
        elif l[mid] > v:
          right = mid - 1
        else:
          left = mid + 1
    
    def bs_del(v, l):
      left = 0
      right = len(l) - 1

      while left <= right:
        mid = (left+right) // 2

        if l[mid] == v:
          l.pop(mid)
          return
        if l[mid] > v:
          right = mid -1
        else:
          left = mid + 1


    window = sorted(nums[:k])
    result.append(window[-1])

    for i in range(k, len(nums)):
      bs_del(nums[i-k], window)
      bs_insert(nums[i], window)
      result.append(window[-1])
      
    return result

sol = Solution()

answer = sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
print(answer)

answer = sol.maxSlidingWindow([1,-1], 1)
print(answer)
