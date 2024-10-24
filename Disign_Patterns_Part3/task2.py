from abc import ABC, abstractmethod


class Pasta(ABC):
    @abstractmethod
    def type_of_pasta(self):
        pass

    @abstractmethod
    def sauce(self):
        pass

    @abstractmethod
    def topping(self):
        pass

    @abstractmethod
    def dressing(self):
        pass

    def __str__(self):
        return (f"Type of Pasta: {self.type_of_pasta()}\n"
                f"Sauce: {self.sauce()}\n"
                f"Topping: {self.topping()}\n"
                f"Dressing: {self.dressing()}")


class Spaghetti(Pasta):
    def type_of_pasta(self):
        return "Spaghetti"

    def sauce(self):
        return "Spaghetti Sauce"

    def topping(self):
        return "Cheese"

    def dressing(self):
        return "Parmesan"


class Penne(Pasta):
    def type_of_pasta(self):
        return "Penne"

    def sauce(self):
        return "Penne Sauce"

    def topping(self):
        return "Garlic"

    def dressing(self):
        return "Olive oil"


class Fettuccine(Pasta):
    def type_of_pasta(self):
        return "Fettuccine"

    def sauce(self):
        return "Fettuccine Sauce"

    def topping(self):
        return "Vegetables"

    def dressing(self):
        return "Pesto"


class PastaFactory:
    @staticmethod
    def create_pasta(pasta_type):
        if pasta_type == "Spaghetti":
            return Spaghetti()
        elif pasta_type == "Penne":
            return Penne()
        elif pasta_type == "Fettuccine":
            return Fettuccine()
        else:
            raise ValueError(f"Unknown pasta type: {pasta_type}")


if __name__ == "__main__":
    pasta_types = ["Spaghetti", "Penne", "Fettuccine"]

    for pasta_type in pasta_types:
        pasta = PastaFactory.create_pasta(pasta_type)
        print(f"\nPreparing {pasta_type}:")
        print(pasta)
