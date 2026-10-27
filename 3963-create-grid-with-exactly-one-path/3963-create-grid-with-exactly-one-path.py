class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        for i in range(m):
            if i == 0:
                # Top row is entirely free cells
                grid.append("." * n)
            else:
                # Other rows are obstacles until the very last column
                grid.append("#" * (n - 1) + ".")
        return grid