def palindrome_num(num):
  return str(num) == str(num)[::-1]

print(palindrome_num(44444))