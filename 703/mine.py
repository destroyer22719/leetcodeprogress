from typing import List

class KthLargest:
  def __init__(self, k: int, nums: List[int]):
    self.nums = sorted(nums)
    self.k = k

  def add(self, val: int) -> int:
    for i in range(len(self.nums)):
      if i == 0 and val < self.nums[i]:
        self.nums = [val] + self.nums
      elif self.nums[i-1] <= val and val <= self.nums[i]:
        self.nums = self.nums[:i] + [val] + self.nums[i:]
        break
      if i == len(self.nums) - 1:
        self.nums.append(val)
    
    return self.nums[-self.k]
  
kthLargest = KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3)
kthLargest.add(5)
kthLargest.add(10)
kthLargest.add(9)
kthLargest.add(4)