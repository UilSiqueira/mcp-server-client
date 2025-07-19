from sqlalchemy import (
    Column, Integer, String, Float, Enum
)
from app.config.db_config import Base
import enum


class FuelType(enum.Enum):
    GASOLINE = "Gasoline"
    ETHANOL = "Ethanol"
    DIESEL = "Diesel"
    ELECTRIC = "Electric"
    HYBRID = "Hybrid"

class Category(enum.Enum):
    SEDAN = "Sedan"
    HATCHBACK = "Hatchback"
    SUV = "SUV"
    WAGON = "Wagon"
    PICKUP = "Pickup"
    CONVERTIBLE = "Convertible"
    COUPE = "Coupe"

class Transmission(enum.Enum):
    MANUAL = "Manual"
    AUTOMATIC = "Automatic"
    CVT = "CVT"
    SEQUENTIAL = "Sequential"

class Steering(enum.Enum):
    MANUAL = "Manual"
    HYDRAULIC = "Hydraulic"
    ELECTRIC = "Electric"

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    engine = Column(String(30), nullable=False)  # e.g., "1.6", "2.0 Turbo"
    fuel_type = Column(Enum(FuelType), nullable=False)
    color = Column(String(30), nullable=False)
    kilometers = Column(Float, nullable=False)  # in kilometers
    number_of_doors = Column(Integer, nullable=False)
    transmission = Column(Enum(Transmission), nullable=False)
    wheel_size = Column(Integer, nullable=False)  # rim size in inches
    category = Column(Enum(Category), nullable=False)
    steering = Column(Enum(Steering), nullable=False)
    price = Column(Float, nullable=True)  # in local currency

    def __repr__(self):
        return (
            f"<Car({self.brand} {self.model} {self.year}, "
            f"{self.engine}, {self.fuel_type.value}, "
            f"Color: {self.color}, {self.mileage} km, "
            f"{self.number_of_doors} doors, {self.transmission.value}, "
            f"Rim {self.wheel_size}, {self.category.value}, "
            f"Steering: {self.steering.value})>"
        )