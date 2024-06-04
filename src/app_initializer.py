from .controller.electricity_reading_controller import service as electricity_reading_service
from .domain.price_plan import PricePlan
from .generator.electricity_reading_generator import generate_electricity_readings
from .repository.price_plan_repository import price_plan_repository

ENERGY_SUPPLIER_I = "Energy Supplier I"
ENERGY_SUPPLIER_II = "Energy Supplier II"
ENERGY_SUPPLIER_III = "Energy Supplier III"

EXPENSIVE_PRICE_PLAN_ID = "price-plan-0"
MEDIUM_PRICE_PLAN_ID = "price-plan-1"
STANDARD_PRICE_PLAN_ID = "price-plan-2"

NUM_METERS = 10
NUM_READINGS_AGAINST_METER = 5


def populate_random_electricity_readings():
    for index in range(NUM_METERS):
        smartMeterId = f"smart-meter-{index}"
        electricity_reading_service.store_reading(
            {
                "smartMeterId": smartMeterId,
                "electricityReadings": generate_electricity_readings(NUM_READINGS_AGAINST_METER),
            }
        )


def populate_price_plans():
    price_plans = [
        PricePlan(EXPENSIVE_PRICE_PLAN_ID, ENERGY_SUPPLIER_I, 10),
        PricePlan(MEDIUM_PRICE_PLAN_ID, ENERGY_SUPPLIER_II, 5),
        PricePlan(STANDARD_PRICE_PLAN_ID, ENERGY_SUPPLIER_III, 1),
    ]
    price_plan_repository.store(price_plans)


def initialize_data():
    populate_random_electricity_readings()
    populate_price_plans()
