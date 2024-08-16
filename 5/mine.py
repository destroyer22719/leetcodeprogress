class Solution:
  def longestPalindrome(self, s: str) -> str:
    longest = s[0]

    for i in range(len(s)):
      if len(s) - i < len(longest):
        break
      for j in range(i+1, len(s)):
        if j - i + 1 < len(longest):
          continue

        isPalindrome = True
        for k in range(i, (i + j + 1)//2):
          if s[k] != s[j-k+i]:
            isPalindrome = False
            break
        if isPalindrome and len(longest) < j - i + 1:
          longest = s[i:j+1]
    return longest

        

sol = Solution()
a = sol.longestPalindrome("abacab")
print(a)