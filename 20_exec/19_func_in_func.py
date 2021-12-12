def main():
        def foo(a):
                def foo2(b):
                        nonlocal a
                        a = (a + 3) * b
                        return a+b
                return foo2

        func = foo(4)
        print(func(4))

if __name__ == "__main__":
    main()        