from customtkinter import *
from pasien import pasien
from obat import obat
from doctor import doctor
from ruangan import ruangan

set_appearance_mode("light")
set_default_color_theme("green")

class MainMenu(pasien, obat, doctor, ruangan):

    def __init__(self):

        self.root = CTk()
        self.root.iconbitmap(r"C:\Users\Asus\Documents\rumah sakit none\hospital_icon.ico")

        width = 1100
        height = 500
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width/2) - (width/2))
        y = int((screen_height/2) - (height/2))

        self.root.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.root.title("Rumah Sakit NONE")

        self.master_frame = CTkFrame(master=self.root)
        self.master_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.sidebar = CTkFrame(master=self.master_frame, width=200, height=200, corner_radius=0)
        self.sidebar.pack(side=LEFT, fill=Y, expand=False)

        #Sidebar
        self.home_btn = CTkButton(self.sidebar, text="Home", anchor="center", command=self.return_home_label, hover_color="#2aa2c7", font=("Bahnschrift", 12))
        self.home_btn.pack(padx=20, pady=10)

        self.pasien_btn = CTkButton(self.sidebar, text="Pasien", anchor="center", command=self.pasien_frame_event, hover_color="#2aa2c7", font=("Bahnschrift", 12))
        self.pasien_btn.pack(padx=20, pady=10)

        self.doctor_btn = CTkButton(self.sidebar, text="Doctor", anchor="center", command=self.doctor_frame_event, hover_color="#2aa2c7", font=("Bahnschrift", 12))
        self.doctor_btn.pack(padx=20, pady=10)

        self.obat_btn = CTkButton(self.sidebar, text="Obat", anchor="center", command=self.obat_frame_event, hover_color="#2aa2c7", font=("Bahnschrift", 12))
        self.obat_btn.pack(padx=20, pady=10)

        self.ruangan_btn = CTkButton(self.sidebar, text="Ruangan", anchor="center", command=self.ruangan_frame_event, hover_color="#2aa2c7", font=("Bahnschrift", 12))
        self.ruangan_btn.pack(padx=20, pady=10)

        self.exit_btn = CTkButton(self.sidebar, text="Exit", anchor="center", command=self.root.destroy, hover_color="red", font=("Bahnschrift", 12))
        self.exit_btn.pack(side="bottom", padx=10, pady=10)

        self.setting_btn = CTkButton(self.sidebar, text="Setting", anchor="center", command=self.setting_frame_event, hover_color="#2aa2c7", font=("Bahnschrift", 12))
        self.setting_btn.pack(side="bottom", padx=20, pady=10)

        #Right Frame
        self.right_frame = CTkFrame(master=self.master_frame, width=140, corner_radius=0)
        self.right_frame.pack(side=RIGHT, fill="both", expand=True, anchor="center")

        self.home_label = CTkLabel(self.right_frame, text="Selamat Datang di Rumah Sakit NONE", anchor="center", font=("Bahnschrift", 50))
        self.home_label.pack(side=LEFT, fill="both", expand=True)

        self.root.mainloop()

    def return_home_label(self):

        #Destroy any active frame
        for frames in self.right_frame.winfo_children():
            frames.destroy()

        self.home_label = CTkLabel(self.right_frame, anchor="center", text="Selamat Datang di Rumah Sakit NONE", font=("Bahnschrift", 50))
        self.home_label.pack(side=LEFT, fill="both", expand=True)

    def setting_frame_event(self):

        #Destroy any active frame
        for frames in self.right_frame.winfo_children():
            frames.destroy()
        
        self.setting_frame = CTkFrame(self.right_frame)
        self.setting_frame.pack(side=LEFT, fill="both", expand=True)

        self.appearance_label = CTkLabel(self.setting_frame, text="Appearance", font=("Bahnschrift", 14))
        self.appearance_label.grid(row=0, column=0, sticky="ew")

        self.appearance_combo = CTkOptionMenu(self.setting_frame, values=["Light", "Dark"], command=self.change_appearance, button_hover_color="#2aa2c7")
        self.appearance_combo.grid(row=1, column=0, padx=20, pady=(10, 20))

        self.scale_label = CTkLabel(self.setting_frame, text="Scale", font=("Bahnschrift", 14))
        self.scale_label.grid(row=2, column=0, sticky="ew")

        self.scale_setting = CTkOptionMenu(self.setting_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.scale_setting_event, button_hover_color="#2aa2c7")
        self.scale_setting.grid(row=3, column=0, padx=20, pady=(10, 20))

    #Theme Function
    def change_appearance(self, new_theme):
        set_appearance_mode(new_theme) 

    #Scale Function
    def scale_setting_event(self, new_scaling):
        new_scaling_float = float(new_scaling.replace("%", "")) / 100
        set_widget_scaling(new_scaling_float)

if __name__ == "__main__":
    run = MainMenu()
