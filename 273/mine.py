class Solution:
  def numberToWords(self, num: int) -> str:
    hundreds = ""
    thousands = ""
    millions = ""
    billions = ""

    numbers = {
      "00": "",
      "0": "Zero",
      "1": "One",
      "2": "Two",
      "3": "Three",
      "4": "Four",
      "5": "Five",
      "6": "Six",
      "7": "Seven",
      "8": "Eight",
      "9": "Nine",
      "10": "Ten",
      "11": "Eleven",
      "12": "Twelve",
      "13": "Thirteen",
      "14": "Fourteen",
      "15": "Fifteen",
      "16": "Sixteen",
      "17": "Seventeen",
      "18": "Eighteen",
      "19": "Nineteen",
      "20": "Twenty",
      "30": "Thirty",
      "40": "Forty",
      "50": "Fifty",
      "60": "Sixty",
      "70": "Seventy",
      "80": "Eighty",
      "90": "Ninety",
      "100": "Hundred"
    }

    strNum =  str(num)

    for i in range(len(strNum) - 1, -1, -1):
      if len(hundreds) < 3:
        hundreds = f"{strNum[i]}{hundreds}"
      elif len(thousands) < 3:
        thousands = f"{strNum[i]}{thousands}"
      elif len(millions) < 3:
        millions = f"{strNum[i]}{millions}"
      elif len(billions) < 3:
        billions = f"{strNum[i]}{billions}"
      
    if len(hundreds) > 0:
      hundreds = hundreds[::-1]


      d1 = f"{numbers[hundreds[0]]}"
      if hundreds[0] == "0":
        if len(hundreds) > 1:
          d1 = ""
      d2 = ""
      d3 = ""

      if len(hundreds) >= 2:
        if len(hundreds) == 2:
          tens = hundreds[::-1]
          if int(tens) >= 11 and int(tens) <= 19:
            d1 = ""
            d2 = f"{numbers[tens]}"
          else:
            tens = f"{hundreds[1]}0"
            d2 = f"{numbers[tens]}"
        else:
          tens = hundreds[0:2][::-1]
          if int(tens) >= 11 and int(tens) <= 19:
            d1 = ""
            d2 = f"{numbers[tens]}"
          else:
            tens = f"{hundreds[1]}0"
            d2 = f"{numbers[tens]}"
      if len(hundreds) == 3:
        if hundreds[2] == "0":
          d3 = ""
        else:
          d3 = f"{numbers[hundreds[2]]} Hundred"

      hundreds = f"{d3} {d2} {d1}".strip()
    if len(thousands) > 0:
      d1 = self.numberToWords(int(thousands))

      if d1 != "Zero":
        thousands = f"{d1} Thousand"
      else:
        thousands = ""
    
    if len(millions) > 0:
      d1 = self.numberToWords(int(millions))

      if d1 != "Zero":
        millions = f"{d1} Million"
      else:
        millions = ""      

    if len(billions) > 0:
      d1 = self.numberToWords(int(billions))

      if d1 != "Zero":
        billions = f"{d1} Billion"
      else:
        billions = ""
    return " ".join(f"{billions} {millions} {thousands} {hundreds}".split())
        
sol = Solution()
a = sol.numberToWords(1000010)
print(a)