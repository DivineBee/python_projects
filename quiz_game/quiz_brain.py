class QuizBrain:
    def __init__(self, question_list):
        self.question_nr = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_nr < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_nr]
        self.question_nr += 1
        answer = input(f"Q.{self.question_nr}: {current_question.text}. (True/False)?: ")
        self.check_answer(answer, current_question.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("Right!")
            self.score += 1
        else:
            print("Wrong!")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_nr}\n")

