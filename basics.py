import tkinter as tk
def say_hello():
    print("Hello,Tkinter!")
window = tk.Tk()
window.geometry("300x200+10+20")
button = tk.Button(window,text = "Say Hello",command = say_hello)
button.pack()
window.mainloop()