from tkinter import *
import random

def roll_dice():
    try:
        num_of_dice = int(num.get())
        results = [random.randint(1, 6) for _ in range(num_of_dice)]
        result_label.config(text="Results: " + ", ".join(map(str, results)))
        roll_button.pack_forget()  # Hide the Roll button
        play_again_button.pack()  # Show the Play Again button
        quit_button.pack()  # Show the Quit button
    except ValueError:
        result_label.config(text="Please enter a valid number.")

def play_again():
    result_label.config(text="")
    num.delete(0, END)
    roll_button.pack()  # Show the Roll button
    play_again_button.pack_forget()  # Hide the Play Again button
    quit_button.pack_forget()  # Hide the Quit button


root = Tk()
root.title("Dice Roller")
root.geometry("900x200")

number_label = Label(root, text="Enter the number of dice to roll:")
number_label.pack()

num = Entry(root)
num.pack()

roll_button = Button(root, text="Roll", command=roll_dice)
roll_button.pack()

play_again_button = Button(root, text="Roll Again", command=play_again)
quit_button = Button(root, text="Quit", command=root.destroy)

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
