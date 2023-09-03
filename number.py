from tkinter import *
import random

my_number = random.randint(1,99)
btn2 = None  
guess_num=None
attempts=10

def reset_game():
    global my_number
    global attempts
    my_number = random.randint(1, 99)
    attempts = 10
    guess_num.delete(0, 'end')
    quit_button.pack_forget()
    label.pack()
    guess_num.pack()
    check_button.pack()
    quit_button.pack()
    play_again_button.pack_forget()
    text.set("You have 10 attempts! Good Luck ")

def submit_name():
    global btn2  
    name = name_entry.get()
    welcome_label.config(text=f"Welcome, {name}!\n Rules: I think of a number between 1 to 100 and \nguess the number within 10 attempts")

    label.grid_forget()  
    name_entry.grid_forget()  
    submit_button.grid_forget()  

    btn2 = Button(root, text="Start Game", command=start_function)
    btn2.grid(row=3, column=1)

def start_function():
    global guess_num
    global btn2  

    btn2.grid_forget()
    welcome_label.grid_forget()

    global label
    label=Label(root, text="Guess a number between 1 to 100")
    label.pack()

    global guess_num
    guess_num=Entry(root,width="40",borderwidth="4")
    guess_num.pack()

    global check_button

    check_button=Button(root, text="Check", command=check_sum)
    check_button.pack()

    global quit_button

    quit_button=Button(root, text="Quit", command=root.destroy)
    quit_button.pack()
    
    global text
    text= StringVar()
    text.set("You have 10 attempts! Good Luck ")

    guess_attempts=Label(root, textvariable=text)
    guess_attempts.pack()
def check_sum():
    global guess_num
    global text
    global attempts
    global check_button
    guess=guess_num.get()
    guess=int(guess)

    attempts-=1
    
    if(my_number==guess):
        text.set("you win! Congrats!!!")
        check_button.pack_forget()
        play_again_button.pack() 
    elif attempts==0:
        text.set("You lose!!")
        check_button.pack_forget()
        guess_num.pack_forget()
        play_again_button.pack() 
    elif my_number > guess:
        text.set("Incorrect! Only "+str(attempts)+" attemps remaining! Your guess is too Low")
    elif my_number < guess:
        text.set("Incorrect! Only "+str(attempts)+" attemps remaining! Your guess is too High")
    

root = Tk()
root.title("Number Guessing Game")
root.geometry("500x150")

label = Label(root, text="Enter Your Name:")
label.grid(row=1, column=1, padx=10, pady=10)

name_entry = Entry(root)
name_entry.grid(row=1, column=2, padx=10, pady=10)

submit_button = Button(root, text="Submit", command=submit_name)
submit_button.grid(row=2, column=2, padx=10, pady=10)

welcome_label = Label(root, text="", font=("Helvetica", 16))
welcome_label.grid(row=2, columnspan=2, padx=10, pady=10)

play_again_button = Button(root, text="Play Again", command=reset_game)
play_again_button.pack_forget()

root.mainloop()
