def main():
    code = '''
    def test(a):
            def add(b):
                    nonlocal a
                    a += 1
                    return a+b
            return add

    func = test(4)
    print(func(4))
    '''
    exec(code) 

if __name__ == "__main__":
    main()