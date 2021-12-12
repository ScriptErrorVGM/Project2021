def main():
    def isPerfect(n):
        s = [j for j in range(1, n // 2 + 1) if not n % j]
        return sum(s) == n
    
    print(isPerfect(5))
    print(isPerfect(6))
    print(isPerfect(28))

if __name__ == "__main__":
    main()    