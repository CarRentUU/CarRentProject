import re
from datetime import datetime, time


def name_validator(name, massage):
    if type(name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", name):
        return name
    else:
        raise ValueError(massage)

def brand_validator(brand,massage):
    if type(brand) == str and re.match(r"^[a-zA-Z\s\d]{3,30}$", brand):
        return brand
    else:
        raise ValueError(massage)


def type_validator(type):
    if type(type) == str and re.match(r"^[a-zA-Z\s]{3,30}$", type):
        return type
    else:
        raise ValueError("Invalid type !!!")


def amount_validator(amount):
    if type(amount) == int and amount > 0:
        return amount
    else:
        raise ValueError("Invalid amount !!!")


def time_validator(time):
    try:
        if type(time) == datetime:
            return datetime.strptime(time, "%H:%M ").time()
    except:
        raise ValueError("Invalid Time !!!")

def date_validator(date):
    try:
        if type(date) == str:
            return datetime.strptime(date, "%Y-%m-%d").date()
    except:
        raise ValueError("Invalid date !!!")

def national_id_validator(national_id,massage):
    if type(national_id) == str and re.match(r"^[0-9]{10}$", national_id):
        return national_id
    else :
        raise ValueError(massage)

def license_plate_validator(license_plate,masssage):

    if type(license_plate) == str and re.match(r"^\d{10}$", license_plate):
        return license_plate
    else:
        raise ValueError(masssage)




