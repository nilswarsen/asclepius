import tkinter as tk
from tkinter import StringVar, ttk
from tkinter.messagebox import showinfo

# specify root window
root = tk.Tk()
root.title('Asclepius Regressietest')
new_geometry = '600x400+100+100'
root.geometry(new_geometry)
#root.attributes('-topmost', 1)

# signin window
signinwindow = tk.Tk()
signinwindow.geometry("300x150")
signinwindow.resizable(False, False)
signinwindow.title('Sign In')
signinwindow.attributes('-topmost', 1)

message = ttk.Label(root, text = 'Hallo ValueCare!')
message.pack()


# store email address and password
email = tk.StringVar()
password = tk.StringVar()


# Sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)


# email
email_label = ttk.Label(signin, text="Email Address:")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

# password
password_label = ttk.Label(signin, text="Password:")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=password, show="*")
password_entry.pack(fill='x', expand=True)

def login_clicked(mail: StringVar):
    """ callback when the login button clicked
    """
    welcome.tkraise()
    print(mail.get())
    return None

    

# login button
login_button = ttk.Button(signin, text="Login", command=lambda: login_clicked(email))
login_button.pack(fill='x', expand=True, pady=10)


class signin(tk.Frame):
    def __init__(self, container) -> None:
        super().__init__(container)

        

    

welcome = tk.Frame(root)
welcome.pack(padx=10, pady=10, fill='x', expand=True)

message2 = ttk.Label(welcome, text = 'Hallo!')
message2.pack()

def show_login(mail: tk.StringVar, passw: tk.StringVar):
    msg = f'You entered email: {mail.get()} and password: {passw.get()}'
    message2.config(text=msg)
    return None

button = ttk.Button(welcome, text="Show", command=lambda: show_login(mail=email, passw=password))
button.pack(fill='x', expand=True, pady=10)



root.mainloop()