# Last updated: 3/29/2025, 4:41:36 PM
"""
understanding the question 
0 - empty 
1 - fresh 
2 - rotten orange 
1 --- > 2 every minute if it is a neighbour 
return the min no of minutes till all the oranges becomes rotten 
Break it down: 
If we see a cell with 0 - ignore 
if we see a cell with 1 - check the neighbors to see if you can find a rotten orrange 
if we find a rotten orange then we should chnage all the nighbors to rotten that are currently fresh and increment the time counter by 1
everytime u make this change increment the minutes timmer by 1
- dont keep a visited 
- before making a chnage just check to make sure that the orange is not rotten 
-------------------------------
"""
class Solution:  
    def bfs(self,grid,queue,ctr_changed):
        counter = ctr_changed
        timer = 0
        rows = len(grid)
        #queue = [(2,2)]
        #ctr_changed = 1
        cols = len(grid[0])
        neighbors = [(1,0),(0,1),(0,-1),(-1,0)]
        while len(queue) != 0:
            l = len(queue) #1
            timer += 1 #3
            for _ in range(l):
                var = queue.pop(0)
                for x,y in neighbors:
                    newx = x + var[0]
                    newy = y + var[1]
                    if newx>=0 and newy>=0 and newx<rows and newy<cols:
                        if grid[newx][newy] == 1:
                            counter -= 1
                            grid[newx][newy] = 2
                            queue.append((newx,newy))
        
        return [timer,counter]




    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ctr_fresh = 0
        queue = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    ctr_fresh += 1
        ctr_changed = ctr_fresh
        if len(queue) == 0 and ctr_fresh ==0:
            return 0
        elif len(queue) == 0:
            return -1 

        n = self.bfs(grid,queue,ctr_changed)
        if n[1]!=0:
            return -1
        return n[0]-1
                    
        #go through the whole grid 
        #find the twos and append to a queue
        #then start the bfs process 
        #keep a counter to keep track of the number of 1s there were initially and if they all have been converted and then return the timer 

        #timer increments using the level logic 

        

        return timer

            


        