# Last updated: 3/29/2025, 12:20:22 AM
"""
you are given a mxn matrix 
empty : . 
wall: +
you are given the enterance of the maze which denotes ur initial pos in the grid 
you can move to any one of the neighbors 
find the nearest exit 
exit: an empty cell near the border 
return the number of steps in the shortest path from the enterace to the exit 
"""
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        visited = []
        queue = []
        for _ in range(rows):
            row = [False]*cols
            visited.append(row)
        r = entrance[0]
        c = entrance[1]
        #print((r,c))
        queue.append((r,c))
        visited[r][c] = True
        steps = 0
        neighbors = [(1,0), (0,1), (-1,0), (0,-1)]
        while len(queue)!=0:
            l = len(queue)
            steps += 1
            for r in range(l):
                var = queue.pop(0)
                for x,y in neighbors:
                    newx = x+var[0]
                    newy = y+var[1]
                    if newx>=0 and newy>=0 and newx<rows and newy<cols:
                        if ((newx == 0 or newx == rows-1) or (newy == 0 or newy == cols-1)) and maze[newx][newy] == '.' and visited[newx][newy] == False:
                                return steps
                        elif maze[newx][newy] == '.' and visited[newx][newy] == False:
                            queue.append((newx,newy))
                            visited[newx][newy] = True
                    
        return -1







        