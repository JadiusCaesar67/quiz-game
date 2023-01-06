from time import *
print("Welcome to Jade's QUIZ GAME!")
sleep(1)
print("This quiz is composed of multiple choices and true or false that has the basic topics related to Software Engineering\n"
    "Answer accordingly and if you made a mistake learn from your it. Good luck!")
sleep(3)
input("Press enter to start the Quiz Game\n")
questions = ["What are the two ways of mode to write your python program?",
             "A named location used to store data in the memory.",
             "True or False... We cannot use a keyword as a variable name, function name or any other identifier. They are "
             "used to define the syntax and structure of the Python language.",
             "Every value in Python has a/an?",
             "True or False... Declaring a Python list are enclosed within braces {  }.",
             "Unordered collection of unique items and defined by values separated by comma inside braces { }.",
             "An ordered sequence of items same as a list, but are immutable and once created cannot be modified; it is defined within parentheses ( )",
             "It is a sequence of Unicode characters which can be used to single quotes or double quotes to represent strings.",
             "True or False... Variables are used to perform mathematical operations like addition, subtraction, multiplication, etc.",
             "True or False... Loops are used to compare values to return to either True or False according to the condition",]

answer_choices = ["a)print and interactive \nb)interactive and script\nc)print and script\nd)None of the above\n:",
                  "a)Print\nb)Concatination\nc)Variable\nd)Data Type\n:",
                  ":",
                  "a)Data Type\nb)Integer\nc)Floating Point\nd)Complex Number\n:",
                  ":",
                  "a)List  \nb)Tuple\nc)String\nd)Set\n:",
                  "a)List  \nb)Tuple\nc)String\nd)Set\n:",
                  "a)List  \nb)Tuple\nc)String\nd)Set\n:",
                  ":",
                  ":",]

correct_choices = [{"b", "interactive and script"},
                   {"c", "Variable"},
                   {"true", "t"},
                   {"a", "Data Type"},
                   {"false", "f"},
                   {"d", "set"},
                   {"b", "tuple"},
                   {"c", "string"},
                   {"false", "f"},
                   {"false", "f"},]

answers = ["interactive and script",
           "c) variable",
           "true",
           "a) data type",
           "enclosed within brackets [ ]",
           "d) set",
           "b) tuple",
           "a string",
           "arithmetic operators",
           "comparison operators",]

def quiz():
    score = 0
    for question, choices, correct_choice, answer in zip(questions, answer_choices, correct_choices, answers):
        print(question)
        user_answer = input(choices)
        if user_answer.lower() in correct_choice:
            print("Correct")
            score += 1
        else:
            print("Incorrect\n That should be", answer)
    print("You've got", score, "out of", len(questions), "That is", float(score / len(questions)) * 100, "%")

#if __name__ == "__main__":
quiz()