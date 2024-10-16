class Length:
    def __init__(self, value, from_unit, to_unit):
        self.__value = value
        self.__from_unit = from_unit.lower()
        self.__to_unit = to_unit.lower()

    measure_units = {
        "Centimeter": "cm",
        "Meter": "m",
        "Kilometer": "km",
        "Foot": "ft",
        "Inch": "in",
        "Yard": "yd",
        "Mile": "mile",
    }

    conversion_factors = {
        "centimeter": 0.01,
        "meter": 1,
        "kilometer": 1000,
        "foot": 0.3048,
        "inch": 0.0254,
        "yard": 0.9144,
        "mile": 1609.34,
    }

    def convert_length(self):
        value_in_meter = float(self.__value) * self.conversion_factors[self.__from_unit]
        return value_in_meter / self.conversion_factors[self.__to_unit]