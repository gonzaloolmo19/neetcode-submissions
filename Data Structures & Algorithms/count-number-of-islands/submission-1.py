class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [(1,0), (-1, 0), (0,1), (0,-1)]
        islands = 0
        def bfs(r,c):
            queue = deque()
            grid[r][c] = "0"
            queue.append((r,c))

            while queue:
                r,c = queue.popleft()
                for dr, dc in direction:
                    nc = c +dc
                    nr = r +dr
                    if not (nc <0 or nr <0 or nc >= len(grid[0]) or nr >= len(grid) or grid[nr][nc] == "0"):
                        queue.append((nr,nc))
                        grid[nr][nc] = "0"
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands+=1
        
        return islands
                       
                    


        