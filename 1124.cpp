//https://leetcode.com/problems/longest-well-performing-interval/

#include <iostream>
#include <vector>

class Solution {
  public:
    static int longestWPI(std::vector<int>& hours) {
      // int maxIntLength = 0;

      // int currIntLength = 0;
      // int currRemainingLength = 0;

      // for(int i = 0; i < hours.size(); i++) {
      //   if (hours[i] > 8) {
      //     currIntLength++;
      //     currRemainingLength++;
      //   } else if (currRemainingLength > 0) {
      //     currIntLength++;
      //     currRemainingLength--;
      //     if (currRemainingLength == 0) {
      //       if (currIntLength - 1 > maxIntLength) {
      //         maxIntLength = currIntLength - 1;
      //       }
      //       currIntLength = 0;
      //     }
      //   }
      // }

      // if (currIntLength )

      // return maxIntLength;
      // }

      int cursor = 0;

      while (cursor ) {
        
      }
    }
};

int main() {
  std::vector<int> hours {9,9,6,0,6,6,9};
  int answer = Solution::longestWPI(hours);
  std::cout << answer << std::endl;
}
