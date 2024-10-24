class Singleton:
    _instance = None  # Class variable to hold the single instance of the class

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            print("Creating the Singleton instance.")
        return cls._instance

    def __init__(self):
        self.data = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data


if __name__ == "__main__":
    # Create the first instance
    singleton1 = Singleton()
    singleton1.set_data("Singleton Instance Data")

    # Create a second instance
    singleton2 = Singleton()

    # Test if both instances are the same
    print(f"singleton1 data: {singleton1.get_data()}")
    print(f"singleton2 data: {singleton2.get_data()}")

    # Check if singleton1 and singleton2 refer to the same instance
    print(f"Are both instances the same? {'Yes' if singleton1 is singleton2 else 'No'}")

    # Modify data through the second instance and see if it affects the first one
    singleton2.set_data("Modified Data")

    print(f"singleton1 data after modification: {singleton1.get_data()}")
    print(f"singleton2 data after modification: {singleton2.get_data()}")
