def find_uniques(l):
  hashmap = {}

  for i in l:
    if i in hashmap:
      hashmap[i] = False
    else:
      hashmap[i] = True
  
  answer = []
  for key, value in hashmap.items():
    if value == True:
      answer.append(key)
  return answer

print(find_uniques([1, 2, 2, 3, 4, 4, 5]
))