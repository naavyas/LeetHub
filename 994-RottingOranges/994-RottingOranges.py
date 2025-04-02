# Last updated: 4/2/2025, 1:18:48 PM
"""
neighbors : no diagonals
every minute - once we find a rotten orange if we see that any of the neighbors are fresh oranges then those also become rotten 
2 - rotten 
1 - fresh 
0 - empty 
basically min time in which all fresh oranges can be made rotten and then of suppose then -1 
bfs : 
considering the board at one time 
timer : minute 
i'll keep all the rotten orange to my queue 
then i'll call my bfs 
visited : array 
ctr : basicallky compares original fresh oranges to final number after conversion 

Time : O(N*M) 
Space : O(N*M)
[(0,1),(1,0)]
var = (0,0)
minutes = 2
original_fresh = 6
[[2,1,1],
[0,1,1],
[1,0,1]]
queue = []
newx = 
"""
class Solution:
    def convertFresh(self, grid,visited,queue,original_fresh,minutes):
        neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
        rows = len(grid)
        cols = len(grid[0])
        while len(queue) != 0:
            n = len(queue) # how many rotten to fresh
            minutes += 1
            for _ in range(n):
                var = queue.pop(0)
                for x,y in neighbors:
                    newx = x + var[0]
                    newy = y + var[1]
                    if newx>=0 and newy>=0 and newx<rows and newy<cols:
                        if grid[newx][newy] == 1 and visited[newx][newy] == False:
                            grid[newx][newy] = 2
                            queue.append((newx,newy))
                            visited[newx][newy] = True
                            original_fresh -= 1
        return [minutes,original_fresh]



    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = []
        for r in range(rows):
            row = [False]*cols
            visited.append(row)
        original_fresh = 0 # keeps tracks of how many fresh oranges we have to convert
        queue = []
        minutes = -1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2 and visited[r][c] == False:
                    queue.append((r,c))
                    visited[r][c] = True
                if grid[r][c] == 1 and visited[r][c] == False:
                    original_fresh += 1 
        
        #add all the rotten oranges into the queue 
        if original_fresh != 0:
            output_values = self.convertFresh(grid,visited,queue,original_fresh,minutes)
            if output_values[1] == 0:
                return output_values[0]
            else:
                return -1 
        else:
            return 0 





        