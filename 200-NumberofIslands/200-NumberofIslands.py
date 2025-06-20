# Last updated: 6/20/2025, 1:02:28 PM
"""
given a map of 1s and 0s return the number of islands 
we go through the grid and we have a queue 
we append values to the queue only when we find a 1 
then we go by level and everytime a level completes it means we've found an island and we return that value 
"""
class Solution:
    def bfs(self,grid,visited,r,c,ctr):
        rows = len(grid)
        cols = len(grid[0])
        neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
        queue = [] # [(1,1)]
        queue.append((r,c))
        while len(queue) != 0:
            l = len(queue) #2
            for _ in range(l):
                var = queue.pop(0) 
                for x,y in neighbors:
                    newx = x + var[0]
                    newy = y + var[1]
                    if newx>=0 and newy>=0 and newx<rows and newy<cols:
                        if grid[newx][newy] == '1' and visited[newx][newy] == False:
                            queue.append((newx,newy)) #
                            visited[newx][newy] = True
                        elif grid[newx][newy] == '0' and visited[newx][newy] == False:
                            visited[newx][newy] = True
        return ctr+1


    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = []
        ctr = 0
        for r in range(rows):
            row = [False]*cols
            visited.append(row)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and visited[r][c] == False:#(0,0)
                    visited[r][c] = True
                    ctr = self.bfs(grid,visited,r,c,ctr)
                    
        return ctr 

        


        