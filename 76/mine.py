class Solution:
  def minWindow(self, s: str, t: str) -> str:
    letters = {}
    letter_counts = {}
    letters_all_found = {}
    n = 0

    for l in t:
      letters[l] = []

      if l in letter_counts:
        letter_counts[l] += 1
      else:
        letter_counts[l] = 1
        n += 1
        letters_all_found[l] = False

    foundAll = False
    subStr = ""

    for i in range(len(s)):
      if s[i] not in letters:
        continue

      if len(letters[s[i]]) == letter_counts[s[i]]:
        letters[s[i]].pop(0)
        letters[s[i]].append(i)

      else:
        letters[s[i]].append(i)

        if len(letters[s[i]]) == letter_counts[s[i]]:
          letters_all_found[s[i]] = True
          if not False and False not in letters_all_found.values():
            foundAll = True


      if foundAll:
        mins = [sublist[0] for sublist in letters.values()]
        maxes = [sublist[-1] for sublist in letters.values()]

        start = mins[0]
        end = maxes[0]
        for i in range(n):
          start = min(start, mins[i])
          end = max(end, maxes[i])

        if subStr == "" or (end + 1 - start) < len(subStr):
          subStr = s[start: end + 1]


    return subStr

sol = Solution()
a = sol.minWindow("ADOBECODEBANC", "ABC")
print(a)