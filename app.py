from tkinter import *
import tkinter as tk
from tkinter import ttk
import pygame
import tkinter.font as font

# import mp3play


# f = mp3play.load('button-16.mp3');
# play = lambda: f.play()                for windows only


root = tk.Tk()

photo = PhotoImage(file="attack_on_titan_logo.png")

root.iconphoto(False, photo)

root.title("Distance converter")
root.geometry("300x150")
root.resizable(False, False)
meters_value = tk.StringVar()
feet_value = tk.StringVar(value="")

font.nametofont("TkDefaultFont").configure(size=11)  # it takes tkinter default font and can change the size

main_frame = ttk.Frame(root)
main_frame.grid()


def calculate_feet(*args):
    try:
        play_music()
        meters = float(meters_value.get())
        feet = meters * 3.28084
        feet_value.set(f"{feet} feet")
        print(f"feet={feet}")
        meter_input.textvariable=" "


    except ValueError:
        play_error_music()


pygame.mixer.init()


def play_music():
    pygame.mixer.music.load("button-16.wav")
    pygame.mixer.music.play()

def play_error_music():
    pygame.mixer.music.load("error.wav")
    pygame.mixer.music.play()


# creating bunch of buttons without grid

meter_label = ttk.Label(main_frame, text="Meters: ")
meter_input = ttk.Entry(main_frame, width=25, textvariable=meters_value, font=("Segoe ui", 15))
feet_label = ttk.Label(main_frame, text="Feet: ")
feet_Display = ttk.Label(main_frame, textvariable=feet_value)
press_button = ttk.Button(main_frame, text="press here", command=calculate_feet)

# placing them in main frames

meter_label.grid(row=0, column=0, sticky="W", padx=10, pady=10)

meter_input.grid(row=0, column=1)
meter_input.focus()

feet_label.grid(row=1, column=0, sticky="W", padx=10, pady=10)

feet_Display.grid(row=1, column=1,sticky="w")
# press_button.grid(row=2,column=0,sticky="ew",padx=10,pady=10,columnspan=8)

press_button.grid(row=2, column=1, columnspan=8, sticky="W")

root.bind("<KP_Enter>", calculate_feet)  # you can select meter_input as well

root.mainloop()
