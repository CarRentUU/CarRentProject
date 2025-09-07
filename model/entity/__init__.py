from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_utils import create_database, database_exists

from model.entity.base import Base
from model.tools.validation import *
from model.tools.logging import *

from model.entity.person import Person
from model.entity.car import Car
from model.entity.rental import Rental



Base = declarative_base()
