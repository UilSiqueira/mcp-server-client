from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.use_cases.car_use_case import create_car_use_case, list_cars_use_case
from app.entities.car_schema import CarCreate, CarResponse
from app.config.db_config import get_db

router = APIRouter()


@router.post("/cars/", response_model=CarResponse, status_code=201)
async def register_car(
    car: CarCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Register a new car in the database.
    """
    return await create_car_use_case(db, car)

@router.get("/cars/", response_model=List[CarResponse], operation_id="cars")
async def list_cars(db: AsyncSession = Depends(get_db)):
    """
    Retrieve all cars from the database.
    """
    return await list_cars_use_case(db)
