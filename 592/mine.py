import math

class Solution:
  def fractionAddition(self, expression: str) -> str:
    numerators = []
    denominators = []

    is_neg = 1
    is_denom = False

    for i in range(len(expression)):
      if expression[i] == "0":
        continue
      
      if expression[i] == "+" or expression[i] == "-":
        if expression[i] == "+":
          is_neg = 1
        elif expression[i] == "-":
          is_neg = -1
        is_denom = False

      if expression[i] == "/":
        is_denom = True
        is_neg = 1
      if expression[i].isdigit():
        if i != len(expression) - 1 and expression[i] == "1" and expression[i+1] == "0":
          if is_denom:
            denominators.append(is_neg*10)
          else:
            numerators.append(is_neg*10)
        else:
          if is_denom:
            denominators.append(is_neg*int(expression[i]))
          else:
            numerators.append(is_neg*int(expression[i]))

    print(denominators)
    print(numerators)
    
    uniq_denominators = list(set(denominators))

    common_denom = 1

    for d in uniq_denominators:
      common_denom *= d
    
    for i in range(len(denominators)):
      product = common_denom/denominators[i]

      numerators[i] *= product
      denominators[i] *= product

    result = [ int(sum(numerators)), int(common_denom)]  
    gcd = math.gcd(result[0], result[1])

    answer = f"{int(result[0]/gcd)}/{int(result[1]/gcd)}"
    return answer


sol = Solution()
a = sol.fractionAddition("-5/2+10/3+7/9")
print(a)