from classes.GameManager import GameManager
from questions import questions

GameManager = GameManager(questions)

while len(GameManager.asked_questions) < len(GameManager.questions):
    next_question = GameManager.choose_next_question()
    user_answer = input(next_question.question + " ")

    if next_question.check_answer(user_answer):
        print("That's correct.")
    else:
        print(f"That's incorrect, the answer is {next_question.answer}")

    print("=======================\n")