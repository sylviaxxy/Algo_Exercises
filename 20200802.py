# LC 799. Champagne Tower

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        f = [[0] * k for k in range(1, query_row + 2)] # f[i][j] is the total amount of water poured into glass[i][j]
        f[0][0]  = poured
        for i in range(query_row):
            for j in range(i + 1):
                remaining = f[i][j] - 1
                if remaining > 0:
                    f[i+1][j] += remaining / 2
                    f[i+1][j+1] += remaining / 2
                
        return min(1, f[query_row][query_glass])