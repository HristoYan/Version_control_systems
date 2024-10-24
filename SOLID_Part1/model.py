from abc import ABC, abstractmethod


class HotDog(ABC):
    def __init__(self, hot_dog_type):
        self.hot_dog_type = hot_dog_type

    @abstractmethod
    def ingredients(self):
        pass


class HotDogOne(HotDog):
    counter = 0

    def __init__(self, sauce, topping, hot_dog_type='One'):
        super().__init__(hot_dog_type)
        self.sauce: str = sauce
        self.topping: str = topping
        self.price: float = 2.99

    def ingredients(self):
        HotDogOne.counter += 1
        return f'Recipe One: Bread one, sausage one, {self.sauce}, {self.topping}'

    def get_counter(self):
        return f'Hod Dog One sold {self.counter} times.'


class HotDogTwo(HotDog):
    counter = 0

    def __init__(self, sauce, topping, hot_dog_type='Two'):
        super().__init__(hot_dog_type)
        self.sauce: str = sauce
        self.topping: str = topping
        self.price: float = 3.49

    def ingredients(self):
        HotDogTwo.counter += 1
        return f'Recipe Two: Bread two, sausage two, {self.sauce}, {self.topping}'

    def get_counter(self):
        return f'Hod Dog Two sold {self.counter} times.'


class HotDogThree(HotDog):
    counter = 0

    def __init__(self, sauce, topping, hot_dog_type='Three'):
        super().__init__(hot_dog_type)
        self.sauce: str = sauce
        self.topping: str = topping
        self.price: float = 3.99

    def ingredients(self):
        HotDogThree.counter += 1
        return f'Recipe Three: Bread three, sausage three, {self.sauce}, {self.topping}'

    def get_counter(self):
        return f'Hod Dog Three sold {self.counter} times.'


class CustomHodDog(HotDog):
    counter = 0

    def __init__(self, bread, sausage, sauce, topping, hot_dog_type='Custom'):
        super().__init__(hot_dog_type)
        self.topping: str = topping
        self.sauce: str = sauce
        self.sausage: str = sausage
        self.bread: str = bread
        self.price: float = 4.99

    def ingredients(self):
        CustomHodDog.counter += 1
        return f'Your Custom Recipe: {self.bread} Bread, Sausage {self.sausage}, {self.sauce}, {self.topping}'

    def get_counter(self):
        return f'Custom Hod Dog sold {self.counter} times.'

