class Vehicle:
    __COLOR_VARIANTS = ['BLUE', 'RED', 'GREEN', 'BLACK', 'WHITE']
    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str):
        self.owner = owner
        self.model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f"Модель: {self.model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(f"{self.get_model()},\n"
              f"{self.get_horsepower()},\n"
              f"{self.get_color()},\n"
              f"Владелец: {self.owner}")

    def set_color(self, new_color: str):
        self.new_color = new_color
        if [i for i in self.__COLOR_VARIANTS if self.new_color == i.upper()]:
            self.__color = self.new_color
        else:
            print(f"Нельзя сменить цвет на {self.new_color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()