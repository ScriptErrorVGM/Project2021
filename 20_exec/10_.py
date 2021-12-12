def main():
    def pEven(lst):
        return [x for x in lst if not x % 2]

    print(pEven(range(100)))
    print(pEven([1, 2, 3, 4, 5, 6, 7, 8, 9]))

if __name__ == "__main__":
    main()    