from typing import List

class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    a = nums1 if len(nums1) <= len(nums2) else nums2
    b = nums2 if len(nums1) < len(nums2) else nums1

    start = 0
    end = len(a) - 1

    while start <= end and len(b) != 0:
      mid = ( start + end ) // 2

      if a[mid-1] <=  a[mid]
