from model.entity import *

class Person(Base):
    __tablename__ = 'persons'

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _first_name = Column("first_name", String(30))
    _last_name = Column("last_name", String(30))
    _national_id = Column("national_id", String(10))

    def __init__(self, first_name, last_name, national_id):
        self.id = None
        self.first_name = first_name
        self.last_name = last_name
        self.national_id = national_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = name_validator(value, "Invalid First Name")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = name_validator(value, "Invalid Last Name")

    @property
    def national_id(self):
        return self._national_id

    @national_id.setter
    def national_id(self, value):
            self._national_id = national_id_validator(value,"Invalid National ID")


