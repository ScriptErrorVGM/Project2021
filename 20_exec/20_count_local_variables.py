def main():
    def foo():
        a = 1
        b = 2
        c = 3 

    print(foo.__code__.co_nlocals)

if __name__ == "__main__":
    main()