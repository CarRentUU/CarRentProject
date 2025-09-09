from tkinter import *
from view.person_view import PersonView
from view.car_view import CarView
from view.rent_veiw import RentalView
from controller.car_controller import find_all

class FirstView:
    def open_person(self):
        PersonView()

    def open_car(self):
        CarView()

    def open_rent(self):
        RentalView()

    def __init__(self):
        self.win = Tk()
        self.win.title("سیستم اجاره خودرو 🚘")
        self.win.geometry("950x650")
        self.win.configure(bg="#ecf0f1")

        # ----- هدر بالا -----
        header = Frame(self.win, bg="#2c3e50", height=80)
        header.pack(side=TOP, fill=X)

        title = Label(
            header,
            text="🚗 سیستم اجاره خودرو",
            bg="#2c3e50",
            fg="white",
            font=("B Nazanin", 22, "bold"),
        )
        title.pack(side=LEFT, padx=20)

        # سبک دکمه‌ها
        btn_style = {
            "font": ("Arial", 12, "bold"),
            "bg": "#3498db",
            "fg": "white",
            "activebackground": "#2980b9",
            "activeforeground": "white",
            "bd": 0,
            "padx": 15,
            "pady": 8,
        }

        Button(header, text="ثبت نام 🧑", command=self.open_person, **btn_style).pack(side=RIGHT, padx=10)
        Button(header, text="ثبت خودرو 🚙", command=self.open_car, **btn_style).pack(side=RIGHT, padx=10)
        Button(header, text="اجاره خودرو 🔑", command=self.open_rent, **btn_style).pack(side=RIGHT, padx=10)

        # ----- بخش اصلی -----
        main_frame = Frame(self.win, bg="#ecf0f1")
        main_frame.pack(fill=BOTH, expand=True, pady=20)

        # گرفتن ماشین‌ها از دیتابیس
        status, car_list = find_all()
        if status and car_list:
            for car in car_list:
                self.create_car_card(main_frame, car)
        else:
            Label(main_frame, text="هیچ ماشینی ثبت نشده است 🚫", font=("Arial", 14), bg="#ecf0f1", fg="#7f8c8d").pack(pady=20)

        self.win.mainloop()

    def create_car_card(self, parent, car):
        frame = Frame(
            parent,
            relief=FLAT,
            bg="white",
            highlightbackground="#bdc3c7",
            highlightthickness=1
        )
        frame.pack(fill=X, padx=40, pady=10, ipadx=10, ipady=10)

        # برند و مدل + ایموجی
        Label(
            frame,
            text=f"🚘 {car.brand} {car.model}   (ID: {car.id})",
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#2c3e50"
        ).pack(anchor=W, padx=15, pady=5)

        # پلاک و رنگ
        info_text = f"پلاک: {car.license_plate}   |   رنگ: {car.color}"
        Label(
            frame,
            text=info_text,
            font=("Arial", 13),
            bg="white",
            fg="#7f8c8d"
        ).pack(anchor=W, padx=15, pady=5)
