class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    # maxSub = 0
    # for i in range(len(s)):
    #   letters = {s[i]:1}
    #   length = len(s) - i
    #   for j in range(i+1, len(s)):
    #     if s[j] not in letters:
    #       letters[s[j]] = 1
    #     else:
    #       letters[s[j]] += 1

    #     if max(letters.values() or [0]) + k <j-i+1:
    #       length = max(letters.values() or [0]) + k
    #       break
        
    #   maxSub = max(maxSub, length)
    # return maxSub

    if s == "":
      return 0
    
    gap = 1
    letters = {s[0]:1}

    for i in range(len(s)):
      if s[i-1] in letters and i != 0:
        letters[s[i-1]] -= 1
      
      newGap = gap
      for j in range(i + gap, len(s)):
        if s[j] not in letters:
          letters[s[j]] = 1
        else:
          letters[s[j]] += 1

        if max(letters.values() or [0]) + k <j-i+1:
          break   

        newGap += 1
      gap = newGap
    return gap


sol = Solution()

a = sol.characterReplacement("AAAA", 0)
print(a)


a = sol.characterReplacement("ABAB", 2)
print(a)

a = sol.characterReplacement("AABABBA", 1)
print(a)

a = sol.characterReplacement("ABBB", 1)
print(a)