class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    # start = 0

    # if len(s) <= 1:
    #   return len(s)
    
    # length = 1
    # currLength = 1
    # for i in range(1, len(s)):
    #   if s[i] in s[start:i]:
    #     start = start + 1
    #     currLength = len(s[start:i+1])
    #   else:
    #     currLength += 1
    #     length = max(currLength, length)
    # return length

    start = 0

    if len(s) <= 1:
      return len(s)
    
    letters = {s[0]: 0}

    length = 1
    currLength = 1
    for i in range(1, len(s)):
      if s[i] in letters:
        start = letters[s[i]] + 1
        currLength = len(s[start:i+1])
        letters = {s[i]:i}
      else:
        currLength += 1
        length = max(currLength, length)
        letters[s[i]] = i
    return length
sol = Solution()
a = sol.lengthOfLongestSubstring("tmmzuxt")
print(a)
            