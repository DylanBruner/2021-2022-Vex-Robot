import os, serial, sys
import tkinter as tk

COM_PORT = str(input("Com Port> "))#.lower().replace("com","")


ser = serial.Serial(port=COM_PORT,baudrate=115200)

def write(text):
    ser.write(bytes(text+'\r\n','utf-8'))

def read():
    return ser.readline().decode('utf-8')

def console():
    while True:
        write(input(">> "))
        print(read())

def robot_drive(direction,distance):
    write("drivetrain.drive_for([DIRECTION],[DISTANCE],INCHES)".replace("[DIRECTION]",direction.upper()).replace("[DISTANCE]",str(distance)))

def robot_turn(direction,distance):
    write("drivetrain.turn_for([DIRECTION],[DISTANCE],DEGREES)".replace("[DIRECTION]",direction.upper()).replace("[DISTANCE]",str(distance)))

root=tk.Tk()
def key_pressed(event):
    if str(event.char).lower() == "w":
        robot_drive("FORWARD",3)

    elif str(event.char).lower() == "s":
        robot_drive("REVERSE",3)

    elif str(event.char).lower() == "a":
        robot_turn("LEFT",.25)

    elif str(event.char).lower() == "d":
        robot_turn("RIGHT",.25)

root.bind("<Key>",key_pressed)
lbl = tk.Label(root, text="v5 Remote")
lbl.pack()
root.geometry("100x100")
root.mainloop()
