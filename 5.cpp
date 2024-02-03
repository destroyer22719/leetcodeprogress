//https://leetcode.com/problems/longest-palindromic-substring/

#include <iostream>
#include <string>
#include <algorithm> 

class Solution {
public:
  static bool isPalindrome(std::string s){
    std::string reversed = s;
    std::reverse(reversed.begin(), reversed.end());

    return s == reversed;
  }

  static std::string longestPalindrome(std::string s) {
    std::string result = "";
    int n = s.length();

    if (n == 1) {
      return s;
    }

    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n + 1; j++) {
        std::string x = s.substr(i, j - i);
        if (isPalindrome(x) && x.length() > result.length()) {
          result = x;
        }
      }
    }

    return result;
  }

  // static std::string longestPalindrome(std::string s) {
  //   std::string longest = "";
  //   std::string curr = "";

  //   for (int i = 1; i < s.length(); i++) {
  //     curr = s[i];

  //     int lIndex = 0;
  //     int rIndex = 0;

  //     while (true) {
  //       bool canShiftLeft = i - (lIndex + 1) > 0;
  //       bool canShiftRight = i + rIndex + 1 < s.length() - 1;

  //       if (canShiftLeft && canShiftRight) {

  //         std::string newStr = s[i- (lIndex + 1)] + curr + s[i+ rIndex + 1];

  //         if (isPalindrome(newStr)) {
  //           curr = newStr;
  //           lIndex++;
  //           rIndex++;
  //           continue;
  //         }
  //       } else if (canShiftLeft) {
  //         std::string newStr = s[i-(lIndex + 1)] + curr;

  //         if (isPalindrome(newStr)) {
  //           curr = newStr;
  //           lIndex++;
  //           continue;
  //         }
  //       } else if (canShiftRight) {
  //         std::string newStr = curr + s[i + rIndex + 1];
          
  //         if (isPalindrome(newStr)) {
  //           rIndex++;
  //           curr = newStr;
  //           continue;
  //         }
  //       } else {
  //         break;
  //       }
  //     }

  //     if (curr.length() > longest.length()) {
  //       longest = curr;
  //     }
  //   }

  //   return longest;
  // }
};

int main() {
  std::string answer = Solution::longestPalindrome("cbbd");
  std::cout << answer << "\n";
}