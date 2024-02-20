import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
    
        is_Prime = [True] * n
        is_Prime[0] = is_Prime[1] = False

        for i in range(2, math.ceil(math.sqrt(n))):
            if is_Prime[i]:
                for j in range(i*i, n, i):
                    is_Prime[j] = False
        
        return is_Prime.count(True)
        
sol = Solution()
print(sol.countPrimes(10))