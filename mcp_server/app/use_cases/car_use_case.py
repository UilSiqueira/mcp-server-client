from app.models.car_models import Car
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.entities.car_schema import CarCreate

async def create_car_use_case(db: AsyncSession, car: CarCreate):
    db_car = Car(
        brand=car.brand,
        model=car.model,
        year=car.year,
        engine=car.engine,
        fuel_type=car.fuel_type,
        color=car.color,
        kilometers=car.kilometers,
        number_of_doors=car.number_of_doors,
        transmission=car.transmission,
        wheel_size=car.wheel_size,
        category=car.category,
        steering=car.steering,
        price=car.price,
    )
    db.add(db_car)
    await db.commit()
    await db.refresh(db_car)
    return db_car

async def list_cars_use_case(db: AsyncSession):
    """
    Retrieve all cars from the database.
    """
    result = await db.execute(select(Car))
    return result.scalars().all()
