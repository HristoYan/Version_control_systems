import copy


class Meal:
    def __init__(self, main_course, side_dish, drink):
        self.main_course = main_course
        self.side_dish = side_dish
        self.drink = drink

    def clone(self):
        # Return a shallow copy of the object
        return copy.copy(self)

    def deep_clone(self):
        # Return a deep copy of the object
        return copy.deepcopy(self)

    def __str__(self):
        return f"Main Course: {self.main_course}, Side Dish: {self.side_dish}, Drink: {self.drink}"


class SideDish:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return f"{self.name} ({', '.join(self.ingredients)})"


burger_meal = Meal(main_course="Burger", side_dish=SideDish("Fries", ["Potatoes", "Salt"]), drink="Coke")
pizza_meal = Meal(main_course="Pizza", side_dish=SideDish("Garlic Bread", ["Garlic", "Butter"]), drink="Sprite")
salad_meal = Meal(main_course="Caesar Salad", side_dish=SideDish("Breadsticks", ["Flour", "Salt"]), drink="Water")


new_burger_meal = burger_meal.clone()
new_burger_meal.drink = "Pepsi"  # Change the drink
print("Original Burger Meal:")
print(burger_meal)
print("Cloned and Modified Burger Meal (Shallow Copy):")
print(new_burger_meal)

print("\n" + "-" * 40 + "\n")

new_pizza_meal = pizza_meal.deep_clone()
new_pizza_meal.side_dish.ingredients.append("Cheese")  # Modify ingredients in side dish
new_pizza_meal.drink = "Fanta"

print("Original Pizza Meal:")
print(pizza_meal)
print("Cloned and Modified Pizza Meal (Deep Copy):")
print(new_pizza_meal)
