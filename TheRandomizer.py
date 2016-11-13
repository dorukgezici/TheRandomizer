#!/usr/bin/env python3

import tkinter as tk
import random

class Data:
    people = []

def run():
    n = len(Data.people)
    if n >= 1:
        i = random.randrange(n)
        person1_label["text"] = Data.people[i]
    else:
        clear_output_labels()
        person1_label["text"] = "You need to add at least 1 people."
    # n = len(Data.people)
    # if n >= 2:
    #     a = random.randrange(n)
    #     b = random.randrange(n)
    #     while a == b:
    #         b = random.randrange(n)
    #     person1_label["text"] = Data.people[a]
    #     arrow_label["text"] = "|\nV"
    #     person2_label["text"] = Data.people[b]
    # else:
    #     clear_output_labels()
    #     person1_label["text"] = "You need to add at least 2 people."

def run_event(event):
    run()

def add():
    new_person = add_person_text.get()
    if new_person != "":
        Data.people.append(new_person)
        people_listbox.insert("end", new_person)
    add_person_text.set("")

def add_event(event):
    add()

def add_team():
    Data.people.extend(["Doruk Gezici", "Anıl Esen", "Zeynep Tek", "Ahmet Cüce", "Özgur Can Milletsever", "Halit Erdoğan", "İrem Işık", "Levent Güner", "Umut Avin", "Ekin Çelebi", "Pelin Gümüşlü", "Defne Bayrak", "Orçun Uysal", "Dilara Bozyılan", "Erdem Özkur"])
    Data.people.sort()
    for person in Data.people:
        people_listbox.insert("end", person)

def remove():
    try:
        i = people_listbox.curselection()[0]
        Data.people.pop(i)
        people_listbox.delete(i)
        clear_output_labels()
    except IndexError:
        clear_output_labels()
        person1_label["text"] = "You haven't selected anyone."

def remove_event(event):
    remove()

def clear():
    Data.people = []
    people_listbox.delete(0, "end")
    clear_output_labels()

def clear_output_labels():
    person1_label["text"] = ""
    arrow_label["text"] = ""
    person2_label["text"] = ""

root = tk.Tk()
root.title("EESTEC LC Istanbul")
root.geometry("640x480+300+100")
root.resizable(width=0, height=0)

header = tk.Label(root, text="IoT Line Fair '17 Team - Osman the Randomizer", padx=10, pady=10)
header.pack()

left_frame = tk.Frame(root)
left_frame.pack(side="left", padx=30, pady=30, fill="both")

people_label = tk.Label(left_frame, text="People")
people_label.pack()

people_listbox = tk.Listbox(left_frame)
people_listbox.pack(side="left", fill="y")
people_listbox.bind("<BackSpace>", remove_event)

right_frame = tk.Frame(root)
right_frame.pack(side="right", padx=30, pady=30, fill="both")

add_person_text = tk.StringVar()
add_person_entry = tk.Entry(right_frame, textvariable=add_person_text)
add_person_entry.pack()
add_person_entry.bind("<Return>", add_event)

list_buttons = tk.Frame(right_frame)
list_buttons.pack()

add_person_button = tk.Button(list_buttons, text="ADD", command=add)
add_person_button.pack(side="left")

remove_person_button = tk.Button(list_buttons, text="REMOVE", command=remove)
remove_person_button.pack(side="left")

add_team_button = tk.Button(list_buttons, text="ADD WHOLE TEAM", command=add_team)
add_team_button.pack(side="right")

output_frame = tk.Frame(right_frame)
output_frame.pack(pady=80)

person1_label = tk.Label(output_frame)
person1_label.pack()

arrow_label = tk.Label(output_frame)
arrow_label.pack()

person2_label = tk.Label(output_frame)
person2_label.pack()

buttons_frame = tk.Frame(right_frame)
buttons_frame.pack(side="bottom")

quit_button = tk.Button(buttons_frame, text="QUIT", command=root.destroy)
quit_button.pack(side="right")

clear_button = tk.Button(buttons_frame, text="CLEAR", command=clear)
clear_button.pack(side="right")

run_button = tk.Button(buttons_frame, text="RUN", command=run)
run_button.pack(side="left")

root.lift()
root.bind("<Command-r>", run_event)
root.mainloop()
