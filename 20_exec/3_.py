from functools import reduce

def main():
    def multiply(n):
        product = 1  
        for x in n:
            product *= x
        return product

    numbers = (8, 2, 3, -1, 7)
    print(multiply(numbers))
    print(reduce(lambda x, y: x*y, numbers))

if __name__ == "__main__":
    main()    