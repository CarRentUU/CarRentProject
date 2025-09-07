from model.entity import *

class Car(Base):
    __tablename__ = 'cars'

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _brand = Column("brand", String(30))
    _model = Column("model", String(30))
    _license_plate = Column("license_plate", String(10))
    _color = Column("color", String(20))

    def __init__(self, brand, model, license_plate, color):
        self.id = None
        self.brand = brand
        self.model = model
        self.license_plate = license_plate
        self.color = color

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def license_plate(self):
        return self._license_plate

    @license_plate.setter
    def license_plate(self, value):
        self._license_plate = value

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = brand_validator(value, "Invalid Brand")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = brand_validator(value, "Invalid Model")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = name_validator(value, "Invalid Color")
