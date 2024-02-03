#include <string>
#include <iostream>

int getMaxBeautifulSubstrings(std::string color) {
    int total = 0;
    int cycleLength = 0;
    int cycleTotal = 0;
    
    for (int i = 0; i < color.length(); i++) {
        if (color[i] == '.') {
            int lAmt = 1;
            int rAmt = 1;
            
            if (i > 1) {
              char neighbour;
              int neighbourAmt = 0;
              int dotAmt = 0;
                for (int j = i-2; j >= 0; j--) {
                    if(color[j] == color[i - 1]) {
                        lAmt++;
                    } else if (color[j] != '.' && !neighbour) {
                      break;
                    } else if (!neighbour) {
                      neighbour = color[j];
                    } else if (color[j] == neighbour) {
                      neighbourAmt++;
                    } else {
                      break;
                    }
                }
            }
            
            if (i + 2 < color.length()) {
                for (int j = i + 2; j < color.length(); j++) {
                    if(color[j] == color[i + 1]) {
                        rAmt++;
                    } else {
                        break;
                    }
                }
            }
            
            if (lAmt > rAmt) {
                color[i] = color[i-1];
            } else {
                color[i] = color[i+1];
            }
            
        }
        
        
        if (i == 0) {
            cycleTotal = 1;
            cycleLength = 1;
            total = 1;
            continue;
        } 
        
        if (color[i] == color[i-1]) {
            cycleLength++;
            total += cycleTotal*cycleLength;
        } else {
            cycleLength = 1;
            cycleTotal = 1;
            total += 1;
        }
    }
    std::cout << color << std::endl;
    return total;
}

int main() {
  int result = getMaxBeautifulSubstrings("p.r."); 
  std::cout << result << std::endl;
  return 0;
}