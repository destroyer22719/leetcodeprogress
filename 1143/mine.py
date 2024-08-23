class Solution:
  def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    n = len(text1) - 1
    m = len(text2) - 1

    i = n
    j = m

    count = 0

    while i != -1 and j != -1:
      if text1[i] == text2[j]:
        count += 1
        j -= 1
      i -= 1

    return count
  
sol = Solution()
a = sol.longestCommonSubsequence("bl", "yby")

print(a)