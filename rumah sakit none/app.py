from CTkMessagebox import CTkMessagebox
from database import database
from main_menu import MainMenu
from customtkinter import *

#Set Custom Tkinter
set_appearance_mode("light")
set_default_color_theme("green")

#Login Window
class LoginWindow(database):

    def __init__(self):

        #Root Setup
        self.root = CTk()
        self.root.iconbitmap(r"C:\Users\Asus\Documents\rumah sakit none\hospital_icon.ico")

        width, height = 400, 300

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = int((screen_width/2) - (width/2))
        y = int((screen_height/2) - (height/2))

        self.root.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.root.title("RUMAH SAKIT NONE")
        self.root.resizable(False, False)

        #Frame
        self.frame = CTkFrame(master=self.root)
        self.frame.pack(pady = 10, padx = 10, fill ="both", expand=True)

        self.label = CTkLabel(self.frame, text="Enter Username & Password", font=("Bahnschrift", 24))
        self.label.pack(padx = 10, pady = 10)

        # Username
        self.name_entry = CTkEntry(self.frame, placeholder_text="Username" )
        self.name_entry.pack(padx = 10, pady = 10)

        # Password
        self.pass_entry = CTkEntry(self.frame, placeholder_text="Password", show='*')
        self.pass_entry.pack(padx = 10, pady = 10)

        login_button = CTkButton(self.frame, text="Login", command=self.login, hover_color="#2aa2c7", font=("Bahnschrift", 12, "bold"))
        login_button.pack(padx = 10, pady = 10)

        exit_button = CTkButton(self.frame, text="Exit", command=self.root.destroy, hover_color="#2aa2c7", font=("Bahnschrift", 12, "bold"))
        exit_button.pack(padx = 10, pady = 10)

        self.root.mainloop()

    # Validate login
    def login(self):

        name = self.name_entry.get()
        password = self.pass_entry.get()

        if name and password:
            import datetime as dt
            if name == LoginWindow._database__conn._user and password == LoginWindow._database__conn._password:
                print(f"User [{name}] logged in at {dt.datetime.now()}")
                logged = CTkMessagebox(title="Login Successful !", message=f"Welcome, {name}", icon="check", option_1="ok")
                if logged.get() == "ok":
                    self.root.destroy()
                    main = MainMenu()
            else:
                CTkMessagebox(title="Access Denied !", message="Invalid Username or Password", icon="cancel")
        else:
            CTkMessagebox(title="Incomplete Fields !", message="Please enter username and password", icon="warning")


main = LoginWindow()  

