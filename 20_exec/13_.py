def main():
    def pascalTriangle(r):
        r1 = [1]
        for i in range(r):
            print(r1)
            r1 = [sum(x) for x in zip([0] + r1, r1 + [0])]

    pascalTriangle(10)

if __name__ == "__main__":
    main()    