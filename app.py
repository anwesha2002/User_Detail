import tkinter as tk
from tkinter import ttk
from datetime import datetime
import csv


class SubDealerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IPL 2024")


        # Dropdown menu (Selection)
        self.selection_label = tk.Label(root, text="Distributor:")
        self.selection_label.grid(row=0, column=0, padx=10, pady=10)
        self.selection_var = tk.StringVar()
        self.selection_dropdown = ttk.Combobox(root, textvariable=self.selection_var)
        self.selection_dropdown['values'] = ('Option 1', 'Option 2', 'Option 3')
        self.selection_dropdown.grid(row=0, column=1, padx=10, pady=10)

        # Subdealer Code
        self.code_label = tk.Label(root, text="Subdealer Code:")
        self.code_label.grid(row=1, column=0, padx=10, pady=10)
        self.code_entry = tk.Entry(root)
        self.code_entry.grid(row=1, column=1, padx=10, pady=10)

        # Subdealer Name
        self.name_label = tk.Label(root, text="Subdealer Name:")
        self.name_label.grid(row=2, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=2, column=1, padx=10, pady=10)

        # Scheme 1
        self.scheme1_label = tk.Label(root, text="Scheme 1:")
        self.scheme1_label.grid(row=3, column=0, padx=10, pady=10)
        self.scheme1_entry = tk.Entry(root)
        self.scheme1_entry.grid(row=3, column=1, padx=10, pady=10)

        # Scheme 2
        self.scheme2_label = tk.Label(root, text="Scheme 2:")
        self.scheme2_label.grid(row=4, column=0, padx=10, pady=10)
        self.scheme2_entry = tk.Entry(root)
        self.scheme2_entry.grid(row=4, column=1, padx=10, pady=10)

        # Scheme 3
        self.scheme3_label = tk.Label(root, text="Scheme 3:")
        self.scheme3_label.grid(row=5, column=0, padx=10, pady=10)
        self.scheme3_entry = tk.Entry(root)
        self.scheme3_entry.grid(row=5, column=1, padx=10, pady=10)

        # Date and Time
        self.datetime_label = tk.Label(root, text="Date and Time:")
        self.datetime_label.grid(row=6, column=0, padx=10, pady=10)
        self.datetime_value = tk.Label(root, text=self.get_current_datetime())
        self.datetime_value.grid(row=6, column=1, padx=10, pady=10)

        # Update Date and Time every second
        self.update_datetime()

        # Submit Button
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=7, column=0, columnspan=2, pady=10)

    def get_current_datetime(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def update_datetime(self):
        self.datetime_value.config(text=self.get_current_datetime())
        self.root.after(1000, self.update_datetime)

    # def storing_data(self):
    #     with open() as file:
    #         reader = csv.reader()
    #
    #     # firebase = pyrebase.initialize_app(self.config)
    #     # storage = firebase.storage()
    #     #
    #     # storage.child("Store/submissions_IPL_2024.csv").put(r/"C:/Users/ANWESHA/Downloads/submissions_IPL_2024.csv")

    def submit_form(self):
        data = {
            "Selection": self.selection_var.get(),
            "Subdealer Code": self.code_entry.get(),
            "Subdealer Name": self.name_entry.get(),
            "Scheme 1": self.scheme1_entry.get(),
            "Scheme 2": self.scheme2_entry.get(),
            "Scheme 3": self.scheme3_entry.get(),
            "Date and Time": self.get_current_datetime()
        }

        with open('submissions_IPL_2024.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data.keys())

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # self.storing_data()

        print("Form Data Submitted:", data)

if __name__ == "__main__":
    root = tk.Tk()
    app = SubDealerApp(root)
    root.mainloop()
