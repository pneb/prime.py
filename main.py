from utils.prime import PrimeSieve

def main():

    n = int(input("Enter a number: "))

    sieve = PrimeSieve(n)

    sieve.run()

    print(sieve.primes)

if __name__ == "__main__":

    main()
