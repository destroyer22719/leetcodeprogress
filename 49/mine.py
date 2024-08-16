from typing import List


class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    tracker = {}
    counter = {}

    for word in strs:
      tracker[word] = {}
      if word in counter:
        counter[word] += 1
      else:
        counter[word] = 1
      for letter in word:
        if letter not in tracker[word]:
          tracker[word][letter] = 1
        else:
          tracker[word][letter] += 1

    answer = []
    # for word_1 in list(tracker):
    while tracker != {}:
      word_1 = list(tracker.keys())[0]
      letter_tracker = tracker[word_1]
      answer.append([word_1]*counter[word_1])

      for word_2 in list(tracker):
        letter_tracker_2 = tracker[word_2]

        if word_1 == word_2:
          continue

        if letter_tracker == letter_tracker_2:
          answer[-1] += [word_2] * counter[word_2]
          del tracker[word_2]
      del tracker[word_1]

    return answer
  
sol = Solution()
a = sol.groupAnagrams(["eat", "eat", "tea","tan","ate","nat","bat"])
print(a)