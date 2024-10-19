class Vehicle:
    __COLOR_VARIANTS = ["Красный", "Оранжевый", "Жёлтый", "Зелёный", "Синий", "Индиго", "Фиолетовый", "Белый", "Чёрный"]
    def __init__(self, owner, __model,  __engine_power,  __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощьность дигателя: {self.__engine_power}"

    def set_color(self, new_color):
        for i in Vehicle.__COLOR_VARIANTS:
            if i == new_color:
                self._Vehicle__color = new_color
                return 
        if new_color == self._Vehicle__color:
            return
        else:
            print("Нельзя сменить цвет на ", new_color)
    def get_color(self):
        return f"Цвет {self.__color}"


    def print_info(self):
        print(self.get_model(),"\n",self.get_horsepower(),"\n",self.get_color(),"\n", "владелец: ",self.owner)

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Чёрный')
vehicle1.set_color('BLACKпукпу')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()