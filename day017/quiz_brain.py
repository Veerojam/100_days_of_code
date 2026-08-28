

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0


    def still_has_questions(self):
        return self.question_number < len(self.question_list)


        
    def next_question(self):
        self.current_quiz = self.question_list[self.question_number]
        self.question_number += 1
        self.answer = input(f"Q.{self.question_number}: {self.current_quiz.text} (True/False)? ").capitalize()

    

    def check_answer(self):
        if self.answer == self.current_quiz.answer:
           self.score += 1
           print("You got it right!")
        else:
           print("Womp womp! Your answer was wrong.")

        print(f"Your current score is {self.score}/{self.question_number}.")
        print("\n")


