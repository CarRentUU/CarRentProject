from tkinter import *
import tkinter.messagebox as msg
from view.component import *
from controller.car_controller import *

class CarView:
    def save_click(self):
        status, data = save(self.brand.variable.get(), self.model.variable.get(),self.license_plate.variable.get(),self.color.variable.get())
        if status:
            msg.showinfo("Save", f"Car Saved\n{data}")
            self.reset_form()
        else:
            msg.showerror("Save Error", f"Error\n{data}")

    def edit_click(self):
        status, data = edit(self.id.variable.get(),self.brand.variable.get(), self.model.variable.get(),self.license_plate.variable.get(),self.color.variable.get())
        if status:
            msg.showinfo("Edit", f"Car Edited\n{data}")
            self.reset_form()
        else:
            msg.showerror("Edit Error", f"Error\n{data}")

    def remove_click(self):
        status, data = remove_by_id(self.id.variable.get())
        if status:
            msg.showinfo("Remove", f"Car Removed\n{data}")
            self.reset_form()
        else:
            msg.showerror("Remove Error", f"Error\n{data}")

    def select_table(self, selected_Car):
        self.id.variable.set(selected_Car[0])
        self.brand.variable.set(selected_Car[1])
        self.model.variable.set(selected_Car[2])
        self.license_plate.variable.set(selected_Car[3])
        self.color.variable.set(selected_Car[4])

    def reset_form(self):
        self.id.variable.set(0)
        self.brand.variable.set("")
        self.model.variable.set("")
        self.license_plate.variable.set("")
        self.color.variable.set("")
        status, car_list = find_all()
        self.table.refresh_table(car_list)

    def __init__(self):
        self.win = Toplevel()
        self.win.title("Car Info")
        self.win.geometry("775x300")

        self.id = LabelAndEntry(self.win, "Id", 20,20, data_type="int", state="readonly")
        self.brand = LabelAndEntry(self.win, "Brand", 20, 60)
        self.model = LabelAndEntry(self.win, "Model", 20, 100)
        self.license_plate = LabelAndEntry(self.win, "License_Plate", 20, 140)
        self.color = LabelAndEntry(self.win, "Color", 20, 180)

        self.table = Table(
            self.win,
            ["Id", "Brand", "Model","License_Plate","Color"],
            [60,100,100,150,100],
            250,40,
            self.select_table
        )

        Button(self.win, text="New", width= 7, command=self.reset_form).place(x=20,y=220)
        Button(self.win, text="Save", width= 7, command=self.save_click).place(x=20,y=260)
        Button(self.win, text="Edit", width= 7, command=self.edit_click).place(x=90,y=260)
        Button(self.win, text="Remove", width= 7, command=self.remove_click).place(x=160,y=260)

        self.reset_form()

        self.win.mainloop()
