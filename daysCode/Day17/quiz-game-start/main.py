from question_model import Question
from data import question_data
from quiz_brain import Quiz_brain
import requests


# From Open Trivia API
api_url = "https://opentdb.com/api.php?amount=10&type=boolean"
response = requests.get(api_url)
questions = response.json()["results"]


question_bank = []
for q in questions:
    text = q["question"]
    answer = q["correct_answer"]
    question_bank.append(Question(text, answer))

#  Creation of quiz brain
quiz_brain = Quiz_brain(question_bank)

while quiz_brain.still_has_question():  # if quiz still have questions remaining
    quiz_brain.next_question()
print("You've completed the quiz")
print(f"Your final score was {quiz_brain.score}/{quiz_brain.question_number}")
