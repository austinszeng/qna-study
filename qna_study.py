import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print('Welcome to QnA Study!')
input('(Press enter to continue...)')

playing = True
options = ['y', 'n']

while playing:
    ##### Reading questions and answers from qna.txt #####
    score = 0
    questions = []
    answers = []
    with open('qna.txt') as f:
        for line in f:
            if not line.strip(): # check for blank line
                break
            questions.append(line.rstrip())
        for line in f:
            answers.append(line.rstrip())

    ##### Questions #####
    i = 0
    user_answers = []
    right_or_wrong = []
    while i < len(questions):
        clear()
        answer = input(questions[i] + " ")
        if answer.lower() == answers[i].lstrip('1234567890. ').lower():
            # print()
            # input('Correct!')
            score += 1
            user_answers.append(answer)
            right_or_wrong.append(True)
        elif answer.lower() == 'q':
            for j in range(i, len(questions)):
                user_answers.append('None')
                right_or_wrong.append(False)
            break
        elif answer.lower() == 's':
            i += 1
            user_answers.append('None')
            right_or_wrong.append(False)
            continue
        else:
            # print()
            # input('Incorrect...')
            user_answers.append(answer)
            right_or_wrong.append(False)
        i += 1

    ##### Score #####
    clear()
    if ((score / len(questions)) * 100).is_integer():
        print('Percent: ' + str(int(((score / len(questions)) * 100))) + "%")
    else:
     print('Percent: ' + str(round(((score / len(questions)) * 100), 1)) + "%")
    print('You got ' + str(score) + "/ " + str(len(questions)) + " questions correct!")

    ##### Review #####
    valid_input = False
    while valid_input != True:
        review_yn = input('Would you like to review your answers (y/n)? ')
        if review_yn in options:
            valid_input = True
        else:
            print()
            input('Please input either "y" or "n"...')
            clear()
    clear()
    if review_yn == 'y':
        i = 0
        while i < len(questions):
            if right_or_wrong[i] == True:
                print('  ' + questions[i] + ' ' + user_answers[i])
            else:
                print('x ' + questions[i] + ' ' + user_answers[i] + ' [' + answers[i].lstrip('1234567890. ') + ']' )
            i += 1
        input('(Press enter to continue...)')

    ##### Retry ####
    clear()
    valid_input = False
    while valid_input != True:
        retry_yn = input('Would you like to retry (y/n)? ')
        if retry_yn in options:
            valid_input = True
        else:
            print()
            input('Please input either "y" or "n"...')
            clear()
    clear()
    if retry_yn != 'y':
        print('Thanks for using QnA Study!')
        input('(Press enter to quit...)')
        playing = False
        quit()