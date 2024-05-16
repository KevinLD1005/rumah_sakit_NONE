from customtkinter import *
from database import database
from CTkMessagebox import CTkMessagebox

class ruangan(database):
        
    def ruangan_frame_event(self):

        #Destroy any active frame
        for frames in self.right_frame.winfo_children():
            frames.destroy()

        #Fetch Data
        self.data_ruangan = self.select_all("ruangan")

        self.ruangan_tab = CTkTabview(self.right_frame, anchor=W)
        self.ruangan_tab.pack(side=LEFT, fill="both", expand=True)
        self.ruangan_tab.add("Add Ruangan")
        self.ruangan_tab.add("View Ruangan")
        self.ruangan_tab.add("Edit Ruangan")
        self.ruangan_tab.add("Delete Ruangan")

        "Add Ruangan Tab"

        #Kode
        self.kode_label = CTkLabel(self.ruangan_tab.tab("Add Ruangan"), text="Kode", anchor="center", font=("Bahnschrift", 14))
        self.kode_label.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.kode_entry = CTkEntry(self.ruangan_tab.tab("Add Ruangan"), placeholder_text="please enter kode")
        self.kode_entry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        # #Jenis
        self.jenis_label = CTkLabel(self.ruangan_tab.tab("Add Ruangan"), anchor="center", text="Jenis", font=("Bahnschrift", 14))
        self.jenis_label.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.jenis_entry = CTkEntry(self.ruangan_tab.tab("Add Ruangan"), placeholder_text="Please enter jenis")
        self.jenis_entry.grid(row=1, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        #Kapasitas
        self.kapasitas_label = CTkLabel(self.ruangan_tab.tab("Add Ruangan"), anchor="center", text="Kapasitas", font=("Bahnschrift", 14))
        self.kapasitas_label.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        self.kapasitas_entry = CTkEntry(self.ruangan_tab.tab("Add Ruangan"), placeholder_text="Please enter kapasitas")
        self.kapasitas_entry.grid(row=2, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        #Blood Type
        self.status_label = CTkLabel(self.ruangan_tab.tab("Add Ruangan"), text="Status", font=("Bahnschrift", 14))
        self.status_label.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

        self.status_entry = CTkEntry(self.ruangan_tab.tab("Add Ruangan"), placeholder_text="Please enter status")
        self.status_entry.grid(row=3, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        #Condition
        self.biaya_label = CTkLabel(self.ruangan_tab.tab("Add Ruangan"), text="Biaya", font=("Bahnschrift", 14))
        self.biaya_label.grid(row=4, column=0, padx=20, pady=20, sticky="ew")

        self.biaya_entry = CTkEntry(self.ruangan_tab.tab("Add Ruangan"), placeholder_text="Please enter biaya")
        self.biaya_entry.grid(row=4, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        #Submit
        self.submit_btn = CTkButton(self.ruangan_tab.tab("Add Ruangan"), text="Submit", command=self.submit_ruangan, hover_color="#2aa2c7", font=("Bahnschrift", 14))
        self.submit_btn.grid(row=4, column=4, padx=20, pady=20)

        "View Ruangan"

        headers = ["Kode", "Jenis", "Kapasitas", "Status", "Biaya"]
        for col, header in enumerate(headers):
            label = CTkLabel(self.ruangan_tab.tab("View Ruangan"), text=header, font=("Bahnschrift", 14))
            label.grid(row=0, column=col, padx=2, pady=2)

        for i, name in enumerate(self.data_ruangan, start=1):
            for col, value in enumerate(name):
                entry = CTkEntry(self.ruangan_tab.tab("View Ruangan"))
                entry.insert(END, value)
                entry.grid(row=i, column=col, padx=2, pady=2)


        "Edit Ruangan"

        self.edit_jenis_label = CTkLabel(self.ruangan_tab.tab("Edit Ruangan"), text="Jenis", font=("Bahnschrift", 14))
        self.edit_jenis_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.edit_jenis_entry = CTkEntry(self.ruangan_tab.tab("Edit Ruangan"), placeholder_text="Enter Jenis...")
        self.edit_jenis_entry.grid(row=0, column=1, padx=5,  pady=5, sticky="ew")

        self.column_label = CTkLabel(self.ruangan_tab.tab("Edit Ruangan"), text="Status", font=("Bahnschrift", 14))
        self.column_label.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.column_option = CTkOptionMenu(self.ruangan_tab.tab("Edit Ruangan"), values=["Tersedia", "Penuh"], button_hover_color="#2aa2c7")
        self.column_option.set("")
        self.column_option.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.update_label = CTkLabel(self.ruangan_tab.tab("Edit Ruangan"), text="Update", font=("Bahnschrift", 14))
        self.update_label.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

        self.update_btn = CTkButton(self.ruangan_tab.tab("Edit Ruangan"), text="Update", command=self.update_ruangan_event, hover_color="#2aa2c7", font=("Bahnschrift", 14))
        self.update_btn.grid(row=3, column=1, padx=5, pady=5)

        "Delete Ruangan"

        self.del_jenis_label = CTkLabel(self.ruangan_tab.tab("Delete Ruangan"), text="Delete by Jenis", font=("Bahnschrift", 14))
        self.del_jenis_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.del_jenis_entry = CTkEntry(self.ruangan_tab.tab("Delete Ruangan"), placeholder_text="Enter Jenis...")
        self.del_jenis_entry.grid(row=0, column=1, padx=5,  pady=5, sticky="ew")

        self.del_kode_label = CTkLabel(self.ruangan_tab.tab("Delete Ruangan"), text="Delete by Kode", font=("Bahnschrift", 14))
        self.del_kode_label.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.del_kode_entry = CTkEntry(self.ruangan_tab.tab("Delete Ruangan"), placeholder_text="Enter Kode...")
        self.del_kode_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.delete_btn = CTkButton(self.ruangan_tab.tab("Delete Ruangan"), text="Delete", command=self.delete_ruangan_event, hover_color="#2aa2c7", font=("Bahnschrift", 14))
        self.delete_btn.grid(row=2, column=1, padx=5, pady=5)


    def submit_ruangan(self):
        
        kode = self.kode_entry.get()
        jenis = self.jenis_entry.get()
        kapasitas = self.kapasitas_entry.get()
        status = self.status_entry.get()
        biaya = self.biaya_entry.get()

        if kode =="" or kapasitas=="" or jenis=="" or status=="" or biaya=="":

            CTkMessagebox(title="Error !", message="Please enter full data", icon="cancel")

        else:
            columns = ("`Kode`", "`Jenis`", "`Kapasitas`", "`Status`", "`Biaya`")
            values = (kode, jenis, kapasitas, status, biaya)
            self.insert("ruangan", columns, values)
            info_box = CTkMessagebox(title="Submitted !", message=f"Ruangan '{kode}' successfully submited", icon="check", option_1="ok")

            if info_box.get() == "ok":
                return self.ruangan_frame_event()
            
            print(kode, kapasitas, jenis, status, biaya, status)


    def delete_ruangan_event(self):
        name = self.del_jenis_entry.get()
        ID = self.del_kode_entry.get()

        if name:
            self.delete("ruangan", "Jenis" , name)

            info_box = CTkMessagebox(title="Updated !", message=f"Ruangan'{name}' successfully deleted", icon="check", option_1="ok")
            if info_box.get() == "ok":
                return self.ruangan_frame_event()

        elif ID:
            self.delete("ruangan", "Kode", ID)

            info_box = CTkMessagebox(title="Updated !", message=f"Ruangan'{ID}' successfully deleted", icon="check", option_1="ok")
            if info_box.get() == "ok":
                return self.ruangan_frame_event()
    
    def update_ruangan_event(self):
        value = self.column_option.get()
        jenis = self.edit_jenis_entry.get()

        if jenis =="" or value=="":

            CTkMessagebox(title="Error !", message="Please enter complete fields", icon="cancel")

        else:

            value = self.column_option.get()
            jenis = self.edit_jenis_entry.get()
            self.update("ruangan", "Status", value, "Jenis", jenis)

            info_box = CTkMessagebox(title="Updated !", message=f"ruangan '{jenis}' successfully updated", icon="check", option_1="ok")
            if info_box.get() == "ok":
                return self.ruangan_frame_event()



