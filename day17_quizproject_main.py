
from day17_QuizProject import Question
from day17_quizproject_data import question_data
from day17_quizproject_brain import QuizBrain


question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]

    new_question = Question(question_text, question_answer)

    # -----make it more easier format --------

    # new_question = Question(question=["text"], question=["answer"])
    question_bank.append(new_question)


# print(question_bank[0])
# print(question_bank[0]["text"])  #  This tries to use the object like a dictionary . we can not retrive anything from a object like dictionary .
# print(question_bank[0].question)   #here (.text) will not work because of you declare the construction as a attribute -- question 

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You completed the quiz successfully.")
print(f"Your final score was = {quiz.score}/{quiz.question_number}")


