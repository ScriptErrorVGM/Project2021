def main():
    def reverseString(s):
        chars = list(s)
        for i in range(len(s) // 2):
            tmp = chars[i]
            chars[i] = chars[len(s) - i - 1]
            chars[len(s) - i - 1] = tmp
        return ''.join(chars)
 

    print(reverseString('1234abcd')) 
    print('1234abcd'[::-1]) 
    print(''.join(reversed('1234abcd')))

if __name__ == "__main__":
    main()    