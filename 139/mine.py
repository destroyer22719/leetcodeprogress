from typing import List

class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    wordsInDict = set(wordDict)  # Using a set for O(1) lookups
    minLenWord = min(map(len, wordDict))
    maxLenWord = max(map(len, wordDict))
    
    memo = {}  # Dictionary for memoization
    
    def find(word):
        if word in memo:  # Check memoized results
            return memo[word]
        if word == "":  # Base case
            return True
        
        for i in range(minLenWord, min(maxLenWord, len(word)) + 1):
            if word[:i] in wordsInDict and find(word[i:]):
                memo[word] = True
                return True
        memo[word] = False
        return False
    
    return find(s)


sol = Solution()

answer = sol.wordBreak("applepenapple", ["apple","pen"])
print(answer)