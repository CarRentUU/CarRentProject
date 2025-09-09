from tkinter import *
import tkinter.messagebox as msg
from view.component import *
from controller.car_controller import *

class CarView:
    def save_click(self):
        status, data = save(
            self.brand.variable.get(),
            self.model.variable.get(),
            self.license_plate.variable.get(),
            self.color.variable.get()
        )
        if status:
            msg.showinfo("ذخیره", f"ماشین ذخیره شد\n{data}")
            self.reset_form()
        else:
            msg.showerror("خطا در ذخیره", f"اشتباه!\n{data}")

    def edit_click(self):
        status, data = edit(
            self.id.variable.get(),
            self.brand.variable.get(),
            self.model.variable.get(),
            self.license_plate.variable.get(),
            self.color.variable.get()
        )
        if status:
            msg.showinfo("ویرایش", f"ماشین ویرایش شد\n{data}")
            self.reset_form()
        else:
            msg.showerror("خطا در ویرایش", f"اشتباه!\n{data}")

    def remove_click(self):
        status, data = remove_by_id(self.id.variable.get())
        if status:
            msg.showinfo("حذف", f"ماشین حذف شد\n{data}")
            self.reset_form()
        else:
            msg.showerror("خطا در حذف", f"اشتباه!\n{data}")

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
        self.win.title("مدیریت ماشین‌ها")
        self.win.geometry("775x300")

        self.id = LabelAndEntry(self.win, "شناسه", 20, 20, data_type="int", state="readonly")
        self.brand = LabelAndEntry(self.win, "برند", 20, 60)
        self.model = LabelAndEntry(self.win, "مدل", 20, 100)
        self.license_plate = LabelAndEntry(self.win, "پلاک", 20, 140)
        self.color = LabelAndEntry(self.win, "رنگ", 20, 180)

        self.table = Table(
            self.win,
            ["شناسه", "برند", "مدل", "پلاک", "رنگ"],
            [60, 100, 100, 150, 100],
            250, 40,
            self.select_table
        )

        # دکمه‌ها با متن فارسی و رنگ پس‌زمینه
        Button(self.win, text="جدید", width=7, bg="#2196F3", fg="white", command=self.reset_form).place(x=20, y=220)
        Button(self.win, text="ذخیره", width=7, bg="#4CAF50", fg="white", command=self.save_click).place(x=20, y=260)
        Button(self.win, text="ویرایش", width=7, bg="#FFC107", fg="black", command=self.edit_click).place(x=90, y=260)
        Button(self.win, text="حذف", width=7, bg="#F44336", fg="white", command=self.remove_click).place(x=160, y=260)

        self.reset_form()

        self.win.mainloop()
