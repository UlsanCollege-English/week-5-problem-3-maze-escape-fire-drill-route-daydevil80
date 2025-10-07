from collections import deque

def find_path(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    sx, sy = start
    gx, gy = goal

    # Check bounds
    if not (0 <= sx < rows and 0 <= sy < cols):
        return None
    if not (0 <= gx < rows and 0 <= gy < cols):
        return None

    # Check start or goal blocked
    if grid[sx][sy] == 1 or grid[gx][gy] == 1:
        return None

    visited = set()

    def backtrack(r, c):
        if not (0 <= r < rows and 0 <= c < cols):
            return None
        if grid[r][c] == 1 or (r, c) in visited:
            return None
        if (r, c) == goal:
            return [(r, c)]

        visited.add((r, c))

        # try all 4 directions
        for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            path = backtrack(r+dr, c+dc)
            if path:
                return [(r,c)] + path

        return None

    return backtrack(sx, sy)
