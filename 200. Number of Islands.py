#!/usr/bin/env python

################################################################################
# @Author Wei-Ming Chen, PhD                                                   #
# @200. Number of Islands                                                      #
# @version: v1.0.0                                                             #
################################################################################

'''
URL: https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
    Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    Output: 1

Example 2:
    Input: grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    Output: 3

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
'''

import time

class Solution:
    def numIslands(grid):

        def bfs(r, c, h , w, grid, d = [[0,1],[1,0],[0,-1],[-1,0]]):
            if  r >= 0 and c >= 0 and r < h and c < w:
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    for dr, dc in d: bfs(r+dr, c+dc, h, w, grid)
                return 1
            return

        h, w = len(grid), len(grid[0])
        island = 0
        for r in range(h):
            for c in range(w):
                if grid[r][c] == '1':
                    island += bfs(r, c, h, w, grid)

        return island

''' main() '''
# Runtime: faster than 89.41% of Python3 online submissions
# Memory Usage: less than 80.47% of Python3 online submissions

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

start_time = time.time()
print("Output:", Solution.numIslands(grid), )
print("Runtime: %6f sec:" % (time.time() - start_time))
