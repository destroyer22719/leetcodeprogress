def second_largest(nums):
  first = nums[0]
  second = nums[0]

  if nums == []:
    return None
  
  for i in range(1, len(nums)):
    if nums[i] > first:
      second = first
      first = nums[i]
    elif nums[i] > second:
      second = nums[i]

  return second

print(second_largest( [3, 5, 2, 9, 1]))