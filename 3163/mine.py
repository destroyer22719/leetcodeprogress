class Solution:
  def compressedString(self, word: str) -> str:
    if word == "":
      return word
    
    comp = ""
    count = 1
    char = word[0]

    for i in range(1, len(word)):
      if word[i] != word[i-1]:
        comp += f"9{char}"*(count//9) + (f"{count % 9}{char}" if count % 9 != 0 else "")
        count = 1
        char = word[i]
      else:
        count += 1

    return comp + f"9{char}"*(count//9) + (f"{count % 9}{char}" if count % 9 != 0 else "")

sol = Solution()
a = sol.compressedString("cccccccccc")
print(a)