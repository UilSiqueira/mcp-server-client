import asyncio
import random
from faker import Faker
from app.config.db_config import AsyncSessionLocal
from app.models.car_models import Car, FuelType, Category, Transmission, Steering

fake = Faker()

car_catalog = {
    "Toyota": [
        {"model": "Corolla", "category": Category.SEDAN},
        {"model": "Yaris", "category": Category.HATCHBACK},
        {"model": "Hilux", "category": Category.PICKUP},
    ],
    "Chevrolet": [
        {"model": "Onix", "category": Category.HATCHBACK},
        {"model": "S10", "category": Category.PICKUP},
        {"model": "Cruze", "category": Category.SEDAN},
    ],
    "Honda": [
        {"model": "Civic", "category": Category.SEDAN},
        {"model": "Fit", "category": Category.HATCHBACK},
        {"model": "HR-V", "category": Category.SUV},
    ],
    "Volkswagen": [
        {"model": "Golf", "category": Category.HATCHBACK},
        {"model": "Virtus", "category": Category.SEDAN},
        {"model": "T-Cross", "category": Category.SUV},
    ],
    "Ford": [
        {"model": "Ranger", "category": Category.PICKUP},
        {"model": "Ka", "category": Category.HATCHBACK},
        {"model": "Fusion", "category": Category.SEDAN},
    ],
    "Fiat": [
        {"model": "Argo", "category": Category.HATCHBACK},
        {"model": "Cronos", "category": Category.SEDAN},
        {"model": "Toro", "category": Category.PICKUP},
    ],
    "Mercedes-Benz": [
        {"model": "C 180", "category": Category.SEDAN},
        {"model": "GLA 200", "category": Category.SUV},
        {"model": "AMG GT", "category": Category.COUPE},
    ],
}


def get_random_car_info():
    brand = random.choice(list(car_catalog.keys()))
    car = random.choice(car_catalog[brand])
    return brand, car["model"], car["category"]

async def create_fake_cars(n: int = 100):
    async with AsyncSessionLocal() as session:
        for _ in range(n):
            brand, model, category = get_random_car_info()

            car = Car(
                brand=brand,
                model=model,
                year=random.randint(2000, 2024),
                engine=f"{random.choice(['1.0', '1.3', '1.6', '2.0', '2.2'])} {random.choice(['', 'Flex', 'Turbo'])}".strip(),
                fuel_type=random.choice(list(FuelType)),
                color=fake.safe_color_name().capitalize(),
                kilometers=round(random.uniform(0, 250_000), 1),
                number_of_doors=random.choice([2, 4]),
                transmission=random.choice(list(Transmission)),
                wheel_size=random.choice([14, 15, 16, 17, 18, 19]),
                category=category,
                steering=random.choice(list(Steering)),
                price=round(random.uniform(30000, 250000), 2)
            )

            session.add(car)

        await session.commit()
        print(f"{n} fake cars created successfully.")

if __name__ == "__main__":
    asyncio.run(create_fake_cars(100))

