def main():
    numbers = [1, 2, 2, 3, 3, 4, 5]
    #unique_numbers = list(set(numbers))
    #print(unique_numbers)
    def uniqueNumbers(numbers):
        list_of_unique_numbers = []
        unique_numbers = set(numbers)

        for number in unique_numbers:
            list_of_unique_numbers.append(number)

        return list_of_unique_numbers

    print(uniqueNumbers(numbers))

if __name__ == "__main__":
    main()    