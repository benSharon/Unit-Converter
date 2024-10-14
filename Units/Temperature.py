class Temperature:
    def __init__(self, value, from_unit, to_unit):
        self.__value = value
        self.__from_unit = from_unit.lower()
        self.__to_unit = to_unit.lower()

    measure_units = {"Celsius": "°C", "Kelvin": "°K", "Fahrenheit": "°F"}

    def convert_temperature(self):
        match self.__from_unit.lower():
            case "celsius":
                return self.__from_celsius()
            case "kelvin":
                return self.__from_kelvin()
            case "fahrenheit":
                return self.__from_fahrenheit()

    def __from_celsius(self):
        match self.__to_unit.lower():
            case "celsius":
                return self.__value
            case "kelvin":
                return float(self.__value) + 273.15
            case "fahrenheit":
                return float(self.__value) * (9 / 5) + 32

    def __from_kelvin(self):
        match self.__to_unit.lower():
            case "celsius":
                return float(self.__value) - 273.15
            case "kelvin":
                return self.__value
            case "fahrenheit":
                return (float(self.__value) - 273.15) * 5 / 9 + 32

    def __from_fahrenheit(self):
        match self.__to_unit.lower():
            case "celsius":
                return (float(self.__value) - 32) * 5 / 9
            case "kelvin":
                return (float(self.__value) - 32) * 5 / 9 + 273.15
            case "fahrenheit":
                return self.__value
