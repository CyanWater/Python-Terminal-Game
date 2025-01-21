class Question:
    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer

    def check_answer(self, user_answer: str):
        return user_answer.strip().lower() == self.answer.strip().lower()