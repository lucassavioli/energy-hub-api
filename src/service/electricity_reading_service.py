from functools import reduce

from ..domain.electricity_reading import ElectricityReading


class ElectricityReadingService:
    def __init__(self, repository):
        self.electricity_reading_repository = repository
        return

    def store_reading(self, json):
        readings = list(map(lambda x: ElectricityReading(x), json["electricityReadings"]))
        return self.electricity_reading_repository.store(json["smartMeterId"], readings)

    def retrieve_readings_for(self, smart_meter_id):
        return self.electricity_reading_repository.find(smart_meter_id)

    def calculate_average_reading(self, readings):
        sum = reduce((lambda p, c: p + c), map(lambda r: r.reading, readings), 0)
        return sum / len(readings)
