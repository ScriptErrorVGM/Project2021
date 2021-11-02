from time import *
import csv
import threading
import os

def main():
    with open('problems1.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        totalQuestions = 0
        correctAnswers = 0
        quizTime = 15

        def answersInfo():
            print(str(correctAnswers) + '/' + str(totalQuestions))
            print('Время выполнения : ' + str(quizTime - myTimer) + ' секунд.')
            print('Оставшееся время ' + str(myTimer))

        def countdown():
            global myTimer

            myTimer = quizTime

            for x in range(myTimer):
                myTimer = myTimer - 1
                sleep(1)
            print()
            print('Out of time')
            answersInfo()
            os._exit(0)

        print('Время на выпонение теста ' + str(quizTime) + ' секунд')
        countdownThread = threading.Thread(target = countdown, daemon = True)

        countdownThread.start() 
        
        while myTimer > 0:
            for row in spamreader:
                question, answer = row[0].split(';')
                totalQuestions += 1
                
                userInput = input(question + ' ')
                if userInput == answer:
                    correctAnswers += 1 
            break
        answersInfo()
if __name__ == "__main__":
    main()