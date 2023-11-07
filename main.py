questions = [
    [
        "Which of the following is the first calculating device?",
        "Abacus",
        "Calculator",
        "Turing",
        "Machine",
        1,
    ],
    [
        "Who invented mechanical calculator called Pascaline?",
        "Charles Babbage",
        "Blaise Pascal",
        "Alan Turing",
        "Lee De Forest",
        2,
    ],
    [
        "Who among the following considered as the 'father of artificial intelligence'?",
        "Charles Babbage",
        "Lee De Forest",
        "John McCarthy",
        "JP Eckert",
        3,
    ],
    [
        "Which was the world's first successful electronic computer?",
        "PARAM",
        "CRAY-1",
        "Pascaline",
        "ENIAC electronic " "Numerical Integrator and computer",
        4,
    ],
    [
        "Select the example of application software of computer:",
        "Ms Word",
        "Ms Excel",
        "Both A and B",
        "MS-DOS",
        3,
    ],
    [
        "Which of the following is also called translator?",
        "Data representation",
        "MS - DOS",
        "OperatingSystem",
        "Language Processor",
        4,
    ],
    [
        "How the quality of printer is measured?",
        "Alphabet per strike",
        "Words per Inch",
        "Strike per Inch",
        "Dots per Inch",
        4,
    ],
    [
        "Google is a Browser or a Search Engine?",
        "Browser",
        "Search Engine",
        "Both Browser and Search Engine",
        "Neither Browser nor Search Engine",
        2,
    ],
    [
        "Who is the founder of Facebook?",
        "Andrew Maclin",
        "Mark Zuckerberg",
        "None of the above mentioned",
        "Mark Adon",
        4,
    ],
    [
        "All mathematical and logical functions in the computer are done by?",
        "Central Processing Unit",
        "Control Unit",
        "Arithmetic and Logical Unit",
        "Memory Unit",
        3,
    ],
]

levels = [1000, 2000, 30000, 50000, 100000, 120000, 320000, 1000000, 5000000, 10000000]
money = 0
for i in range(len(questions)):
    question = questions[i]
    print(question[0])
    print(f"A.{question[1]}                              B.{question[2]}")
    print(f"C.{question[3]}                              D.{question[4]}")
    reply = int(input("Enter value between (1-4): "))
    print("\n")
    if not (reply == question[-1]):
        print("Wrong Answer. You lost!")
        break
    if i == 1:
        money = levels[i]
    elif i == 5:
        money = levels[5]
    elif i == 7:
        money = levels[7]
    elif i == 9:
        money = levels[9]
print("Your total money is: ", money)
