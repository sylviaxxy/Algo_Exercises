# LC 72.Edit Distance

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        
        if m * n == 0:
            return m + n
        
        # array to store the convertion history
        d = [[0 for j in range(n + 1)] for i in range(m + 1)]
        
        # initial boundry
        for i in range(m + 1):
            d[i][0] = i
        for j in range(n + 1):
            d[0][j] = j
            
        # DP compute
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                left = d[i - 1][j] + 1
                down = d[i][j - 1] + 1
                left_down = d[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                d[i][j] = min(left, down, left_down)
        
        return d[m][n]