from ..repository.price_plan_repository import price_plan_repository
from .electricity_reading_service import ElectricityReadingService
from .time_conversion_service import calculate_time_elapsed


class PricePlanService:
    def __init__(self, reading_repository):
        self.electricity_reading_service = ElectricityReadingService(reading_repository)

    def get_spend_per_price_plan(self, smart_meter_id, limit=None):
        readings = self.electricity_reading_service.retrieve_readings_for(smart_meter_id)
        if not readings:
            return []

        consumed_energy = self.calculate_consumed_energy(readings)
        price_plans = price_plan_repository.get()
        spend_per_plan = self.calculate_spend_against_each_price_plan(consumed_energy, price_plans)

        return spend_per_plan[:limit]

    def calculate_consumed_energy(self, readings):
        average = self.electricity_reading_service.calculate_average_reading(readings)
        time_elapsed = calculate_time_elapsed(readings)
        return average / time_elapsed

    def calculate_spend_against_each_price_plan(self, consumed_energy, price_plans):
        spend_per_plan = [
            {plan.name: consumed_energy * plan.unit_rate} for plan in self.cheapest_plans_first(price_plans)
        ]
        return spend_per_plan

    def cheapest_plans_first(self, price_plans):
        return list(sorted(price_plans, key=lambda plan: plan.unit_rate))
