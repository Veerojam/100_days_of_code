from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    quiz = Question(q["text"],q["answer"])
    question_bank.append(quiz)


quiz = QuizBrain(question_bank)

continue_with_quiz = True

while quiz.still_has_questions():
        quiz.next_question()
        quiz.check_answer()

print("You've completed the quiz, congrats!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")