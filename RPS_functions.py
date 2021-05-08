import tkinter as tk
from PIL import ImageTk, Image
import random

def quickGame():
    global rImg
    global pImg
    global sImg
    global win1
    
    win1 = tk.Toplevel()
    win1.title("Quick Game")

    def picked(picks):
        global playerChoice
        global compChoice
        global AI_go
        global playerChoicePic
        global compChoicePic

        # Player choice
        playerChoice = Image.open(picks)
        newsize = (100, 100)# same for all
        playerChoice = playerChoice.resize(newsize)
        playerChoice = ImageTk.PhotoImage(playerChoice)
        playerChoicePic = tk.Label(win1, image=playerChoice)
        playerChoicePic.grid(column=0, row=2)
        # Computer choice
        x = random.choice(["rock.png", "paper.png", "scissors.png"])
        if x == "rock.png":
            AI_go = "r"
        elif x == "paper.png":
            AI_go = "p"
        elif x == "scissors.png":
            AI_go = "s"
        else:
            AI_go = "NONE"
        compChoice = Image.open(x)
        compChoice = compChoice.resize(newsize)
        compChoice = ImageTk.PhotoImage(compChoice)
        compChoicePic = tk.Label(win1, image=compChoice)
        compChoicePic.grid(column=2, row=2)
        
    global rbtn
    global pbtn
    global sbtn   
    def optionDisable():
        global rbtn
        global pbtn
        global sbtn
        rbtn["state"] = tk.DISABLED
        pbtn["state"] = tk.DISABLED
        sbtn["state"] = tk.DISABLED
    def optionEnable():
        global rbtn
        global pbtn
        global sbtn
        rbtn["state"] = tk.NORMAL
        pbtn["state"] = tk.NORMAL
        sbtn["state"] = tk.NORMAL
        
    # Player picks
    def pickR():
        global Player_go
        picked("rock.png")
        Player_go = "r"
        optionDisable()
        result()
    def pickP():
        global Player_go
        picked("paper.png")
        Player_go = "p"
        optionDisable()
        result()
    def pickS():
        global Player_go
        picked("scissors.png")
        Player_go = "s"
        optionDisable()
        result()

    # Play Again
    def replay():
        global playerChoicePic
        global compChoicePic
        global res
        
        res.destroy()
        playerChoicePic.destroy()
        compChoicePic.destroy()
        optionEnable()
        
    again = tk.Button(win1, text="Play Again", fg="White", bg="Blue", command=replay)
    again.grid(column=1, row=4)
    
    # Result
    def result():
        global res
        
        if (Player_go == "r" and AI_go == "s") or (Player_go == "p" and AI_go == "r") or (Player_go == "s" and AI_go == "p"):
            res = tk.Label(win1, text="WIN", font=("cursive", 60))
            res.grid(column=1, row=3)
        elif (Player_go == "r" and AI_go == "p") or (Player_go == "p" and AI_go == "s") or (Player_go == "s" and AI_go == "r"):
            res = tk.Label(win1, text="LOSE", font=("cursive", 60))
            res.grid(column=1, row=3)
        else:
            res = tk.Label(win1, text="DRAW", font=("cursive", 60))
            res.grid(column=1, row=3)
            
    # Rock
    rImg = Image.open("rock.png")
    newsize = (100, 100)# same for all
    rImg = rImg.resize(newsize)
    rImg = ImageTk.PhotoImage(rImg)
    rbtn = tk.Button(win1, image=rImg, text="1", bg="Black", command=pickR)
    rbtn.grid(column=0, row=0, padx=5, pady=10)

    # Paper
    pImg = Image.open("paper.png")
    pImg = pImg.resize(newsize)
    pImg = ImageTk.PhotoImage(pImg)
    pbtn = tk.Button(win1, image=pImg, text="2", bg="Black", command=pickP)
    pbtn.grid(column=1, row=0, padx=5, pady=10)

    # Scissors
    sImg = Image.open("scissors.png")
    sImg = sImg.resize(newsize)
    sImg = ImageTk.PhotoImage(sImg)
    sbtn = tk.Button(win1, image=sImg, text="3", bg="Black", command=pickS)
    sbtn.grid(column=2, row=0, padx=5, pady=10)

    # Name tags
    r = tk.Label(win1, text="^ ROCK ^")
    r.grid(column=0, row=1)
    p = tk.Label(win1, text="^ PAPER ^")
    p.grid(column=1, row=1)
    s = tk.Label(win1, text="^ SCISSORS ^")
    s.grid(column=2, row=1)
    
    # VS
    lbl = tk.Label(win1, text=" VS ", font=("Arial Bold", 60))
    lbl.grid(column=1, row=2)
    
    # Exit button
    eButton = tk.Button(win1, text="Exit", fg="White", bg="Red", command=win1.destroy)
    eButton.grid(column=1, row=5)

def marathon():
    win2 = tk.Toplevel()
    win2.title("RPS Marathon")

    lbl = tk.Label(win2, text="Coming Soon", font=("Arial", 60))
    lbl.grid(column=0, row=0)    

def tournament():
    global rImg
    global pImg
    global sImg
    global win1
    
    win1 = tk.Toplevel()
    win1.title("Best of 3 ~ RPS Tournament")

    def picked(picks):
        global playerChoice
        global compChoice
        global AI_go
        global playerChoicePic
        global compChoicePic

        # Player choice
        playerChoice = Image.open(picks)
        newsize = (100, 100)# same for all
        playerChoice = playerChoice.resize(newsize)
        playerChoice = ImageTk.PhotoImage(playerChoice)
        playerChoicePic = tk.Label(win1, image=playerChoice)
        playerChoicePic.grid(column=0, row=2)
        # Computer choice
        x = random.choice(["rock.png", "paper.png", "scissors.png"])
        if x == "rock.png":
            AI_go = "r"
        elif x == "paper.png":
            AI_go = "p"
        elif x == "scissors.png":
            AI_go = "s"
        else:
            AI_go = "NONE"
        compChoice = Image.open(x)
        compChoice = compChoice.resize(newsize)
        compChoice = ImageTk.PhotoImage(compChoice)
        compChoicePic = tk.Label(win1, image=compChoice)
        compChoicePic.grid(column=2, row=2)
        
    global rbtn
    global pbtn
    global sbtn   
    def optionDisable():
        global rbtn
        global pbtn
        global sbtn
        rbtn["state"] = tk.DISABLED
        pbtn["state"] = tk.DISABLED
        sbtn["state"] = tk.DISABLED
    def optionEnable():
        global rbtn
        global pbtn
        global sbtn
        rbtn["state"] = tk.NORMAL
        pbtn["state"] = tk.NORMAL
        sbtn["state"] = tk.NORMAL
    
    # Player picks
    def pickR():
        global Player_go
        picked("rock.png")
        Player_go = "r"
        optionDisable()
        result()
    def pickP():
        global Player_go
        picked("paper.png")
        Player_go = "p"
        optionDisable()
        result()
    def pickS():
        global Player_go
        picked("scissors.png")
        Player_go = "s"
        optionDisable()
        result()

    # Play Again
    def replay():
        global playerChoicePic
        global compChoicePic
        global res

        res.destroy()
        playerChoicePic.destroy()
        compChoicePic.destroy()
        optionEnable()
        
    again = tk.Button(win1, text="Play Again", fg="White", bg="Blue", command=replay)
    again.grid(column=1, row=4)
    
    # Result
    def result():
        global res
        
        if (Player_go == "r" and AI_go == "s") or (Player_go == "p" and AI_go == "r") or (Player_go == "s" and AI_go == "p"):
            res = tk.Label(win1, text="WIN", font=("cursive", 60))
            res.grid(column=1, row=3)
        elif (Player_go == "r" and AI_go == "p") or (Player_go == "p" and AI_go == "s") or (Player_go == "s" and AI_go == "r"):
            res = tk.Label(win1, text="LOSE", font=("cursive", 60))
            res.grid(column=1, row=3)
        else:
            res = tk.Label(win1, text="DRAW", font=("cursive", 60))
            res.grid(column=1, row=3)
            
    # Rock
    rImg = Image.open("rock.png")
    newsize = (100, 100)# same for all
    rImg = rImg.resize(newsize)
    rImg = ImageTk.PhotoImage(rImg)
    rbtn = tk.Button(win1, image=rImg, text="1", bg="Black", command=pickR)
    rbtn.grid(column=0, row=0, padx=5, pady=10)

    # Paper
    pImg = Image.open("paper.png")
    pImg = pImg.resize(newsize)
    pImg = ImageTk.PhotoImage(pImg)
    pbtn = tk.Button(win1, image=pImg, text="2", bg="Black", command=pickP)
    pbtn.grid(column=1, row=0, padx=5, pady=10)

    # Scissors
    sImg = Image.open("scissors.png")
    sImg = sImg.resize(newsize)
    sImg = ImageTk.PhotoImage(sImg)
    sbtn = tk.Button(win1, image=sImg, text="3", bg="Black", command=pickS)
    sbtn.grid(column=2, row=0, padx=5, pady=10)

    # Name tags
    r = tk.Label(win1, text="^ ROCK ^")
    r.grid(column=0, row=1)
    p = tk.Label(win1, text="^ PAPER ^")
    p.grid(column=1, row=1)
    s = tk.Label(win1, text="^ SCISSORS ^")
    s.grid(column=2, row=1)
    
    # VS
    lbl = tk.Label(win1, text=" VS ", font=("Arial Bold", 60))
    lbl.grid(column=1, row=2)
    
    # Exit button
    eButton = tk.Button(win1, text="Exit", fg="White", bg="Red", command=win1.destroy)
    eButton.grid(column=1, row=5)

def how2play():
    global rImg
    global pImg
    global sImg

    imgColumn = 1
    infoColumn = 2

    win = tk.Toplevel()
    win.title("How to play?")
    
    # Rock
    rImg = Image.open("rock.png")
    newsize = (100, 100)# same for all
    rImg = rImg.resize(newsize)
    rImg = ImageTk.PhotoImage(rImg)
    rockPic = tk.Label(win, image=rImg)
    rockPic.grid(column=imgColumn, row=0)

    rock = "Rock > Scissors or Rock < Paper"
    rockInfo = tk.Label(win, text=rock, font=("Arial Bold", 20))
    rockInfo.grid(column=infoColumn, row=0)

    # Paper
    pImg = Image.open("paper.png")
    pImg = pImg.resize(newsize)
    pImg = ImageTk.PhotoImage(pImg)
    paperPic = tk.Label(win, image=pImg)
    paperPic.grid(column=imgColumn, row=1)

    paper = "Paper > Rock or Paper < Scissors"
    paperInfo = tk.Label(win, text=paper, font=("Arial Bold", 20))
    paperInfo.grid(column=infoColumn, row=1)

    # Scissors
    sImg = Image.open("scissors.png")
    sImg = sImg.resize(newsize)
    sImg = ImageTk.PhotoImage(sImg)
    scissorsPic = tk.Label(win, image=sImg)
    scissorsPic.grid(column=imgColumn, row=2)

    scissors = "Scissors > Paper or Scissors < Rock"
    scissorsInfo = tk.Label(win, text=scissors, font=("Arial Bold", 20))
    scissorsInfo.grid(column=infoColumn, row=2)

    # Back button
    btn = tk.Button(win, text="Back", fg="white", bg="red", command=win.destroy)
    btn.grid(column=infoColumn, row=3)
