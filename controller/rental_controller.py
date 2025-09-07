from model.da.da import DataAccess
from model.entity import Person, Car, Logger, Rental
from model.da.da import session

def save(person_id, car_id,rental_date,return_date):
    try:

        rental_da = DataAccess(Rental)
        person_da = DataAccess(Person)
        car_da = DataAccess(Car)


        existing_person = person_da.find_by_id(person_id)
        if not existing_person:
            return False, f"Person ID {person_id} does not exist."

        existing_car = car_da.find_by_id(car_id)
        if not existing_car:
            return False, f"Car ID {car_id} does not exist."


        existing_rentals = rental_da.find_by((Rental.car_id == car_id) & (Rental.return_date == None))
        if existing_rentals:
            return False, f"Car ID {car_id} is already rented and not yet returned."




        rental = Rental(person_id, car_id, rental_date,return_date)

        rental_da.save(rental)
        Logger.info(f"Rental Info {rental} Saved")
        return True, rental
    except Exception as e:
        Logger.error(f"{e} - Not Saved")
        return False, f"{e}"



def return_click( car_id, return_date):
    try:
        rental_da = DataAccess(Rental)

        existing_rental = session.query(Rental) \
            .filter(Rental.car_id == car_id, Rental.return_date == None) \
            .first()

        if existing_rental:
            existing_rental.return_date = return_date
            session.commit()
            Logger.info(f"Rental return updated: {existing_rental}")
            return True, existing_rental


        else:
            Logger.warning("No active rental found to return.")
            return False, "No active rental found for this car."

    except Exception as e:
        Logger.error(f"{e} - Return failed")
        return False, f"{e}"



def edit(id, person_id, car_id, rental_date,return_date):
    try:
        rental = Rental(person_id, car_id, rental_date,return_date)
        rental.id = id

        rental_da = DataAccess(Rental)
        rental_da.edit(rental)
        Logger.info(f"Rental Info {rental} Edited")
        return True, rental
    except Exception as e:
        Logger.error(f"{e} - Not Edited")
        return False, f"{e}"


def remove_by_id(id):
    try:
        rental_da = DataAccess(Rental)

        rental = session.query(Rental).get(id)

        if rental is None:
            return False, "Rental not found"


        rental_str = str(rental)

        session.delete(rental)
        session.commit()

        Logger.info(f"Rental Info {rental_str} Removed")
        return True, rental
    except Exception as e:
        Logger.error(f"{e} - Not Removed")
        return False, f"{e}"

def find_all():
    try:
        rental_da = DataAccess(Rental)
        rental_list = rental_da.find_all()
        Logger.info(f"Rental Info FindALL")
        return True, rental_list
    except Exception as e:
        Logger.error(f"{e} - FindALL")
        return False, f"{e}"


def find_by_id(id):
    try:
        rental_da = DataAccess(Rental)
        rental = rental_da.find_by_id(id)
        if rental:
            Logger.info(f"Rental Info FindById {id}")
            return True, rental
        else:
            raise ValueError("No Rental Info Found")
    except Exception as e:
        Logger.error(f"{e} - FindById {id}")
        return False, f"{e}"


def find_by_person_id(person_id):
    try:
        person_da = DataAccess(Person)
        person = person_da.find_by(Person._person_id == person_id)
        if person:
            Logger.info(f"Person FindBy_person_id {person_id}")
            return True, person
        else:
            raise ValueError("No Person Found")
    except Exception as e:
        Logger.error(f"{e} - FindBy_person_id {person_id}")
        return False, f"{e}"

def find_by_car_id(car_id):
    try:
        car_da = DataAccess(Car)
        car = car_da.find_by(Car._car_id == car_id)
        if car:
            Logger.info(f"Car FindBy_car_id {car_id}")
            return True, car
        else:
            raise ValueError("No Car Found")
    except Exception as e:
        Logger.error(f"{e} - FindBy_car_id {car_id}")
        return False, f"{e}"


def find_by_rental_date(rental_date):
    try:
        rental_da = DataAccess(Rental)
        rental = rental_da.find_by(Rental._rental_date == rental_date)
        if rental:
            Logger.info(f"Car FindBy_rental_date {rental_date}")
            return True, rental
        else:
            raise ValueError("No Rent Found")
    except Exception as e:
        Logger.error(f"{e} - FindBy_rental_date {rental_date}")
        return False, f"{e}"

def find_by_return_date(return_date):
    try:
        rental_da = DataAccess(Rental)
        rental = rental_da.find_by(Rental._return_date == return_date)
        if rental:
            Logger.info(f"Car FindBy_return_date {return_date}")
            return True, rental
        else:
            raise ValueError("No Rent Found")
    except Exception as e:
        Logger.error(f"{e} - FindBy_return_date{return_date}")
        return False, f"{e}"

