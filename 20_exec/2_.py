def main():
    def sumNum(n):
        s = 0  
        for x in n:
            s += x
        return s

    print(sumNum((8, 2, 3, 0, 7)))
    print(sum((8, 2, 3, 0, 7)))

if __name__ == "__main__":
    main()    