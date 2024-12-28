def first_non_repeat(string): 
  occurences = {}

  for s in string:
    occurences[s] = occurences.get(s, 0) + 1
  
  for s in string:
    if occurences[s] == 1:
      return s
  return ""

print(first_non_repeat("huh"))