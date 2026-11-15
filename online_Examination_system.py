
# Online Examination System

# Store questions using a list of dictionaries

questions = [
    {
        "question": "Which language is used for Python programming?",
        "options": {
            "a": "HTML",
            "b": "Python",
            "c": "CSS",
            "d": "JavaScript"
        },
        "answer": "b"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {
            "a": "function",
            "b": "define",
            "c": "def",
            "d": "fun"
        },
        "answer": "c"
    },
    {
        "question": "Which data type stores multiple values in Python?",
        "options": {
            "a": "Integer",
            "b": "List",
            "c": "Float",
            "d": "String"
        },
        "answer": "b"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": {
            "a": "//",
            "b": "#",
            "c": "/*",
            "d": "%"
        },
        "answer": "b"
    },
    {
        "question": "Which function is used to display output?",
        "options": {
            "a": "input()",
            "b": "print()",
            "c": "output()",
            "d": "show()"
        },
        "answer": "b"
    }
]


# Function to conduct the examination
def conduct_exam():

    correct = 0
    wrong = 0
    skipped = 0

    print("\n===== ONLINE EXAMINATION SYSTEM =====")
    print("Total Questions: 5")
    print("Marks per Question: 2")
    print("Enter 's' to skip a question.")

    for i, q in enumerate(questions):

        print("\nQuestion", i + 1, ":", q["question"])

        for key, value in q["options"].items():
            print(key + ".", value)

        while True:
            answer = input("Enter your answer (a/b/c/d/s): ").lower().strip()

            if answer in ["a", "b", "c", "d", "s"]:
                break
            else:
                print("Invalid option. Enter a, b, c, d or s to skip.")

        if answer == "s":
            skipped += 1

        elif answer == q["answer"]:
            correct += 1

        else:
            wrong += 1

    return correct, wrong, skipped


# Function to calculate and display result
def calculate_result(correct, wrong, skipped):

    total_marks = 10
    score = correct * 2
    percentage = (score / total_marks) * 100

    print("\n========== EXAM RESULT ==========")
    print("Correct:", correct)
    print("Wrong:", wrong)
    print("Skipped:", skipped)
    print("Score:", score, "/", total_marks)
    print("Percentage: {:.2f}%".format(percentage))

    if percentage >= 40:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    print("=================================")


# Main program
correct, wrong, skipped = conduct_exam()

calculate_result(correct, wrong, skipped)
