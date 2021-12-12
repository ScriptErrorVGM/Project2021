def main():
    def numSqaure(num):
        return num**2

    def numSqaure1(num):
        print('Квадрат числа равен: ' + str(num**2))
    
    def numSqaure2(num):
        print('Квадрат числа равен: ' + str(num**2))
        return num**2
    
    userInput = int(input())
    print(numSqaure(userInput))
    print(numSqaure1(userInput))
    print(numSqaure2(userInput))


if __name__ == "__main__":
    main()