import tkinter as tk
from tkinter import END, ttk
from tkinter import filedialog as fd
from tkinter.scrolledtext import ScrolledText

import sys
sys.path.append(r'.\src')
from asclepius.medewerker import Medewerker
from asclepius.instelling import GGZ, Instelling
from asclepius.releasetest import ReleaseTest
from ggz_instellingen import alle_instellingen

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Asclepius Releasetest')
        self.geometry('600x600')

        #background_image = tk.PhotoImage(file = 'index.gif')
        #background_label = ttk.Label(self, image=background_image)
        #background_label.place(x=0, y=0)

        #s = ttk.Style()
        # Create style used by default for all Frames
        #s.configure('TFrame', background = "")   

        # label
        #self.label = ttk.Label(self, text = 'Dit is de app window')
        #self.label.pack()

        self.email: str
        self.password: str
        self.medewerker: Medewerker
        self.releasetest: ReleaseTest

        self.instellingen = []

        return None

class SignIn(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, width = 300, height = 150)

        self.email = tk.StringVar()
        self.password = tk.StringVar()

        # email
        email_label = ttk.Label(self, text = "Email Address:")
        email_label.pack(fill='x', expand=True)

        email_entry = ttk.Entry(self, textvariable = self.email)
        email_entry.pack(fill='x', expand=True)
        email_entry.focus()

        # password
        password_label = ttk.Label(self, text = "Password:")
        password_label.pack(fill='x', expand=True)

        password_entry = ttk.Entry(self, textvariable = self.password, show="*")
        password_entry.pack(fill='x', expand=True)

        # login button
        login_button = ttk.Button(self, text = "Login", command = self.login_clicked)
        login_button.pack(fill='x', expand=True, pady=10)

        self.pack(padx=10, pady=10, fill=None, expand=True)
        self.pack_propagate(0)

        return None

    def login_clicked(self):
        app.email, app.password = self.email.get(), self.password.get()
        downloads = Downloads(app)
        downloads.tkraise()
        self.destroy()
        return None

    
class Downloads(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, width = 300, height = 150)

        self.downloads = tk.StringVar()
        self.destination = tk.StringVar()

        # downloads map
        downloads_label = ttk.Label(self, text = "Downloads map:")
        downloads_label.grid(row = 0, column  = 0, sticky='w')

        # open button
        downloads_button = ttk.Button(self, text='Map selecteren', command=lambda: self.select_folder('downloads'))
        downloads_button.grid(row = 1, column = 1, sticky='w', columnspan = 1, padx=10, pady=10)

        self.downloads_entry = ttk.Entry(self, textvariable = self.downloads)
        self.downloads_entry.grid(row = 1, column = 0)

        # destination map
        destination_label = ttk.Label(self, text = "Bestemmings map:")
        destination_label.grid(row = 2, column  = 0, sticky='w')

        destination_button = ttk.Button(self, text='Map selecteren', command=lambda: self.select_folder('destination'))
        destination_button.grid(row = 3, column = 1, sticky='w', columnspan = 1, padx=10, pady=10)

        self.destination_entry = ttk.Entry(self, textvariable = self.destination)
        self.destination_entry.grid(row = 3, column = 0)

        # save button
        save_button = ttk.Button(self, text = "Opslaan", command = self.save_clicked)
        save_button.grid(row = 5, column = 0, sticky='w', columnspan = 1, padx=10, pady=10)

        self.pack(padx=10, pady=10, fill=None, expand=True)
        self.pack_propagate(0)

        return None


    def select_folder(self, folder):
        foldername = fd.askdirectory(title='Open folder', initialdir='/')
        setattr(self, folder, foldername)

        entry_name = f'{folder}_entry'
        entry = getattr(self, entry_name)
        entry.delete(0, END)
        entry.insert(0, foldername)
        return None

    def save_clicked(self):
        app.medewerker = Medewerker(app.email, self.downloads, self.destination, wachtwoord = app.password)
        kies_instelling = KiesInstelling(app)
        kies_instelling.tkraise()
        self.destroy()
        return None

class KiesInstelling(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, width = 300, height = 350)

        # label
        test_label = ttk.Label(self, text = "Vink aan welke instellingen je wilt testen:")
        test_label.pack(fill = 'x', padx = 5, pady = 5)

        save_button = ttk.Button(self, text = "Opslaan", command = self.save_clicked)
        save_button.pack(fill='x', padx=5, pady=5, anchor='s')

        self.instelling_dict = {}

        text = ScrolledText(self, width = 200, height = 50)
        text.pack()

        for instelling in alle_instellingen:
            self.instelling_dict[instelling.klant_code] = tk.IntVar()
            checkbox = tk.Checkbutton(text, text = instelling.klant_code, variable = self.instelling_dict[instelling.klant_code], onvalue=1, offvalue=0, bg='white', anchor='w')
            checkbox.pack(fill = 'x', padx = 5, pady = 5)
            text.window_create('end', window=checkbox)
            text.insert('end', '\n')
        
        text.configure(state ='disabled')

        self.pack(padx=10, pady=10, fill=None, expand=True)
        self.pack_propagate(0)
        return None

    def save_clicked(self):
        for instelling in alle_instellingen:
            if self.instelling_dict[instelling.klant_code].get():
                app.instellingen.append(instelling)
        
        testen = Testen(app)
        testen.tkraise()
        self.destroy()
        return None

class Testen(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, width = 300, height = 150)

        # label
        test_label = ttk.Label(self, text = "Kies welke test je wilt uitvoeren:")
        test_label.pack(fill = 'x', padx = 5, pady = 5)

        self.selected_test = tk.StringVar()

        # BI test button
        bi_button = ttk.Radiobutton(self, text = "BI Prestatiekaarten", value = 'bi', variable = self.selected_test)
        bi_button.pack(fill='x', padx=5, pady=5)

        # omzetprognose test button
        omzet_button = ttk.Radiobutton(self, text = "Omzetprognose", value = 'omzetprognose', variable = self.selected_test)
        omzet_button.pack(fill='x', padx=5, pady=5)

        test_button = ttk.Button(self, text = "Testen", command = self.start_test)
        test_button.pack(fill='x', padx=5, pady=5)



        self.pack(padx=10, pady=10, fill=None, expand=True)
        self.pack_propagate(0)
        return None

    def start_test(self):
        # initialize
        product = self.selected_test.get()
        app.releasetest = ReleaseTest(app.medewerker, product = product)

        # test
        instellingen = app.instellingen
        app.releasetest.test(*instellingen)
        return




if __name__ == "__main__":
    app = App()
    signin = SignIn(app)
    app.mainloop()