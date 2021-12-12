from os import name


def main():
    def compareLen(name , age):
        newDict = {}
        if range(len(name)) == range(len(age)) :
            for i in range(len(name)):
                newDict[name[i]] = age[i]  
        else:
            print("Списки имеют разную длину")
            return newDict
        return newDict        

    name = ["Ann", "Tim", "Sam"]
    age = [12, 23, 17]
    print(compareLen(name,age))

    name = ["Ann", "Tim", "Sam"]
    age = [12, 23, 17, 45]
    print(compareLen(name,age))    

if __name__ == "__main__":
    main()