def main():
    c = input()
    if c != c[::-1]: # -1 шаг строки: от конца к началу
        print("It's not palindrome")
    else:
        print("It's palindrome")
    

if __name__ == "__main__":
    main()    