def main():
    def isPrime(n):
        if not n < 0 :
            if n == 1:
                return False
            if n % 2 == 0:
                return n == 2 and n > 0
            d = 3
            while d * d <= n and n % d != 0:
                d += 2
            return d * d > n
        else:
            return False

    print(isPrime(-1))
    print(isPrime(1))
    print(isPrime(11))

if __name__ == "__main__":
    main()  
