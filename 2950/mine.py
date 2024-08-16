class Solution:
  def countDivisibleSubstrings(self, word: str) -> int:
    letters = {
      "a":1,
      "b": 1,
      "c": 2,
      "d": 2,
      "e": 2,
      "f": 3,
      "g": 3,
      "h": 3,
      "i": 4,
      "j": 4,
      "k": 4,
      "l": 5,
      "m": 5,
      "n": 5,
      "o": 6,
      "p": 6,
      "q": 6,
      "r": 7,
      "s": 7,
      "t": 7,
      "u": 8,
      "v": 8,
      "w": 8,
      "x": 9,
      "y": 9,
      "z": 9
    }

    def isDivisable(word):
      if len(word) == 1:
        return True

      total = 0

      for c in word:
        total += letters[c] 
      print(total)
      return total
      # return (total/len(word)).is_integer()
    
    result = 0

    for i in range(len(word)):
      curr_sum = letters[word[i]]

      for j in range(i, len(word)):
        if j != i:
          curr_sum += letters[word[j]]
        if (curr_sum/len(word[i:j+1])).is_integer():
          result += 1
    
    return result
  
sol = Solution()
print(sol.countDivisibleSubstrings("abcd"))

        
