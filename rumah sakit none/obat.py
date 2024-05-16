from customtkinter import *
from database import database
from CTkMessagebox import CTkMessagebox


class obat(database):

    def obat_frame_event(self):

        #Fetch Data
        self.data_pasien = self.select_all("obat")

        #Destroy any active frame
        for frames in self.right_frame.winfo_children():
            frames.destroy()

        # #Fetch Data
        # self.data_pasien = self.select_all("pasien")

        self.obat_tab = CTkTabview(self.right_frame, anchor=W)
        self.obat_tab.pack(side=LEFT, fill="both", expand=True)
        self.obat_tab.add("Add Obat")
        self.obat_tab.add("View Obat")
        self.obat_tab.add("Edit Obat")
        self.obat_tab.add("Delete Obat")

        "Add Obat Tab"

        #ID
        self.id_label = CTkLabel(self.obat_tab.tab("Add Obat"), text="ID Obat", anchor=W, font=("Bahnschrift", 14))
        self.id_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.id_entry = CTkEntry(self.obat_tab.tab("Add Obat"), placeholder_text="Masukkan ID")
        self.id_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        #Name
        self.name_label = CTkLabel(self.obat_tab.tab("Add Obat"), anchor=W, text="Nama Obat", font=("Bahnschrift", 14))
        self.name_label.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

        self.name_entry = CTkEntry(self.obat_tab.tab("Add Obat"), placeholder_text="Masukkan Nama")
        self.name_entry.grid(row=1, column=2,  padx=10, pady=10, sticky="ew")

        #Manfaat
        self.manfaat_label = CTkLabel(self.obat_tab.tab("Add Obat"), text="Manfaat obat", anchor=W, font=("Bahnschrift", 14))
        self.manfaat_label.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.manfaat_entry = CTkTextbox(self.obat_tab.tab("Add Obat"))
        self.manfaat_entry.grid(row=3, column=0,  padx=10, pady=10, sticky="ew")

        #Cara
        self.cara_label = CTkLabel(self.obat_tab.tab("Add Obat"), text="Cara Penggunaan", anchor=W, font=("Bahnschrift", 14))
        self.cara_label.grid(row=2, column=2, padx=10, pady=10, sticky="ew")

        self.cara_entry = CTkTextbox(self.obat_tab.tab("Add Obat"))
        self.cara_entry.grid(row=3, column=2,  padx=10, pady=10, sticky="ew")

        #Submit
        self.submit_btn = CTkButton(self.obat_tab.tab("Add Obat"), text="Submit", command=self.insert_obat, hover_color="#2aa2c7", font=("Bahnschrift", 14))
        self.submit_btn.grid(row=1, column=4,  padx=10, pady=10, sticky="ew")

        "View Obat"

        headers = ["ID", "Name", "Manfaat", "Cara Peggunaan"]
        for col, header in enumerate(headers):
            label = CTkLabel(self.obat_tab.tab("View Obat"), text=header, font=("Bahnschrift", 14))
            label.grid(row=0, column=col, padx=2, pady=2)

        for i, name in enumerate(self.data_pasien, start=1):
            for col, value in enumerate(name):
                entry = CTkEntry(self.obat_tab.tab("View Obat"))
                entry.insert(END, value)
                entry.grid(row=i, column=col, padx=2, pady=2)

        "Edit Obat"

        self.edit_name_label = CTkLabel(self.obat_tab.tab("Edit Obat"), text="Name", font=("Bahnschrift", 14))
        self.edit_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.edit_name_entry = CTkEntry(self.obat_tab.tab("Edit Obat"), placeholder_text="Enter Name...")
        self.edit_name_entry.grid(row=0, column=1, padx=5,  pady=5, sticky="ew")

        self.column_label = CTkLabel(self.obat_tab.tab("Edit Obat"), text="Column", font=("Bahnschrift", 14))
        self.column_label.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.column_option = CTkOptionMenu(self.obat_tab.tab("Edit Obat"), values=["manfaat_obat", "cara_penggunaan"], button_hover_color="#2aa2c7")
        self.column_option.set("")
        self.column_option.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.edit_value_label = CTkLabel(self.obat_tab.tab("Edit Obat"), text="New Value", font=("Bahnschrift", 14))
        self.edit_value_label.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        self.edit_value_entry = CTkEntry(self.obat_tab.tab("Edit Obat"), placeholder_text="Enter Value...")
        self.edit_value_entry.grid(row=2, column=1, padx=5,  pady=5, sticky="ew")

        self.update_label = CTkLabel(self.obat_tab.tab("Edit Obat"), text="Update", font=("Bahnschrift", 14))
        self.update_label.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

        self.update_btn = CTkButton(self.obat_tab.tab("Edit Obat"), text="Update", command=self.update_obat_event, hover_color="#2aa2c7", font=("Bahnschrift", 14))
        self.update_btn.grid(row=3, column=1, padx=5, pady=5)

        "Delete Obat"

        self.del_name_label = CTkLabel(self.obat_tab.tab("Delete Obat"), text="Delete by name", font=("Bahnschrift", 14))
        self.del_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.del_name_entry = CTkEntry(self.obat_tab.tab("Delete Obat"), placeholder_text="Enter Name...")
        self.del_name_entry.grid(row=0, column=1, padx=5,  pady=5, sticky="ew")

        self.del_id_label = CTkLabel(self.obat_tab.tab("Delete Obat"), text="Delete by ID", font=("Bahnschrift", 14))
        self.del_id_label.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.del_id_entry = CTkEntry(self.obat_tab.tab("Delete Obat"), placeholder_text="Enter ID...")
        self.del_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.delete_btn = CTkButton(self.obat_tab.tab("Delete Obat"), text="Delete", command=self.delete_obat_event, hover_color="#2aa2c7", font=("Bahnschrift", 14))
        self.delete_btn.grid(row=2, column=1, padx=5, pady=5)

 

    def insert_obat(self):
        ID = self.id_entry.get()
        name = self.name_entry.get()
        manfaat = self.manfaat_entry.get(0.1, END)
        cara = self.cara_entry.get(0.1, END)

        if ID =="" or name=="" or manfaat=="" or cara== "":

            CTkMessagebox(title="Error !", message="Please enter full data", icon="cancel")

        else:
            columns = ("`id_product`", "`nama_product`", "`manfaat_obat`", "`cara_penggunaan`")
            values = [ID, name, manfaat, cara]
            self.insert("obat", columns, values)
            info_box = CTkMessagebox(title="Submitted !", message=f"Obat '{name}' successfully submited", icon="check", option_1="ok")

            if info_box.get() == "ok":
                return self.obat_frame_event()
            
    def delete_obat_event(self):
        name = self.del_name_entry.get()
        ID = self.del_id_entry.get()

        if name:
            self.delete("obat", "nama_product", name)

            info_box = CTkMessagebox(title="Updated !", message=f"Obat'{name}' successfully deleted", icon="check", option_1="ok")
            if info_box.get() == "ok":
                return self.obat_frame_event()

        elif ID:
            self.delete("obat", "id_product", ID)

            info_box = CTkMessagebox(title="Updated !", message=f"Obat'{ID}' successfully deleted", icon="check", option_1="ok")
            if info_box.get() == "ok":
                return self.obat_frame_event()
    
    def update_obat_event(self):
        column = self.column_option.get()
        value = self.edit_value_entry.get()
        name = self.edit_name_entry.get()

        if name =="" or column=="" or value=="":

            CTkMessagebox(title="Error !", message="Please enter complete fields", icon="cancel")

        else:

            column = self.column_option.get()
            value = self.edit_value_entry.get()
            name = self.edit_name_entry.get()
            self.update("obat", column, value, "nama_product", name)

            info_box = CTkMessagebox(title="Updated !", message=f"obat '{name}' successfully updated", icon="check", option_1="ok")
            if info_box.get() == "ok":
                return self.obat_frame_event()
