class PrimeSieve:

    def __init__(self, n):

        self.n = n

        self.primes = []

        self.sieve = [True] * (n + 1)

        self.sieve[0] = self.sieve[1] = False

    def run(self):

        for i in range(2, int(self.n ** 0.5) + 1):

            if self.sieve[i]:

                for j in range(i * i, self.n + 1, i):

                    self.sieve[j] = False

        for i in range(2, self.n + 1):

            if self.sieve[i]:

                self.primes.append(i)
