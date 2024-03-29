class Solution:
  def subarraySum(self, nums, k: int) -> int:
    hm = {0: 1}

    curr_sum = 0
    total = 0
    for n in nums:
      curr_sum += n
      if (curr_sum - k) in hm:
        total += hm[curr_sum - k]
      if curr_sum in hm:
        hm[curr_sum] += 1
      else:
        hm[curr_sum] = 1
    return total
  
sol = Solution()

print(sol.subarraySum([1,1,1], 2))

