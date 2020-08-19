# 77. Combinations
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        
        def backtrack(first = 1, curr= [ ]):
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n+1):
                curr.append(i)
                backtrack(i+1, curr)
                curr.pop()
               
        backtrack()
        
        return output
