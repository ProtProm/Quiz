import random

data = {
    "easy": {
        "question" :  '''
        The city councilmen refused the demonstrators a permit because they feared violence. (__1__) feared violence.
        The city councilmen refused the demonstrators a permit because they advocated violence. (__2__) advocated violence.
        Sam and Amy are passionately in love, but Amy's parents are unhappy about it. It is because (__3__) are snobs.
        Sam and Amy are passionately in love, but Amy's parents are unhappy about it. It is because (__4__) are fifteen.
        ''',
        "answer" : ["the city councilmen","the demonstrators","amy's parents","sam and amy"],
    },
    "medium": {
        "question" : '''
        John was doing research in the library when he heard a man humming and whistling. (__1__) was annoyed.
        John was doing research in the library when he heard a man humming and whistling. (__2__) was annoying.
        Mary took out her flute and played one of her favorite pieces. Mary has loved (__3__) since she was a child.
        Mary took out her flute and played one of her favorite pieces. Mary has had (__4__) since she was a child.
        ''',
        "answer" : ["john","the hummer","the piece","the flute"],
    },
    "hard": {
        "question" :  '''
        The city councilmen refused the demonstrators a permit because they feared violence. (__1__) feared violence.
        The city councilmen refused the demonstrators a permit because they advocated violence. (__2__) advocated violence.
        Sam and Amy are passionately in love, but Amy's parents are unhappy about it. It is because (__3__) are snobs.
        Sam and Amy are passionately in love, but Amy's parents are unhappy about it. It is because (__4__) are fifteen.
        ''',
        "answer" : ["joan","jane","the chatbots","the judges"],
    }
}

blanks_to_fill = ["__1__","__2__", "__3__", "__4__"]

print ('''

>>> WINOGRAD SCHEMAS CHALLENGE <<<

''')

lives = int(input("How many lives do you want? "))

def level_choice():
    level = input("Choose difficulty: easy, medium, hard or nothing: ").lower()
    if level == "easy":
        print (data[level]['question'])
        print ("Fill in the blanks.")
        return challenge(data[level]['question'], data[level]['answer'], lives)
    elif level == "medium":
        print (data[level]['question'])
        print ("Fill in the blanks.")
        return challenge(data[level]['question'], data[level]['answer'], lives)
    elif level == "hard":
        print (data[level]['question'])
        print ("Fill in the blanks.")
        return challenge(data[level]['question'], data[level]['answer'], lives)
    else:
        return "Well done anyways!"

def challenge(question, answer, lives):
    index = 0
    while index < len(answer):
        user_input = input("Write word to fill " + str(blanks_to_fill[index]) + " : ").lower()
        if user_input == answer[index]:
            question = question.replace(blanks_to_fill[index], answer[index])
            index += 1
            print (correct_guess(answer, question, index))
        elif user_input != answer[index]:
            if lives == 1:
                print( "0 lives left!")
                return level_choice()
            else:
                lives -= 1
                print( question)

def correct_guess(answer, question, index):
    if len(answer) == index:
        print ("\n" + question + "\n")
        print ("\n >>> PASSED. \n")
        user_again = input("Do you want to try another difficulty? Write: y/n ").lower()
        if user_again == "y":
            return level_choice()
        elif user_again == "n":
            return "Don't forget to come back if you change your mind."
        else:
            return "Well done anyways!"
    elif len(answer) != index:
        print ("\n CORRECT. Running next:")
        return question
    else:
        return "Well done anyways!"

print (level_choice())
