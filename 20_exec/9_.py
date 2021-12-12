def main():
    def isPrime(n):
        if n == 1:
            return False
        if n % 2 == 0:
            return n == 2
        d = 3
        while d * d <= n and n % d != 0:
            d += 2
        return d * d > n

    print(isPrime(2))
    print(isPrime(6))

if __name__ == "__main__":
    main()    
