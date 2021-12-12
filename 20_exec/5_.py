import math

def main():
    def factorial(n):
        if n == 0:
            return 1
        return factorial(n-1) * n
 
 
    print(factorial(4))
    print(math.factorial(4))


if __name__ == "__main__":
    main()    