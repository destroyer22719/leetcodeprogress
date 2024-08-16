from typing import List


class Codec:
  def encode(self, strs: List[str]) -> str:
    """Encodes a list of strings to a single string.
    """
    
    encoded = []

    for s in strs:
      e = ""
      for c in s:
        e += f"{ord(c)}-"
      encoded.append(e)
    return ",".join(encoded)
    

  def decode(self, s: str) -> List[str]:
    """Decodes a single string to a list of strings.
    """

    decoded = []

    for w in s.split(","):
      d = ""
      for c in w.split("-"): 
        if c == "":
          continue
        d += f"{chr(int(c))}"
      decoded.append(d)
    return decoded
  
c = Codec()

a = c.encode(["Hello","World"])
b = c.decode(a)
print(a)
print(b)