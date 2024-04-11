from functools import reduce


class Solution:
  def smallestNumber(self, num: int) -> int:
    isNeg = num < 0
    num = abs(num)

    toArray = list(map(int, str(num)))

    if num == 0:
      return num
    elif not isNeg:
      toArray = sorted(toArray)
      if toArray[0] == 0:
        for i in range(len(toArray)):
          if toArray[i] != 0:
            toArray[0], toArray[i] = toArray[i], toArray[0]
            break
    else:
       toArray = sorted(toArray, reverse=True)
    answer = int(''.join([ "%d"%x for x in toArray]))

    if isNeg:
      return -answer
    else:
      return answer

sol = Solution()

# answer = sol.smallestNumber(310)
# print(answer)

answer = sol.smallestNumber(95005)
print(answer)

