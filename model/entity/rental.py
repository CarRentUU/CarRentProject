from model.entity import *

class Rental(Base):
    __tablename__ = 'rentals'

    id = Column(Integer, primary_key=True, autoincrement=True)
    person_id = Column(Integer, ForeignKey('persons.id'))
    car_id = Column(Integer, ForeignKey('cars.id'))
    rental_date = Column(Date)
    return_date = Column(Date, nullable=True)

    person = relationship("Person")
    car = relationship("Car")

    def __init__(self, person_id, car_id, rental_date,return_date):
        self.person_id = person_id
        self.car_id = car_id
        self.rental_date = rental_date
        self.return_date = return_date

    def __repr__(self):
        return f"Person: {self.person.first_name} {self.person.last_name}\nCar: {self.car.brand} {self.car.model}\nRental Date: {self.rental_date}\nReturn Date: {self.return_date if self.return_date else 'Not Returned'}"
