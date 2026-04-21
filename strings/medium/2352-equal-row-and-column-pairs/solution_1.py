"""
2352. Equal Row and Column Pairs
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) 
such that row ri and column cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Example 1:
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

Constraints:
n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105
"""
class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        #  store the length of the given grid
        n = len(grid)

        # keeps track of number of row_col_pairs
        num_row_col_pairs = 0
        # stores the column values
        col_grid = []

        #  iterate the rows
        for i in range(n):
            #  column pair
            col_pair = []
            # iterate the columns
            for j in range(n):
                col_pair.append(grid[j][i])
            
            # append the columns 
            col_grid.append(col_pair)

        # iterate the grid
        for i in range(n):
            #  iterate the col_grid
            for j in range(n):
                #  compare each row with each column
                if grid[i] == col_grid[j]:
                    # increase the count by 1
                    #  for each equal row and column pair
                    num_row_col_pairs += 1


        return num_row_col_pairs
    
        
s = Solution()
print(s.equalPairs([[3,2,1],[1,7,6],[2,7,7]])) #1
