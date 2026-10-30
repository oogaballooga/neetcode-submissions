class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #initialize
        ROWS, COLS = len(grid), len(grid[0])
        freshRotten = set()
        rotten = set()
        reallyRotten = set()
        time = 0
        initFreshCount = 0

        # fill rotten set
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten.add((r, c))
                if grid[r][c] == 1:
                    initFreshCount += 1
                    
        if initFreshCount == 0:
            return 0

        def infect(r, c):
            # out of bounds base case
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return

            # victim base case
            if grid[r][c] == 1:
                grid[r][c] = 2
                freshRotten.add((r,c))
                
        while rotten:
            for (r, c) in rotten:
                infect(r+1, c)
                infect(r-1, c)
                infect(r, c+1)
                infect(r, c-1)
                reallyRotten.add((r, c))
            for rr in reallyRotten:
                rotten.remove(rr)
            for fr in freshRotten:
                rotten.add(fr)
            freshRotten.clear()
            reallyRotten.clear()
            time += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return time - 1