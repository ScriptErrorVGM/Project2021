def main():
    def up_low(s):      
        u = sum(1 for i in s if i.isupper())
        l = sum(1 for i in s if i.islower())
        print(s)
        print( "No. of Upper case characters : %s ,No. of Lower case characters : %s" % (u,l))

    up_low("Быстрая Лиса Бровей")

if __name__ == "__main__":
    main()    