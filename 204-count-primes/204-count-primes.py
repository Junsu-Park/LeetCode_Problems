class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n==1:
            return 0
        
        primes = [1 for _ in range(n+1)]
        primes[0], primes[1], primes[-1] = 0, 0, 0
        max_iter=int(n**0.5) + 1
        for i in range(2, max_iter):
            if not primes[i]:continue
            j = i
            for j in range(2, n//i + 1):
                primes[i*j] = 0
        return sum(primes)