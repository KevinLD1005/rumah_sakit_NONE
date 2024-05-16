from customtkinter import *
from database import database
from CTkMessagebox import CTkMessagebox


class pasien(database):
        
    def pasien_frame_event(self):

        # #Destroy any active frame
        for frames in self.right_frame.winfo_children():
            frames.destroy()

        #Fetch Data
        self.data_pasien = self.select_all("pasien")

        self.pasien_tab = CTkTabview(self.right_frame, anchor=W)
        self.pasien_tab.pack(side=LEFT, fill="both", expand=True)
        self.pasien_tab.add("Add Pasien")
        self.pasien_tab.add("View Pasien")
        self.pasien_tab.add("Search Pasien")
        self.pasien_tab.add("Edit Pasien")
        self.pasien_tab.add("Delete Pasien")

        "Add Pasien Tab"

        #Name 
        self.name_label = CTkLabel(self.pasien_tab.tab("Add Pasien"), text="Name", anchor="center", font=("Bahnschrift", 14))
        self.name_label.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.name_entry = CTkEntry(self.pasien_tab.tab("Add Pasien"), placeholder_text="please enter fullname")
        self.name_entry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        #Age 
        self.age_label = CTkLabel(self.pasien_tab.tab("Add Pasien"), anchor="center", text="Age", font=("Bahnschrift", 14))
        self.age_label.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.age_entry = CTkEntry(self.pasien_tab.tab("Add Pasien"), placeholder_text="Please enter age")
        self.age_entry.grid(row=1, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        #Gender
        self.gender_label = CTkLabel(self.pasien_tab.tab("Add Pasien"), text="Gender", anchor="center", font=("Bahnschrift", 14))
        self.gender_label.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        #Gender Radio Buttons
        self.genderVar = StringVar(value="")

        self.male_radio_btn = CTkRadioButton(self.pasien_tab.tab("Add Pasien"), text="Male", variable=self.genderVar, value="Male")
        self.male_radio_btn.grid(row=2, column=1, padx=20, pady=20, sticky="ew")

        self.female_radio_btn = CTkRadioButton(self.pasien_tab.tab("Add Pasien"),text="Female", variable=self.genderVar, value="Female")
        self.female_radio_btn.grid(row=2, column=2, padx=20, pady=20, sticky="ew")

        #Blood Type
        self.blood_type_label = CTkLabel(self.pasien_tab.tab("Add Pasien"), text="Blood Type", font=("Bahnschrift", 14))
        self.blood_type_label.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

        self.blood_type_entry = CTkEntry(self.pasien_tab.tab("Add Pasien"), placeholder_text="Please enter blood type")
        self.blood_type_entry.grid(row=3, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        #Condition
        self.condition_label = CTkLabel(self.pasien_tab.tab("Add Pasien"), text="Condition", font=("Bahnschrift", 14))
        self.condition_label.grid(row=4, column=0, padx=20, pady=20, sticky="ew")

        self.condition_entry = CTkEntry(self.pasien_tab.tab("Add Pasien"), placeholder_text="Please enter condition")
        self.condition_entry.grid(row=4, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        # Occupation Label
        self.status_label = CTkLabel(self.pasien_tab.tab("Add Pasien"), text="Status", font=("Bahnschrift", 14))
        self.status_label.grid(row=5, column=0, padx=20, pady=20, sticky="ew")

        # Occupation combo box
        self.status_option = CTkOptionMenu(self.pasien_tab.tab("Add Pasien"), values=["Sudah Sembuh", "Belum Sembuh"], button_hover_color="#2aa2c7")
        self.status_option.set("")
        self.status_option.grid(row=5, column=1, padx=20, pady=20, columnspan=2, sticky="ew")

        #Submit
        self.submit_btn = CTkButton(self.pasien_tab.tab("Add Pasien"), text="Submit", command=self.submit_pasien, hover_color="#2aa2c7", font=("Bahnschrift", 14))
        self.submit_btn.grid(row=5, column=3, padx=20, pady=20)

        "View Pasien"

        headers = ["ID", "Name", "Age", "Sex", "Blood Type", "Condition", "Status"]
        for col, header in enumerate(headers):
            label = CTkLabel(self.pasien_tab.tab("View Pasien"), text=header, font=("Bahnschrift", 14))
            label.grid(row=0, column=col, padx=2, pady=2)

        for i, name in enumerate(self.data_pasien, start=1):
            for col, value in enumerate(name):
                entry = CTkEntry(self.pasien_tab.tab("View Pasien"))
                entry.insert(END, value)
                entry.grid(row=i, column=col, padx=2, pady=2)

        "Search Pasien"

        self.search_name_label = CTkLabel(self.pasien_tab.tab("Search Pasien"), text="Search by name", font=("Bahnschrift", 14))
        self.search_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.search_name_entry = CTkEntry(self.pasien_tab.tab("Search Pasien"), placeholder_text="Enter Name...")
        self.search_name_entry.grid(row=0, column=1, padx=5,  pady=5, sticky="ew")

        self.search_name_btn = CTkButton(self.pasien_tab.tab("Search Pasien"), text="search", command=self.search_name_event, hover_color="#2aa2c7", font=("Bahnschrift", 14))
        self.search_name_btn.grid(row=0, column=2, padx=5, pady=5)

        self.search_id_label = CTkLabel(self.pasien_tab.tab("Search Pasien"), text="Search by ID", font=("Bahnschrift", 14))
        self.search_id_label.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.search_id_entry = CTkEntry(self.pasien_tab.tab("Search Pasien"), placeholder_text="Enter ID...")
        self.search_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.search_id_btn = CTkButton(self.pasien_tab.tab("Search Pasien"), text="search", command=self.search_id_event, hover_color="#2aa2c7", font=("Bahnschrift", 14))
        self.search_id_btn.grid(row=1, column=2, padx=5, pady=5)

        "Edit Pasien"

        self.edit_name_label = CTkLabel(self.pasien_tab.tab("Edit Pasien"), text="Name", font=("Bahnschrift", 14))
        self.edit_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.edit_name_entry = CTkEntry(self.pasien_tab.tab("Edit Pasien"), placeholder_text="Enter Name...")
        self.edit_name_entry.grid(row=0, column=1, padx=5,  pady=5, sticky="ew")

        self.column_label = CTkLabel(self.pasien_tab.tab("Edit Pasien"), text="Column", font=("Bahnschrift", 14))
        self.column_label.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.column_option = CTkOptionMenu(self.pasien_tab.tab("Edit Pasien"), values=["Age", "Condition", "Status"], button_hover_color="#2aa2c7")
        self.column_option.set("")
        self.column_option.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.edit_value_label = CTkLabel(self.pasien_tab.tab("Edit Pasien"), text="New Value", font=("Bahnschrift", 14))
        self.edit_value_label.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        self.edit_value_entry = CTkEntry(self.pasien_tab.tab("Edit Pasien"), placeholder_text="Enter Value...")
        self.edit_value_entry.grid(row=2, column=1, padx=5,  pady=5, sticky="ew")

        self.update_label = CTkLabel(self.pasien_tab.tab("Edit Pasien"), text="Update", font=("Bahnschrift", 14))
        self.update_label.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

        self.update_btn = CTkButton(self.pasien_tab.tab("Edit Pasien"), text="Update", command=self.update_btn_event, hover_color="#2aa2c7", font=("Bahnschrift", 14))
        self.update_btn.grid(row=3, column=1, padx=5, pady=5)

        "Delete Pasien"

        self.del_name_label = CTkLabel(self.pasien_tab.tab("Delete Pasien"), text="Delete by name", font=("Bahnschrift", 14))
        self.del_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.del_name_entry = CTkEntry(self.pasien_tab.tab("Delete Pasien"), placeholder_text="Enter Name...")
        self.del_name_entry.grid(row=0, column=1, padx=5,  pady=5, sticky="ew")

        self.del_id_label = CTkLabel(self.pasien_tab.tab("Delete Pasien"), text="Delete by ID", font=("Bahnschrift", 14))
        self.del_id_label.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.del_id_entry = CTkEntry(self.pasien_tab.tab("Delete Pasien"), placeholder_text="Enter ID...")
        self.del_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.delete_btn = CTkButton(self.pasien_tab.tab("Delete Pasien"), text="Delete", command=self.delete_btn_event, hover_color="#2aa2c7", font=("Bahnschrift", 14))
        self.delete_btn.grid(row=2, column=1, padx=5, pady=5)


    def submit_pasien(self):
        
        name = self.name_entry.get()
        age = self.age_entry.get()
        sex = self.genderVar.get()
        Btype = self.blood_type_entry.get()
        condition = self.condition_entry.get()
        status = self.status_option.get()

        if name =="" or age=="" or sex=="" or Btype=="" or condition=="" or status=="":

            CTkMessagebox(title="Error !", message="Please enter full data", icon="cancel")

        else:
            default_ID = str(1 + len(self.data_pasien))
            add_ID = default_ID.zfill(4) 
            columns = ("`ID`", "`Name`", "`Age`", "`Sex`", "`Blood Type`", "`Condition`", "`Status`")
            values = (add_ID, name, age, sex, Btype, condition, status)
            self.insert("pasien", columns, values)
            info_box = CTkMessagebox(title="Submitted !", message=f"Pasien '{name}' successfully submited", icon="check", option_1="ok")

            if info_box.get() == "ok":
                return self.pasien_frame_event()
            
            print(name, age, sex, Btype, condition, status)

    def search_name_event(self):
        headers = ["ID", "Name", "Age", "Sex", "Blood Type", "Condition", "Status"]
        for col, header in enumerate(headers):
            label = CTkLabel(self.pasien_tab.tab("Search Pasien"), text=header, font=("Bahnschrift", 14))
            label.grid(row=5, column=col, padx=2, pady=2)

        value = self.search_name_entry.get()
        pasien_result = self.select("pasien", "Name", value)
        print(pasien_result)

        for i, name in enumerate(pasien_result, start=1):
            for col, value in enumerate(name):
                entry = CTkEntry(self.pasien_tab.tab("Search Pasien"))
                entry.insert(END, value)
                entry.grid(row=i+6, column=col, padx=2, pady=2)

    def search_id_event(self):
        headers = ["ID", "Name", "Age", "Sex", "Blood Type", "Condition", "Status"]
        for col, header in enumerate(headers):
            label = CTkLabel(self.pasien_tab.tab("Search Pasien"), text=header, font=("Bahnschrift", 14))
            label.grid(row=5, column=col, padx=2, pady=2)

        value = self.search_id_entry.get()
        pasien_result = self.select("pasien", "ID", value)
        print(pasien_result)

        for i, name in enumerate(pasien_result, start=1):
            for col, value in enumerate(name):
                entry = CTkEntry(self.pasien_tab.tab("Search Pasien"))
                entry.insert(END, value)
                entry.grid(row=i+6, column=col, padx=2, pady=2)

    def update_btn_event(self):
        column = self.column_option.get()
        value = self.edit_value_entry.get()
        name = self.edit_name_entry.get()

        if name =="" or column=="" or value=="":

            CTkMessagebox(title="Error !", message="Please enter complete fields", icon="cancel")

        else:

            column = self.column_option.get()
            value = self.edit_value_entry.get()
            name = self.edit_name_entry.get()
            self.update("pasien", column, value, "Name", name)

            info_box = CTkMessagebox(title="Updated !", message=f"Pasien '{name}' successfully updated", icon="check", option_1="ok")
            if info_box.get() == "ok":
                return self.pasien_frame_event()
            
    def delete_btn_event(self):
        name = self.del_name_entry.get()
        ID = self.del_id_entry.get()

        if name:
            self.delete("pasien", "Name", name)

            info_box = CTkMessagebox(title="Updated !", message=f"Pasien '{name}' successfully deleted", icon="check", option_1="ok")
            if info_box.get() == "ok":
                return self.pasien_frame_event()

        elif ID:
            self.delete("pasien", "ID", ID)

            info_box = CTkMessagebox(title="Updated !", message=f"Pasien '{ID}' successfully deleted", icon="check", option_1="ok")
            if info_box.get() == "ok":
                return self.pasien_frame_event()

        


    
    

        



