from model.da.da import DataAccess
from model.entity import Person, Logger


def save(first_name, last_name,national_id):
    try:
        person = Person(first_name, last_name,national_id)

        person_da = DataAccess(Person)
        person_da.save(person)
        Logger.info(f"Person {person} Saved")
        return True, person
    except Exception as e:
        Logger.error(f"{e} - Not Saved")
        return False, f"{e}"


def edit(id, first_name, last_name,national_id):
    try:
        person = Person(first_name, last_name,national_id)
        person.id = id

        person_da = DataAccess(Person)
        person_da.edit(person)
        Logger.info(f"Person {person} Edited")
        return True, person
    except Exception as e:
        Logger.error(f"{e} - Not Edited")
        return False, f"{e}"


def remove_by_id(id):
    try:
        person_da = DataAccess(Person)
        person = person_da.remove_by_id(id)

        Logger.info(f"person {person} Removed")
        return True, person
    except Exception as e:
        Logger.error(f"{e} - Not Removed")
        return False, f"{e}"


def find_all():
    try:
        person_da = DataAccess(Person)
        person_list = person_da.find_all()
        Logger.info(f"Person FindALL")
        return True, person_list
    except Exception as e:
        Logger.error(f"{e} - FindALL")
        return False, f"{e}"

def find_by_id(id):
    try:
        person_da = DataAccess(Person)
        person = person_da.find_by_id(id)
        if person:
            Logger.info(f"Person FindById {id}")
            return True, person
        else:
            raise ValueError("No person Found")
    except Exception as e:
        Logger.error(f"{e} - FindById {id}")
        return False, f"{e}"
def find_by_first_name(first_name):
    try:
        person_da = DataAccess(Person)
        person = person_da.find_by(Person._first_name == first_name)
        if person:
            Logger.info(f"Person FindBy_first_name {first_name}")
            return True, person
        else:
            raise ValueError("No Person Found")
    except Exception as e:
        Logger.error(f"{e} - FindBy_first_name {first_name}")
        return False, f"{e}"

def find_by_last_name(last_name):
    try:
        person_da = DataAccess(Person)
        person = person_da.find_by(Person._last_name == last_name)
        if person:
            Logger.info(f"Person FindBy_last_name {last_name}")
            return True, person
        else:
            raise ValueError("No Person Found")
    except Exception as e:
        Logger.error(f"{e} - FindBy_last_name {last_name}")
        return False, f"{e}"


def find_by_national_id(national_id):
    try:
        person_da = DataAccess(Person)
        person = person_da.find_by(Person._national_id == national_id)
        if person:
            Logger.info(f"Person FindBy_national_id {national_id}")
            return True, person
        else:
            raise ValueError("No Person Found")
    except Exception as e:
        Logger.error(f"{e} - FindBy_national_id {national_id}")
        return False, f"{e}"

