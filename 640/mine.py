class Solution:
  def solveEquation(self, equation: str) -> str:
    sides = {
      "left": {
        "x": 0,
        "c": 0
      },
      "right": {
        "x": 0,
        "c": 0
      }
    }

    sign = 1
    curr_side = "left"
    curr_num = ""

    for c in equation:
      if c == "-":

        if curr_num != "":
          sides[curr_side]["c"] += sign*int(curr_num)
          curr_num = ""

        sign = -1
        curr_num = ""

      elif c == "+":

        if curr_num != "":
          sides[curr_side]["c"] += sign*int(curr_num)
          curr_num = ""
        sign = +1
        curr_num = ""

      elif c == "x":
        sides[curr_side]["x"] += sign
        if curr_num != "":
          sides[curr_side]["c"] += sign*int(curr_num)
          curr_num = ""

      elif c.isdigit():
        curr_num += c
      if c == "=":
        if curr_num != "":
          sides[curr_side]["c"] += sign*int(curr_num)
        curr_side = "right"

    if curr_num != "":
      sides[curr_side]["c"] += sign*int(curr_num)
    print(sides)

    sides["left"]["x"] -= sides["right"]["x"]
    sides["right"]["c"] -= sides["left"]["c"]

    string = f'{sides["left"]["x"]}x={sides["right"]["c"]}'
    print(string)

a = Solution()
sol = a.solveEquation("x+5-3+x=6+x-2")