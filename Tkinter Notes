import tkinter as tk

def on_button_click():
    label.config(text="Hello,Tkinter!")

#create the main application window
root =tk.Tk()

#set the window title
root.title("Tkinter Example")

#set the window size
root.geometry("300x150")

#create a label widget
label = tk.Label(root,text = "click the button to change this")
label.pack(pady=20)

#create a button
button = tk.Button(root,text = "Click Me!",command=on_button_click)
button.pack()


#start the Tkinter event loop
root.mainloop()