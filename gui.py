import tkinter as tk
from tkinter import ttk
from secret import get_secret_key
from database import connect, disconnect, data, add_password

global key
key = get_secret_key()

class showall():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x300")
        top_bar = tk.Frame(self.root, height=50, bg='lightblue')
        top_bar.pack(side=tk.TOP, fill=tk.X)

        tk.Button(top_bar, text="UPDATE", width=400, command=self.update).pack()
        
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.scrollable_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor='nw')


        self.scrollable_frame.bind("<Configure>", self.on_frame_configure)

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def update(self):
        connect()
        udata = data()
    
        for button in self.scrollable_frame.winfo_children():
            button.destroy()

        for entry in udata:
            self.name = entry[2]
            self.btn = tk.Button(self.scrollable_frame, text=f"{self.name}", command=lambda id=self.name: self.button_click(id))
            self.btn.pack(padx=10, pady=10)

        disconnect()
    def button_click(self, id):
        print(f"Button {id} clicked!")



    
class insert():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x700")

        self.id = tk.Label(self.root, text="What is the app for your login?").pack(pady=10)
        self.entry1 = tk.Entry(self.root, width=50, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light ', 11))
        self.entry1.pack(padx=0, pady=20)

        self.name = tk.Label(self.root, text="insert the username").pack(pady=10)
        self.entry2 = tk.Entry(self.root, width=50, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light ', 11))
        self.entry2.pack(padx=0, pady=20)
        self.age = tk.Label(self.root, text="insert the password").pack(pady=10)
        self.entry3 = tk.Entry(self.root, width=50, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light ', 11))
        self.entry3.pack(padx=0, pady=20)

        self.button = tk.Button(self.root, text='insert', command=self.enter, width=20, height=1).pack(pady=20)
        self.back = tk.Button(self.root, text='back', command=self.back_out, width=20, height=1).pack(pady=20)

    def back_out(self):
        self.root.destroy()
        logged_in()

    def enter(self):
        user = self.entry2.get()
        password = self.entry3.get()
        app = self.entry1.get()
        connect()
        add_password(user, password, app)
        disconnect()
        self.root.destroy()
        logged_in()


class logged_in():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")

        self.label = tk.Label(self.root, text="LOGIN SUCCESSFUL")
        self.label.pack()

        self.insert = tk.Button(self.root, text="INSERT", font=('Microsoft YaHei UI Light ', 18), width = 400, height= 3, command=self.inserts)
        self.insert.pack(padx=10, pady=20)

        self.frame = tk.Frame(self.root)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        self.search = tk.Button(self.frame, text="SEARCH", font=('Microsoft YaHei UI Light ', 18), height=3, fg="black")
        self.search.grid(row=0, column=0, sticky = tk.W+tk.E, padx=20, pady=20)
        
        self.all = tk.Button(self.frame, text="SHOW ALL", font=('Microsoft YaHei UI Light ', 18), height=3, command=self.show_all)
        self.all.grid(row=0, column=1, sticky = tk.W+tk.E, padx=20, pady=20)

        self.revise = tk.Button(self.frame, text="REVISE", font=('Microsoft YaHei UI Light ', 18), height=3)
        self.revise.grid(row=1, column=0, sticky = tk.W+tk.E, padx=20, pady=20)

        self.delete= tk.Button(self.frame, text="DELETE", font=('Microsoft YaHei UI Light ', 18), height=3)
        self.delete.grid(row=1, column=1, sticky = tk.W+tk.E, padx=20, pady=20)
        self.frame.pack(padx=20, pady=20, fill='x')

        self.root.mainloop()
    
    def show_all(self):
        connect()
        data()
        disconnect()
        self.root.destroy()
        showall()
    
    def inserts(self):
        self.root.destroy()
        insert()



class Login:
    def __init__(self):
        self.secret_key = get_secret_key()

        self.root = tk.Tk()
        self.root.geometry('500x500')

        self.label = tk.Label(self.root, text='ENTER YOUR MASTER PASSWORD', font=('Microsoft YaHei UI Light ', 18))
        self.label.pack(padx=10, pady=100)

        self.entry = tk.Entry(self.root, width=50, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light ', 11))
        self.entry.insert(0, 'Password')
        self.entry.pack(pady=10)
        self.entry.bind('<FocusIn>', self.clear_entry)
        self.entry.bind('<FocusOut>', self.restore_entry)

        self.button = tk.Button(self.root, text='login', command=self.login, width=20, height=1)
        self.button.pack()

        self.root.mainloop()

    def clear_entry(self, event):
        if self.entry.get() == 'Password':
            self.entry.delete(0, 'end')
            self.entry.config(fg='black', show='*') 

    def restore_entry(self, event):
        if not self.entry.get():
            self.entry.insert(0, 'Password')
            self.entry.config(fg='black', show='')

    def login(self):
        entered_password = self.entry.get()
        
        if entered_password == self.secret_key:
            print("Login successful!")
            self.root.destroy()
            logged_in()
        else:
            print("Login failed!")

if __name__ == "__main__":
    Login()