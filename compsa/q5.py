def two_sum(nums, target):
  hashmap = {}

  for i in range(len(nums)):
    if target - nums[i] in hashmap:
      return [nums[i], target - nums[i]]
    hashmap[nums[i]] = True

print(two_sum( [3,3], 6))