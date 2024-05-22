from typing import List

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    numsInDict = {n: True for n in nums}

    if nums == []:
      return 0

    longest = 1
    for n in list(numsInDict):
      # if numsInDict[n] == True:
      #   continue

      curLen = 1

      next = n + 1
      while next in numsInDict:
        # numsInDict[next] = True
        del numsInDict[next]
        next += 1
        curLen += 1

        longest = max(longest, curLen)
      
      prev = n - 1
      while prev in numsInDict:
        # numsInDict[next] = True
        del numsInDict[prev]
        prev -= 1
        curLen += 1

        longest = max(longest, curLen)
    return longest
  
sol = Solution()
answer = sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
print(answer)
