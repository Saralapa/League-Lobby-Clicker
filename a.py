import tkinter as Tk

root = Tk.Tk()
root.title("Vários títulos")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - 400) // 2
y = (screen_height - 400) // 2
root.geometry(f"400x400+{x-screen_width}+{y}")

buttonA = Tk.Button(root, text="Texto de um botão", command=lambda: root.title("Texto de um botão"))
buttonA.pack(pady=50)
buttonB = Tk.Button(root, text="League of Legends (TM) Client", command=lambda: root.title("League of Legends (TM) Client"))
buttonB.pack(pady=50)

root.mainloop()