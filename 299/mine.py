class Solution:
  def getHint(self, secret: str, guess: str) -> str:
    bulls = 0
    crows = 0

    digits = {}
    compare = ""

    for i in range(len(secret)):
      if secret[i] == guess[i]:
        bulls += 1
      else:
        compare += guess[i]
        if secret[i] not in digits:
          digits[secret[i]] = 1
        else:
          digits[secret[i]] += 1
        
    
    for c in compare:
      if c in digits and digits[c] > 0:
        crows += 1
        digits[c] -= 1
      
    return f"{bulls}A{crows}B"
  
sol=  Solution()
a = sol.getHint("1807", "7810")
print(a)