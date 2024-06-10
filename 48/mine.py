from typing import List

class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
    q = []
    n = len(matrix)
    temp = []

    for j in range(n-1):
      for i in range(j, n-j-1):

        #top row to right col
        temp.append(matrix[i][n-j-1])
        matrix[i][n-j-1] = matrix[j][i]

        #right col to last row
        temp.append(matrix[n-j-1][n-i-1])
        matrix[n-j-1][n-i-1] = temp.pop(0)

        #bot row to left col
        temp.append(matrix[n-1-i][j])
        matrix[n-i-1][j] = temp.pop(0)

        #left col to first row
        # temp.append(matrix[0][i])
        matrix[j][i] = temp.pop(0)
    
    print("done")

    # for i in range(n):
    #   q.append(matrix[i][n-1])
    #   matrix[i][n-1] = matrix[0][i]
    
    # for i in range(n):
    #   q.append(matrix[n-1][n-i-1])
    #   matrix[n-1][n-i-1] = q.pop(0)
    
    # for i in range(n)

m = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
sol = Solution()
sol.rotate(m)

print(m)