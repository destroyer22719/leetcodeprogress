from typing import List


class Solution:
  def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
    squares1 = {}
    squares2 = {}
    
    vals1 = {}
    vals2 = {}

    sols = 0

    for i in range(max(len(nums1), len(nums2))):
      if i < len(nums1):
        squares1[nums1[i]**2] = squares1.get(nums1[i]**2, 0) + 1
        # vals1[nums1[i]] = vals1.get(nums1[i], 0) + 1
        vals1[nums1[i]] = 1

      if i < len(nums2):
        squares2[nums2[i]**2] = squares2.get(nums2[i]**2, 0) + 1
        # vals2[nums2[i]] = vals2.get(nums2[i], 0) + 1
        vals2[nums2[i]] = 1

    for i in range(max(len(nums1), len(nums2))):
      for j in range(i, max(len(nums1), len(nums2))):
        if i < len(nums1) and j < len(nums2):
          sq1 = nums1[i]**2
          sols += squares1[sq1]*vals2.get(sq1/nums2[j], 0)
        if i < len(nums2) and j < len(nums1):
          sq2 = nums2[i]**2
          sols += squares2[sq2]*vals1.get(sq2/nums1[j], 0)

    return sols//2
  
ansewr = Solution()
print(ansewr.numTriplets([7,4], [5,2,8,9]))

ansewr = Solution()
print(ansewr.numTriplets([1,1], [1,1,1]))