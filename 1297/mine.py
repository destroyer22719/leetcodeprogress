class Solution:
  def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    left = 0, right = len(s) - 1

    curr_letters = {}

    while left <= right:
      if len(curr_letters) <= maxLetters and right - left < maxSize:
        right += 1
        if s[right] not in curr_letters:
          curr_letters[s[right]] = 0
        else:
          curr_letters[s[right]] += 1
      
      
      if len(curr_letters) > maxLetters