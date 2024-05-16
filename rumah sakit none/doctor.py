from customtkinter import *
from database import database
from CTkMessagebox import CTkMessagebox


class doctor(database):
        
    def doctor_frame_event(self):

        #Fetch Data
        self.data_doctor = self.select_all("doctor")

        #Destroy any active frame
        for frames in self.right_frame.winfo_children():
            frames.destroy()

        # locked_frame = access_doctor()

        self.doctor_tab = CTkTabview(self.right_frame, anchor=W)
        self.doctor_tab.pack(side=LEFT, fill="both", expand=True)
        self.doctor_tab.add("Search Doctor")
        self.doctor_tab.add("Add Doctor")
        self.doctor_tab.add("View Doctor")
        self.doctor_tab.add("Edit Doctor")
        self.doctor_tab.add("Delete Doctor")

        #ID
        self.id_label = CTkLabel(self.doctor_tab.tab("Add Doctor"), text="ID", anchor="center", font=("Bahnschrift", 14))
        self.id_label.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.id_entry = CTkEntry(self.doctor_tab.tab("Add Doctor"), placeholder_text="please enter ID")
        self.id_entry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        #Name
        self.name_label = CTkLabel(self.doctor_tab.tab("Add Doctor"), anchor="center", text="Name", font=("Bahnschrift", 14))
        self.name_label.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.name_entry = CTkEntry(self.doctor_tab.tab("Add Doctor"), placeholder_text="Please enter name")
        self.name_entry.grid(row=1, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        #Specialis
        self.specialis_label = CTkLabel(self.doctor_tab.tab("Add Doctor"), text="Specialis", font=("Bahnschrift", 14))
        self.specialis_label.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        self.specialis_entry = CTkEntry(self.doctor_tab.tab("Add Doctor"), placeholder_text="Please enter specialis")
        self.specialis_entry.grid(row=2, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        #Jam
        self.jam_label = CTkLabel(self.doctor_tab.tab("Add Doctor"), anchor="center",text="Jam", font=("Bahnschrift", 14))
        self.jam_label.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

        self.jam_entry = CTkEntry(self.doctor_tab.tab("Add Doctor"), placeholder_text="Please enter jam")
        self.jam_entry.grid(row=3, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        #Submit
        self.submit_btn = CTkButton(self.doctor_tab.tab("Add Doctor"), text="Submit", command=self.submit_doctor, hover_color="#2aa2c7", font=("Bahnschrift", 14))
        self.submit_btn.grid(row=3, column=4, padx=20, pady=20)

        "Search Doctor"

        #Specialis
        self.search_specialis_label = CTkLabel(self.doctor_tab.tab("Search Doctor"), text="Search Specialis", font=("Bahnschrift", 14))
        self.search_specialis_label.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        self.search_specialis_entry = CTkEntry(self.doctor_tab.tab("Search Doctor"), placeholder_text="Search...")
        self.search_specialis_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        self.search_specialis_btn = CTkButton(self.doctor_tab.tab("Search Doctor"), text="search", command=self.search_specialis, hover_color="#2aa2c7", font=("Bahnschrift", 14))
        self.search_specialis_btn.grid(row=2, column=3, padx=20, pady=20)

        #Jam
        self.search_jam_label = CTkLabel(self.doctor_tab.tab("Search Doctor"), text="Search Jam", font=("Bahnschrift", 14))
        self.search_jam_label.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

        self.search_jam_entry = CTkEntry(self.doctor_tab.tab("Search Doctor"), placeholder_text="Search...")
        self.search_jam_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        self.search_jam_btn = CTkButton(self.doctor_tab.tab("Search Doctor"), text="search", command=self.search_jam, hover_color="#2aa2c7", font=("Bahnschrift", 14))
        self.search_jam_btn.grid(row=3, column=3, padx=20, pady=20)

        "View Doctor"

        headers = ["ID", "Name", "Specialis"]
        for col, header in enumerate(headers):
            label = CTkLabel(self.doctor_tab.tab("View Doctor"), text=header, font=("Bahnschrift", 14))
            label.grid(row=0, column=col, padx=2, pady=2)

        for i, name in enumerate(self.data_doctor, start=1):
            for col, value in enumerate(name):
                entry = CTkEntry(self.doctor_tab.tab("View Doctor"))
                entry.insert(END, value)
                entry.grid(row=i, column=col, padx=2, pady=2)

        "Edit Doctor"

        self.edit_name_label = CTkLabel(self.doctor_tab.tab("Edit Doctor"), text="Name", font=("Bahnschrift", 14))
        self.edit_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.edit_name_entry = CTkEntry(self.doctor_tab.tab("Edit Doctor"), placeholder_text="Enter Name...")
        self.edit_name_entry.grid(row=0, column=1, padx=5,  pady=5, sticky="ew")

        self.column_label = CTkLabel(self.doctor_tab.tab("Edit Doctor"), text="Column", font=("Bahnschrift", 14))
        self.column_label.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.column_option = CTkOptionMenu(self.doctor_tab.tab("Edit Doctor"), values=["Name", "Specialty", "Jam"], button_hover_color="#2aa2c7")
        self.column_option.set("")
        self.column_option.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.edit_value_label = CTkLabel(self.doctor_tab.tab("Edit Doctor"), text="New Value", font=("Bahnschrift", 14))
        self.edit_value_label.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        self.edit_value_entry = CTkEntry(self.doctor_tab.tab("Edit Doctor"), placeholder_text="Enter Value...")
        self.edit_value_entry.grid(row=2, column=1, padx=5,  pady=5, sticky="ew")

        self.update_label = CTkLabel(self.doctor_tab.tab("Edit Doctor"), text="Update", font=("Bahnschrift", 14))
        self.update_label.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

        self.update_btn = CTkButton(self.doctor_tab.tab("Edit Doctor"), text="Update", command=self.update_doctor_event, hover_color="#2aa2c7", font=("Bahnschrift", 14))
        self.update_btn.grid(row=3, column=1, padx=5, pady=5)

        "Delete Doctor"

        self.del_name_label = CTkLabel(self.doctor_tab.tab("Delete Doctor"), text="Delete by name", font=("Bahnschrift", 14))
        self.del_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.del_name_entry = CTkEntry(self.doctor_tab.tab("Delete Doctor"), placeholder_text="Enter Name...")
        self.del_name_entry.grid(row=0, column=1, padx=5,  pady=5, sticky="ew")

        self.del_id_label = CTkLabel(self.doctor_tab.tab("Delete Doctor"), text="Delete by ID", font=("Bahnschrift", 14))
        self.del_id_label.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.del_id_entry = CTkEntry(self.doctor_tab.tab("Delete Doctor"), placeholder_text="Enter ID...")
        self.del_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.delete_btn = CTkButton(self.doctor_tab.tab("Delete Doctor"), text="Delete", command=self.delete_doctor_event, hover_color="#2aa2c7", font=("Bahnschrift", 14))
        self.delete_btn.grid(row=2, column=1, padx=5, pady=5)

    def search_specialis(self):
        headers = ["ID", "Name", "Specialis", "Jam"]
        for col, header in enumerate(headers):
            label = CTkLabel(self.doctor_tab.tab("Search Doctor"), text=header, font=("Bahnschrift", 14))
            label.grid(row=5, column=col, padx=2, pady=2)

        value = self.search_specialis_entry.get()
        doctor_result = self.select("doctor", "Specialty", value)
        print(doctor_result)

        for i, name in enumerate(doctor_result, start=1):
            for col, value in enumerate(name):
                entry = CTkEntry(self.doctor_tab.tab("Search Doctor"))
                entry.insert(END, value)
                entry.grid(row=i+6, column=col, padx=2, pady=2)

                edit_btn = CTkButton(self.doctor_tab.tab("Search Doctor"), text="Edit")
                edit_btn.grid(row=i+6, column=col+1, padx=2, pady=2)

    def search_jam(self):
        headers = ["ID", "Name", "Specialis", "Jam"]
        for col, header in enumerate(headers):
            label = CTkLabel(self.doctor_tab.tab("Search Doctor"), text=header, font=("Bahnschrift", 14))
            label.grid(row=5, column=col, padx=2, pady=2)

        value = self.search_jam_entry.get()
        doctor_result = self.select("doctor", "Jam", value)
        print(doctor_result)

        for i, name in enumerate(doctor_result, start=1):
            for col, value in enumerate(name):
                entry = CTkEntry(self.doctor_tab.tab("Search Doctor"))
                entry.insert(END, value)
                entry.grid(row=i+6, column=col, padx=2, pady=2)

                edit_btn = CTkButton(self.doctor_tab.tab("Search Doctor"), text="Edit")
                edit_btn.grid(row=i+6, column=col+1, padx=2, pady=2)


    def submit_doctor(self):
        ID = self.id_entry.get()
        name = self.name_entry.get()
        specialis = self.specialis_entry.get()
        jam = self.jam_entry.get()
   

        if ID =="" or name=="" or specialis=="":

            CTkMessagebox(title="Error !", message="Please enter full data", icon="cancel")

        else:
            columns = ("`Id_Doctor`", "`Name`", "`Specialty`", "`Jam`")
            values = [ID, name, specialis, jam]
            self.insert("doctor", columns, values)
            info_box = CTkMessagebox(title="Submitted !", message=f"Doctor '{name}' successfully submited", icon="check", option_1="ok")

            if info_box.get() == "ok":
                return self.doctor_frame_event()
            
    def update_doctor_event(self):
        column = self.column_option.get()
        value = self.edit_value_entry.get()
        name = self.edit_name_entry.get()

        if name =="" or column=="" or value=="":

            CTkMessagebox(title="Error !", message="Please enter complete fields", icon="cancel")

        else:

            column = self.column_option.get()
            value = self.edit_value_entry.get()
            name = self.edit_name_entry.get()
            self.update("doctor", column, value, "Name", name)

            info_box = CTkMessagebox(title="Updated !", message=f"Doctor '{name}' successfully updated", icon="check", option_1="ok")
            if info_box.get() == "ok":
                return self.doctor_frame_event()
            
    def delete_doctor_event(self):
        name = self.del_name_entry.get()
        ID = self.del_id_entry.get()

        if name:
            self.delete("doctor", "Name", name)

            info_box = CTkMessagebox(title="Updated !", message=f"Doctor '{name}' successfully deleted", icon="check", option_1="ok")
            if info_box.get() == "ok":
                return self.doctor_frame_event()

        elif ID:
            self.delete("doctor", "Id_Doctor", ID)

            info_box = CTkMessagebox(title="Updated !", message=f"Doctor '{ID}' successfully deleted", icon="check", option_1="ok")
            if info_box.get() == "ok":
                return self.doctor_frame_event()



