from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional


class FuelType(str, Enum):
    GASOLINE = "Gasoline"
    ETHANOL = "Ethanol"
    DIESEL = "Diesel"
    ELECTRIC = "Electric"
    HYBRID = "Hybrid"


class Category(str, Enum):
    SEDAN = "Sedan"
    HATCHBACK = "Hatchback"
    SUV = "SUV"
    WAGON = "Wagon"
    PICKUP = "Pickup"
    CONVERTIBLE = "Convertible"
    COUPE = "Coupe"


class Transmission(str, Enum):
    MANUAL = "Manual"
    AUTOMATIC = "Automatic"
    CVT = "CVT"
    SEQUENTIAL = "Sequential"


class Steering(str, Enum):
    MANUAL = "Manual"
    HYDRAULIC = "Hydraulic"
    ELECTRIC = "Electric"


class CarBase(BaseModel):
    brand: str = Field(..., example="Toyota")
    model: str = Field(..., example="Corolla")
    year: int = Field(..., example=2020)
    engine: str = Field(..., example="2.0 Flex")
    fuel_type: FuelType
    color: str = Field(..., example="Silver")
    kilometers: float = Field(..., example=35000.5)
    number_of_doors: int = Field(..., example=4)
    transmission: Transmission
    wheel_size: int = Field(..., example=16)
    category: Category
    steering: Steering
    price: Optional[float] = Field(None, example=85000.00)

    class Config:
        use_enum_values = True
        from_attributes = True


class CarCreate(CarBase):
    pass


class CarResponse(CarBase):
    id: int

    class Config:
        from_attributes = True
