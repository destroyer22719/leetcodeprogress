
"""
inputStr, represents the given string containing substring of latitude/longitude pairs.
"""

def funcValidPairsEach(inputStr):
  if inputStr[0] != "(" or inputStr[-1] != ")":
    return False
  if "," not in inputStr:
    return False
  
  x = inputStr.split(",")[0]
  y = inputStr.split(",")[1]

  if x[0] == "-" or x[0] == "+":
    if not x[1:].isdigit():
      return False
    x = int(x[1:])
    if x > 90 or x < -90:
      return False
  else:
    if not x.isdigit():
      return False
    x = int(x)
    if x > 90 or x < -90:
      return False
  
  if y[0] == "-" or y[0] == "+":
    if not y[1:].isdigit():
      return False
    y = int(y[1:])
    if y > 90 or y < -90:
      return False
  else:
    if not y.isdigit():
      return False
    y = int(y)
    if y > 90 or y < -90:
      return False
  return True   


def funcValidPairs(inputStr):
  result = []

  for i in inputStr:
    a = funcValidPairsEach(i)

    if a == True:
      result.append("Valid")
    else:
      result.append("Invalid")

def main():
	#input for inputStr
	inputStr = []
	inputStr_size  = 6
	inputStr = list(map(str,input().split()))
	
	
	result = funcValidPairs(inputStr)
	print(" ".join([str(res) for res in result]))	

if __name__ == "__main__":
	main()