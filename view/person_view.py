from tkinter import *
import tkinter.messagebox as msg
from view.component import LabelAndEntry, Table
from controller.person_controller import *

class PersonView:
    def save_click(self):
        status, data = save(
            self.first_name.variable.get(),
            self.last_name.variable.get(),
            self.national_id.variable.get()
        )
        if status:
            msg.showinfo("ذخیره", f"عضو ذخیره شد\n{data}")
            self.reset_form()
        else:
            msg.showerror("خطا در ذخیره", f"خطا\n{data}")

    def edit_click(self):
        status, data = edit(
            self.id.variable.get(),
            self.first_name.variable.get(),
            self.last_name.variable.get(),
            self.national_id.variable.get()
        )
        if status:
            msg.showinfo("ویرایش", f"اطلاعات ویرایش شد\n{data}")
            self.reset_form()
        else:
            msg.showerror("خطا در ویرایش", f"خطا\n{data}")

    def remove_click(self):
        status, data = remove_by_id(self.id.variable.get())
        if status:
            msg.showinfo("حذف", f"عضو حذف شد\n{data}")
            self.reset_form()
        else:
            msg.showerror("خطا در حذف", f"خطا\n{data}")

    def select_table(self, selected_person):
        self.id.variable.set(selected_person[0])
        self.first_name.variable.set(selected_person[1])
        self.last_name.variable.set(selected_person[2])
        self.national_id.variable.set(selected_person[3])

    def reset_form(self):
        self.id.variable.set(0)
        self.first_name.variable.set("")
        self.last_name.variable.set("")
        self.national_id.variable.set("")
        status, person_list = find_all()
        self.table.refresh_table(person_list)

    def __init__(self):
        self.win = Toplevel()
        self.win.title("اطلاعات افراد")
        self.win.geometry("700x300")
        self.win.configure(bg="#f0f4f7")  # رنگ زمینه ملایم

        # ساخت ورودی‌ها با فونت ساده
        self.id = LabelAndEntry(self.win, "آیدی", 20, 20, data_type="int", state="readonly")
        self.first_name = LabelAndEntry(self.win, "نام", 20, 60)
        self.last_name = LabelAndEntry(self.win, "نام خانوادگی", 20, 100)
        self.national_id = LabelAndEntry(self.win, "کد ملی", 20, 140)

        # جدول
        self.table = Table(
            self.win,
            ["آیدی", "نام", "نام خانوادگی", "کد ملی"],
            [60, 120, 120, 100],
            250, 20,
            self.select_table
        )

        # دکمه‌ها با رنگ و فونت ساده
        Button(self.win, text="جدید", width=8, bg="#4caf50", fg="white", command=self.reset_form).place(x=20, y=180)
        Button(self.win, text="ذخیره", width=8, bg="#2196f3", fg="white", command=self.save_click).place(x=20, y=220)
        Button(self.win, text="ویرایش", width=8, bg="#ff9800", fg="white", command=self.edit_click).place(x=110, y=220)
        Button(self.win, text="حذف", width=8, bg="#f44336", fg="white", command=self.remove_click).place(x=200, y=220)

        self.reset_form()
        self.win.mainloop()
