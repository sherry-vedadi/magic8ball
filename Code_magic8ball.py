import random, csv, sys

class magic8ball:

    def __init__(self, name):
        self.__name = name
        self.__mQuestion = []

        self.__start_game()

    def __start_game(self):
        mResponse = ["As I see it, yes", "You may relay on it", "Ask again later",
                     "Cannot predict now", "Don't count on it",
                     "It is decidedly so", "It is certain", "Most likely"]

        lQuestions = True

        print("Welcome " + self.__name)

        while lQuestions:
            mQues = input("Please Enter a Question:")

            mRespond = mResponse[random.randint(0,7)]

            if mQues == "":
                print("Thank you for playing")

                self.__write_questions()

                sys.exit()
            else:
                print(mRespond)
                
                self.__mQuestion.append(mQues)

    def __write_questions(self):
        f = open("magic_questions.csv", "a", newline="")

        wrt = csv.writer(f)

        for q in self.__mQuestion:
            wrt.writerow([q])

        f.close()
            
