def main():
    def sortList(*args):
        sList = list(args)
        sList.sort()
        return sList

    print(sortList(7, 6, 1, 3, 8, 0, -2))

if __name__ == "__main__":
    main()    