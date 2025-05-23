

def true_or_false(msg):
        while True:
            answer = input(msg).lower().strip()
            if answer == 'y' or answer == 't':
                return True
            elif answer == 'n' or answer == 'f':
                return False
            else:
                print('Invalid answer, try again')

class QuizzBrain():
    
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.streak = 0
        self.user_answer = None
        self.current_question = None
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 100 * (self.streak + 1)
            self.streak += 1
            print('You got it right!')
        else:
            self.streak = 0
            print('That\'s wrong.')
        print(f'The correct answer was: {correct_answer}')
        input('Press enter to continue...')
        print('\n')

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        print(f'Your current score is {self.score}/{self.question_number}')
        print(f'Your current streak is {self.streak}')
        self.question_number += 1
        self.user_answer = true_or_false(f'Q.{self.question_number}: {self.current_question.text} (True/False): ')
        self.check_answer(self.user_answer, self.current_question.answer)


    