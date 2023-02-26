from tkinter import *
from random import choice
from PIL import Image, ImageTk


def play(player, cpu):
    win_with = {"papier": "kamień",
                "kamień": "nożyce",
                "nożyce": "papier"}
    if player == cpu:
        return None
    elif win_with[player] == cpu:
        return True
    else:
        return False


def play_cmd(player):
    global text_label
    global player_score
    global cpu_score
    global scores_count
    global rounds_no
    global rounds_count
    cpu = choice(available_choices)
    is_user_winner = play(player, cpu)
    cpu_label.config(text=f"Komputer wybrał {cpu}")
    if is_user_winner is None:
        text_label.config(text="Remis")
    elif is_user_winner:
        text_label.config(text="Gracz wygrał")
        player_score += 1
    else:
        text_label.config(text="Komputer wygrał")
        cpu_score += 1
    scores_count.config(text=f"Gracz : {player_score} \nKomputer : {cpu_score}")
    rounds_no += 1
    rounds_count.config(text=f"{rounds_no}")


available_choices = ["papier", "nożyce", "kamień"]

player_score = 0
cpu_score = 0
rounds_no = 0

root = Tk()
root.resizable(width=False, height=False)
root.title("Papier-Nozyce-Kamien")

root.geometry("460x400")

scores = Label(root, text="Wynik", font=30, width=15,  fg="black")
scores.grid(row=0, column=1)


rounds = Label(root, text="Rozegrano rund: ", font=30, width=15, fg="red")
rounds.grid(row=0, column=3)

scores_count = Label(root, text="Gracz : 0 \nKomputer : 0", justify=LEFT)
scores_count.grid(row=1, column=1)

rounds_count = Label(root, text="0", font=30, fg="red")
rounds_count.grid(row=1, column=3)

paper_image = Image.open('paper.jpg')
paper_image = ImageTk.PhotoImage(paper_image)

paper = Button(root, image=paper_image, text="Papier", compound=TOP, command=lambda: play_cmd("papier"))
paper.grid(row=2, column=1)

scissors_image = Image.open('scissors.jpg')
scissors_image = ImageTk.PhotoImage(scissors_image)

scissors = Button(root, image=scissors_image, text="Nożyce", compound=TOP, command=lambda: play_cmd("nożyce"))
scissors.grid(row=2, column=2)

rock_image = Image.open('rock.jpg')
rock_image = ImageTk.PhotoImage(rock_image)

rock = Button(root, image=rock_image, text="Kamień", compound=TOP, command=lambda: play_cmd("kamień"))
rock.grid(row=2, column=3)

cpu_label = Label(root, text="", font=10, width=25, fg="blue")
cpu_label.grid(row=3, column=1, columnspan=3)

text_label = Label(root, text="Wybierz opcję", font=30, fg="blue")
text_label.grid(row=4, column=1, columnspan=3)

koniec = Button(root, text="Koniec", height=2, width=15, command=root.destroy)
koniec.grid(row=5, column=2)

root.mainloop()
