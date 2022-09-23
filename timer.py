import tkinter as tk

counter = 60
def counter_label(label):
  counter = 60
  def count():
    global counter
    counter -= 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()

def clicked():
    global counter # inform funtion to use external variable `count`
    counter = counter + 60

def clicked5():
    global counter # inform funtion to use external variable `count`
    counter = counter + 300

def clicked10():
    global counter # inform funtion to use external variable `count`
    counter = counter + 600
 
 
root = tk.Tk()
root.title("Subathon Timer")
label = tk.Label(root, fg="dark green", font=("Arial", 45))
label.pack()
counter_label(label)
button = tk.Button(root, text='add minute', width=25, command=clicked)

button.pack()

button2a = tk.Button(root, text='add 5 minutes', width=25, command=clicked5)
button2a.pack()

button2 = tk.Button(root, text='add 10 minutes', width=25, command=clicked10)
button2.pack()
root.mainloop()
