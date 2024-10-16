class Weight:
    def __init__(self, value, from_unit, to_unit):
        self.__value = value
        self.__from_unit = from_unit.lower()
        self.__to_unit = to_unit.lower()

    measure_units = {
        "Gram": "g",
        "Milligram": "mg",
        "Kilogram": "kg",
        "Ton": "t",
        "Pound": "lb",
    }

    # Conversion factors from base unit (gram)
    # All units are converted to grams
    conversion_factors = {
        "gram": 1,
        "milligram": 1000,
        "kilogram": 1e-3,
        "ton": 1e-6,
        "pound": 0.00220462,
    }

    def convert_weight(self):
        if (self.__from_unit in self.conversion_factors) and (self.__to_unit in self.conversion_factors):
            # First, convert value in grams
            value_in_grams = int(self.__value) / self.conversion_factors[self.__from_unit]
            # Then, convert grams to target unit
            return value_in_grams * self.conversion_factors[self.__to_unit]