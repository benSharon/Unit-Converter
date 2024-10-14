from math import pow


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
        "Pound": "lb"
    }

    def convert_weight(self):
        match self.__from_unit.lower():
            case "gram":
                return self.__from_gram()
            case "milligram":
                return self.__from_milligram()
            case "kilogram":
                return self.__from_kilogram()
            case "ton":
                return self.__from_ton()
            case "pound":
                return self.__from_pound()

    def __from_gram(self):
        match self.__to_unit.lower():
            case "gram":
                return self.__value
            case "milligram":
                return self.__value * 1000
            case "kilogram":
                return self.__value * pow(10, -3)
            case "ton":
                return self.__value * pow(10, -6)
            case "pound":
                return self.__value * 0.00220462

    def __from_milligram(self):
        match self.__to_unit.lower():
            case "gram":
                return float(self.__value) * pow(10, -3)
            case "milligram":
                return float(self.__value)
            case "kilogram":
                return float(self.__value) * pow(10, -6)
            case "ton":
                return float(self.__value) * pow(10, -9)
            case "pound":
                return float(self.__value) * 2.20462 * pow(10, -6)

    def __from_kilogram(self):
        match self.__to_unit.lower():
            case "gram":
                return float(self.__value) * pow(10, 3)
            case "milligram":
                return float(self.__value) * pow(10, 6)
            case "kilogram":
                return float(self.__value)
            case "ton":
                return float(self.__value) * pow(10, -3)
            case "pound":
                return float(self.__value) * 2.20462

    def __from_ton(self):
        match self.__to_unit.lower():
            case "gram":
                return float(self.__value) * pow(10, 6)
            case "milligram":
                return float(self.__value) * pow(10, 9)
            case "kilogram":
                return float(self.__value) * pow(10, 3)
            case "ton":
                return float(self.__value)
            case "pound":
                return float(self.__value) * 2204.62

    def __from_pound(self):
        match self.__to_unit.lower():
            case "gram":
                return float(self.__value) * 453.592
            case "milligram":
                return float(self.__value) * 453592
            case "kilogram":
                return float(self.__value) * 0.453592
            case "ton":
                return float(self.__value) * 0.000453592
            case "pound":
                return float(self.__value)
