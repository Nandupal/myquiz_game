import random

# Define questions and answers for different difficulty levels
questions = {
    'easy': [
        ("How many properties are their for OOPJ?", "7"),
        ("what is full form of ATM?", "Automated teller machine"),
        ("what is the shortcut key for copy?", "Ctrl+C")
    ],
    'medium': [
        ("Who wrote the National Anthem?", "Ravindranath Tagore"),
        ("What is the cude of 3?", "27"),
        ("What is the chemical formula of boron?", "B")
    ],
    'hard': [
        ("When the Telangana got the independence?", "1948"),
        ("Who is the IT minister of Telangana?", "Dr sundhar babu"),
        ("Which country is flat plateau?", "Malasiya")
    ]
}

def select_difficulty():
    print("Select the level to quiz: easy, medium, hard")
    while True:
        difficulty = input("Enter level to play quiz: ").lower()
        if difficulty in questions:
            return difficulty
        else:
            print("Incorrect difficulty level. Please choose again.")

def ask_question(question, answer):
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.strip().lower():
        return True
    else:
        return False

def quiz_game():
    print("Welcome to play Quiz Game!")
    score = 0
    difficulty = select_difficulty()
    question_set = random.sample(questions[difficulty], len(questions[difficulty]))
    
    for question, answer in question_set:
        if ask_question(question, answer):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {answer}.")
    
    print(f"Your final score is {score}/{len(question_set)}")

if __name__ == "__main__":
    quiz_game()
