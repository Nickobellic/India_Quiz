from tkinter import *
from tkinter import messagebox
import pandas as pd
# states_and_ut = ["Rajasthan","Madhya Pradesh","Maharashtra","Uttar Pradesh","Gujarat","Karnataka","Andhra Pradesh","Odisha","Chhattisgarh",	 "Tamil Nadu","Telangana","Bihar","West Bengal","Arunachal Pradesh","Jharkhand", "Assam","Ladakh","Himachal Pradesh","Uttarakhand","Punjab","Haryana","Jammu and Kashmir","Kerala","Meghalaya","Manipur","Mizoram","Nagaland","Tripura","Andaman and Nicobar Islands","Sikkim","Goa", "Delhi", "Dadra and Nagar Haveli and Daman and Diu", "Puducherry", "Chandigarh", "Lakshadweep"]
# x_cor = []
# y_cor = []
# st = 0

found_states = 0 # FOUND STATES' COUNT

# WINDOW SETUP
root = Tk()
root.config(bg="black")
inp = StringVar()
root.title('Can you guess the States?')


# UI OF THE QUIZ
map = Canvas(root, width=400, height=500, bg="black")
img_path = "india-outline-map.png"
img = PhotoImage(file=img_path)
ima = map.create_image(200, 250, image=img)
found = Label(text=f"States & UT Found: {found_states}/36", font=("Verdana", 20, 'bold'), fg="white", bg="black")
lab = Label(text="Guess the Next State:", bg="black", fg="white", font=("Verdana",20,'bold'))
state = Entry(textvariable=inp, bg="white", width=20, font=("Verdana"))
check = Button(text="OK", font=("Verdana", 15), bg="red", fg="white", width=10, command=lambda: verify(inp.get().title()))
state.focus_set()


found.pack()
map.pack()
lab.pack()
state.pack()
check.pack()

# READING THE CSV AND GETTING INPUT FROM THE PLAYER
coor = pd.read_csv('Coordinates.csv')
mentioned = []

def verify(answer_or_not):
    global found_states
    state.delete(0,END)
    correct_states = list(coor['State'])
    coordinates_x = list(coor['X'])
    coordinates_y = list(coor['Y'])
    if answer_or_not in correct_states:
        if answer_or_not not in mentioned:
            found_states += 1
            mentioned.append(answer_or_not)
            found.config(text=f"States & UT Found: {found_states}/36")
            t = correct_states.index(answer_or_not)
            l = map.create_text(coordinates_x[t], coordinates_y[t], text=answer_or_not)

    if len(mentioned) == 36:
        lab.config(state=DISABLED)
        state.config(state=DISABLED)
        messagebox.showinfo(title="India Quiz", message="You\'ve found all the 29 States and 7 Union Territories. Congratulations ")
        root.after(2000, quit())


# CODE TO FIND THE COORDINATGS
#
# def store(e):
#     global st
#     x = e.x
#     y = e.y
#     x_cor.append(x)
#     y_cor.append(y)
#     print(x, y)
#     st += 1
#
# root.bind('<Button-1>',store)
#
# if st == 36:
#     t = pd.read_csv('Coordinates.csv')
#     tp = pd.DataFrame({'X':x_cor, 'Y':y_cor})
#     t['X'] = tp['X']
#     t['Y'] = tp['Y']













root.mainloop()