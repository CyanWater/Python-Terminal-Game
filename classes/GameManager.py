import random

from classes.Question import Question

class GameManager:
    def __init__(self, questions):
        if not all(isinstance(question, Question) for question in questions):
            raise TypeError("All elements in questions must be instances of the Question class.")
        
        self.questions = questions
        self.asked_questions = set()

    def choose_next_question(self) -> Question:
        if not self.questions:
            raise ValueError("No questions available.")
        
        remaining_questions = [question for question in self.questions if question not in self.asked_questions]

        if not remaining_questions:
            raise ValueError("All questions have been asked.")

        next_question = random.choice(remaining_questions)
        self.asked_questions.add(next_question)
        return next_question
