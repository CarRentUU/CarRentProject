# ------------------- RentalView -------------------
from tkinter import *
import tkinter.messagebox as msg
from view.component import Table
from controller.rental_controller import *
from datetime import datetime

class RentalView:
    def save_click(self):
        now_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        status, data = save(
            int(self.person_entry.get()),
            int(self.car_entry.get()),
            now_date,
            None
        )
        if status:
            msg.showinfo("ذخیره", f"اجاره ثبت شد.\n{data}")
            self.reset_form()
        else:
            msg.showerror("خطا", f"امکان ثبت اجاره وجود ندارد.\n{data}")

    def return_click(self):
        now_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        status, data = return_rent(int(self.car_entry.get()), now_date)
        if status:
            msg.showinfo("بازگشت", f"خودرو بازگردانده شد.\n{data}")
            self.reset_form()
        else:
            msg.showerror("خطا", f"امکان بازگرداندن خودرو وجود ندارد.\n{data}")

    def edit_click(self):
        status, data = edit(
            int(self.id_entry.get()),
            int(self.person_entry.get()),
            int(self.car_entry.get()),
            self.rental_entry.get(),
            self.return_entry.get()
        )
        if status:
            msg.showinfo("ویرایش", f"اجاره ویرایش شد.\n{data}")
            self.reset_form()
        else:
            msg.showerror("خطا", f"امکان ویرایش وجود ندارد.\n{data}")

    def remove_click(self):
        status, data = remove_by_id(int(self.id_entry.get()))
        if status:
            msg.showinfo("حذف", f"اجاره حذف شد.\n{data}")
            self.reset_form()
        else:
            msg.showerror("خطا", f"امکان حذف وجود ندارد.\n{data}")

    def select_table(self, selected_rental):
        self.id_entry.delete(0, END)
        self.id_entry.insert(0, selected_rental[0])
        self.person_entry.delete(0, END)
        self.person_entry.insert(0, selected_rental[1])
        self.car_entry.delete(0, END)
        self.car_entry.insert(0, selected_rental[2])
        self.rental_entry.delete(0, END)
        self.rental_entry.insert(0, selected_rental[3])
        self.return_entry.delete(0, END)
        self.return_entry.insert(0, selected_rental[4])

    def reset_form(self):
        self.id_entry.configure(state=NORMAL)
        self.id_entry.delete(0, END)
        self.id_entry.insert(0, "0")
        self.id_entry.configure(state="readonly")

        self.person_entry.delete(0, END)
        self.car_entry.delete(0, END)
        self.rental_entry.delete(0, END)
        self.return_entry.delete(0, END)

        status, rental_list = find_all()
        self.table.refresh_table(rental_list)

    def __init__(self):
        self.win = Toplevel()
        self.win.title("ثبت اجاره خودرو")
        self.win.geometry("800x350")
        self.win.configure(bg="#f0f4f7")

        # فرم سمت چپ
        form_frame = Frame(self.win, padx=10, pady=10, bg="#f0f4f7")
        form_frame.pack(side=LEFT, fill=Y)

        Label(form_frame, text="آیدی").grid(row=0, column=0, sticky=E, pady=5)
        self.id_entry = Entry(form_frame, width=25)
        self.id_entry.grid(row=0, column=1, pady=5)
        self.id_entry.configure(state="readonly")

        Label(form_frame, text="آیدی فرد").grid(row=1, column=0, sticky=E, pady=5)
        self.person_entry = Entry(form_frame, width=25)
        self.person_entry.grid(row=1, column=1, pady=5)

        Label(form_frame, text="آیدی خودرو").grid(row=2, column=0, sticky=E, pady=5)
        self.car_entry = Entry(form_frame, width=25)
        self.car_entry.grid(row=2, column=1, pady=5)

        Label(form_frame, text="تاریخ اجاره").grid(row=3, column=0, sticky=E, pady=5)
        self.rental_entry = Entry(form_frame, width=25)
        self.rental_entry.grid(row=3, column=1, pady=5)
        self.rental_entry.configure(state="readonly", disabledbackground="#e0e0e0")

        Label(form_frame, text="تاریخ بازگشت").grid(row=4, column=0, sticky=E, pady=5)
        self.return_entry = Entry(form_frame, width=25)
        self.return_entry.grid(row=4, column=1, pady=5)
        self.return_entry.configure(state="readonly", disabledbackground="#e0e0e0")

        # دکمه‌ها
        btn_frame = Frame(form_frame, pady=10, bg="#f0f4f7")
        btn_frame.grid(row=5, column=0, columnspan=2)

        Button(btn_frame, text="جدید", width=10, bg="#4caf50", fg="white", command=self.reset_form).grid(row=0, column=0, padx=5, pady=5)
        Button(btn_frame, text="ذخیره", width=10, bg="#2196f3", fg="white", command=self.save_click).grid(row=0, column=1, padx=5, pady=5)
        Button(btn_frame, text="ویرایش", width=10, bg="#ff9800", fg="white", command=self.edit_click).grid(row=0, column=2, padx=5, pady=5)
        Button(btn_frame, text="حذف", width=10, bg="#f44336", fg="white", command=self.remove_click).grid(row=0, column=3, padx=5, pady=5)
        Button(btn_frame, text="بازگشت", width=10, bg="#607d8b", fg="white", command=self.return_click).grid(row=1, column=1, padx=5, pady=5)

        # جدول سمت راست
        table_frame = Frame(self.win, padx=10, pady=10, bg="#f0f4f7")
        table_frame.pack(side=RIGHT, fill=BOTH, expand=True)

        self.table = Table(
            table_frame,
            ["آیدی", "آیدی فرد", "آیدی خودرو", "تاریخ اجاره", "تاریخ بازگشت"],
            [60, 100, 100, 120, 120],
            0, 0,
            self.select_table
        )

        self.reset_form()
        self.win.mainloop()
