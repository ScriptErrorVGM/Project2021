def main():
    def splitStr(string):
        temp = string.lower()
        res = temp.split(' ')
        return res

    string = 'В лесу родилась ёлочка В лесу она росла'
    print(splitStr(string))

if __name__ == "__main__":
    main()