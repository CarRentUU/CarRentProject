from model.da.da import DataAccess
from model.entity import Car, Logger


def save(brand, model,license_plate,color):
    try:
        car = Car(brand, model,license_plate,color)

        car_da = DataAccess(Car)
        car_da.save(car)
        Logger.info(f"Car {car} Saved")
        return True, car
    except Exception as e:
        Logger.error(f"{e} - Not Saved")
        return False, f"{e}"


def edit(id, brand, model,license_plate,color):
    try:
        car = Car(brand, model,license_plate,color)
        car.id = id

        car_da = DataAccess(Car)
        car_da.edit(car)
        Logger.info(f"Car {car} Edited")
        return True, car
    except Exception as e:
        Logger.error(f"{e} - Not Edited")
        return False, f"{e}"


def remove_by_id(id):
    try:
        car_da = DataAccess(Car)
        car = car_da.remove_by_id(id)

        Logger.info(f"car {car} Removed")
        return True, car
    except Exception as e:
        Logger.error(f"{e} - Not Removed")
        return False, f"{e}"


def find_all():
    try:
        car_da = DataAccess(Car)
        car_list = car_da.find_all()
        Logger.info(f"Car FindALL")
        return True, car_list
    except Exception as e:
        Logger.error(f"{e} - FindALL")
        return False, f"{e}"

def find_by_id(id):
    try:
        car_da = DataAccess(Car)
        car = car_da.find_by_id(id)
        if car:
            Logger.info(f"Car FindById {id}")
            return True, car
        else:
            raise ValueError("No car Found")
    except Exception as e:
        Logger.error(f"{e} - FindById {id}")
        return False, f"{e}"


def find_by_brand(brand):
    try:
        car_da = DataAccess(Car)
        car = car_da.find_by(Car._brand == brand)
        if car:
            Logger.info(f"Car FindBy_brand {brand}")
            return True, car
        else:
            raise ValueError("No Car Found")
    except Exception as e:
        Logger.error(f"{e} - FindBy_brand {brand}")
        return False, f"{e}"

def find_by_model(model):
    try:
        car_da = DataAccess(Car)
        car = car_da.find_by(Car._model == model)
        if car:
            Logger.info(f"Car FindBy_model {model}")
            return True, car
        else:
            raise ValueError("No Car Found")
    except Exception as e:
        Logger.error(f"{e} - FindBy_model {model}")
        return False, f"{e}"


def find_by_license_plate(license_plate):
    try:
        car_da = DataAccess(Car)
        car = car_da.find_by(Car._license_plate == license_plate)
        if car:
            Logger.info(f"Car FindBy_license_plate {license_plate}")
            return True, car
        else:
            raise ValueError("No Car Found")
    except Exception as e:
        Logger.error(f"{e} - FindBy_license_plate {license_plate}")
        return False, f"{e}"

def find_by_color(color):
    try:
        car_da = DataAccess(Car)
        car = car_da.find_by(Car._color == color)
        if car:
            Logger.info(f"Car FindBy_color {color}")
            return True, car
        else:
            raise ValueError("No Car Found")
    except Exception as e:
        Logger.error(f"{e} - FindBy_color {color}")
        return False, f"{e}"
