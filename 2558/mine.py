from typing import List

class Solution:
  def pickGifts(self, gifts: List[int], k: int) -> int:
    for _ in range(k):
      v = max(gifts)
      gifts[gifts.index(v)] = int(v**(1/2))
    return sum(gifts)
  

