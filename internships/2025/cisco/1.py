def funcValidPairs(inputStr):
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