class Solution(object):
  def findMin(self, nums):
    left = 0
    right = len(nums)-1

    if right == 0:
      return nums[0]

    while True:
      mid = (left + right) // 2

      if mid + 1 == right and mid - 1 == left:
        return min(nums[left], nums[mid], nums[right])
      elif mid + 1 == right and (right - left == 1):
        return min(nums[mid], nums[right])
      elif mid - 1 == left and (right - left == 1):
        return min(nums[mid], nums[left])
      elif nums[mid] > nums[right]:
        left = mid
      else:
        right = mid

MySol = Solution()

answer = MySol.findMin([2,3,4,5,6,1])
print(answer)