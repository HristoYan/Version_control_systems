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

    def prepare_pasta(self):
        return (f"Pasta Type: {self.type_of_pasta()}\n"
                f"Sauce: {self.sauce()}\n"
                f"Topping: {self.topping()}\n"
                f"Dressing: {self.dressing()}\n")


class Spaghetti(Pasta):
    def type_of_pasta(self):
        return "Spaghetti"

    def sauce(self):
        return "Tomato Basil Sauce"

    def topping(self):
        return "Grated Parmesan Cheese"

    def dressing(self):
        return "Fresh Basil"


class Fettuccine(Pasta):
    def type_of_pasta(self):
        return "Fettuccine"

    def sauce(self):
        return "Alfredo Sauce"

    def topping(self):
        return "Grilled Chicken"

    def dressing(self):
        return "Chopped Parsley"


class Penne(Pasta):
    def type_of_pasta(self):
        return "Penne"

    def sauce(self):
        return "Arrabbiata Sauce"

    def topping(self):
        return "Shredded Mozzarella"

    def dressing(self):
        return "Red Chili Flakes"


class PastaFactory:
    @staticmethod
    def create_pasta(self, pasta_type):
        if pasta_type == "Spaghetti":
            return Spaghetti()
        elif pasta_type == "Fettuccine":
            return Fettuccine()
        elif pasta_type == "Penne":
            return Penne()
        else:
            raise ValueError(f"Unknown pasta type: {pasta_type}")


factory = PastaFactory()

pasta = factory.create_pasta("Spaghetti")
print(pasta.prepare_pasta())

print("-" * 30)

pasta = factory.create_pasta("Fettuccine")
print(pasta.prepare_pasta())

print("-" * 30)

pasta = factory.create_pasta("Penne")
print(pasta.prepare_pasta())
