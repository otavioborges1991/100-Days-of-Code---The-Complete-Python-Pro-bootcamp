
from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain
import os

def clear():
    platform = os.name
    if platform == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    # fill the question bank with the question in data file
    question_bank = []
    for question in question_data:
        question_text = question['text']
        question_answer = question['answer']
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    # making the questions
    quiz = QuizzBrain(question_bank)

    # starting the game
    while quiz.still_has_questions():
        clear()
        quiz.next_question()
        
if __name__ == '__main__':
    main()