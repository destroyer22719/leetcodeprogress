def funcTwins(inputArr):
  for i in range(0, len(inputArr), 2):
    if inputArr[i] >= len(inputArr) - 1 or inputArr[i] != inputArr[i+1]:
      return inputArr[i]
  return -1

print(funcTwins([1,1,2,3,3,4,4]))