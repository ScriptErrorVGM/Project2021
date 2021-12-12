def main():
    def maxNum(a,b,c):
        tmp = a
        if b > tmp:
            tmp = b
        if c > tmp:
            tmp = c
        print(tmp) 

    maxNum(1,10,3)
    print(max(*[ 1, 10, 3]))

if __name__ == "__main__":
    main()    