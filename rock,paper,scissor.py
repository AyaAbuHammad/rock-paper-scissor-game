import tkinter as tk
import random

window = tk.Tk()
window.geometry('400x300')
window.title('Rock Paper Scissor game')

USER_SCORE = 0
COMPUTER_SCORE = 0
USER_CHOICE = ''
COMPUTER_CHOICE = ''

def choice_to_number(choice):
    rps={'rock':0,'paper':1,'scissor':2}
    return rps[choice] #to return 0 or 1 or 2


def random_computer_choice():
    return random.choice(['rock','paper','scissor'])


def result(human_choice,computer_choice):
    global USER_SCORE
    global COMPUTER_SCORE
    user = choice_to_number(human_choice)
    computer = choice_to_number(COMPUTER_CHOICE)
    if user == computer:
        print('Tie!,no one wins')
    elif ((user-computer) %3 == 1):
        print('You win')
        USER_SCORE+=1
    else:
        print('Computer wins')
        COMPUTER_SCORE+=1
    
    text_area = tk.Text(master=window, height=12, width=30, bg='#FFFF99')
    text_area.grid(row=4, column=0)
    answer = 'Your choice: {uc} \n Computer choice: {cc} \n Your score: {us} \n Computer score: {cs}'.format(uc=USER_CHOICE,cc=COMPUTER_CHOICE,us=USER_SCORE,cs=COMPUTER_SCORE)
    text_area.insert(tk.END, answer)



def rock():
    global USER_CHOICE
    global COMPUTER_CHOICE
    USER_CHOICE = 'rock'
    COMPUTER_CHOICE = random_computer_choice()
    result(USER_CHOICE,COMPUTER_CHOICE)

def paper():
    global USER_CHOICE
    global COMPUTER_CHOICE
    USER_CHOICE = 'paper'
    COMPUTER_CHOICE = random_computer_choice()
    result(USER_CHOICE,COMPUTER_CHOICE)

def scissor():
    global USER_CHOICE
    global COMPUTER_CHOICE
    USER_CHOICE = 'scissor'
    COMPUTER_CHOICE = random_computer_choice()
    result(USER_CHOICE,COMPUTER_CHOICE)


button1 = tk.Button(text='Rock', bg='skyblue', command=rock)
button1.grid(row=1, column=0)

button2 = tk.Button(text='Paper', bg='pink', command=paper)
button2.grid(row=2, column=0)

button3 = tk.Button(text='Scissor', bg='lightgreen', command=scissor)
button3.grid(row=3, column=0)

window.mainloop()
