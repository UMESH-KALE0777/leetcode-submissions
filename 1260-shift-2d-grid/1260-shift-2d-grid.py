from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        Returns the grid after shifting it k times to the right.
        """
        m = len(grid)
        n = len(grid[0])
        total = m * n
        k %= total                     # effective shifts

        # 1. flatten the grid
        flat = [grid[i][j] for i in range(m) for j in range(n)]

        # 2. rotate right by k positions
        if k:
            rotated = flat[-k:] + flat[:-k]
        else:
            rotated = flat

        # 3. reshape back to m x n
        res = [rotated[i * n:(i + 1) * n] for i in range(m)]
        return res


# --------------------------------------------------------------
# Simple self‑test (the three examples from the statement)
if __name__ == "__main__":
    sol = Solution()

    g1 = [[1,2,3],[4,5,6],[7,8,9]]
    print(sol.shiftGrid(g1, 1))
    # -> [[9,1,2],[3,4,5],[6,7,8]]

    g2 = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
    print(sol.shiftGrid(g2, 4))
    # -> [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

    g3 = [[1,2,3],[4,5,6],[7,8,9]]
    print(sol.shiftGrid(g3, 9))
    # -> [[1,2,3],[4,5,6],[7,8,9]]