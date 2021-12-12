import math

def main():
    def logList(numList):
        for i in range(len(numList)):
            if numList[i] > 0:
                    numList[i] = math.log(numList[i])
            else:
                numList[i] = None

        return numList
    
    numList = [1, 3, 2.5, -1, 9, 0, 2.71]
    print(logList(numList))

if __name__ == "__main__":
    main()