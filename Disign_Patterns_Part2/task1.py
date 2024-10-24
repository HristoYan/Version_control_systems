from abc import ABC, abstractmethod


# Strategy for getting data (either from keyboard or file)
class InputStrategy(ABC):
    @abstractmethod
    def get_data(self):
        pass


# Strategy for displaying data (either on the screen or writing to a file)
class OutputStrategy(ABC):
    @abstractmethod
    def display_data(self, data):
        pass


# Input strategy: from keyboard
class KeyboardInputStrategy(InputStrategy):
    def get_data(self):
        data = input("Enter numbers separated by spaces: ")
        return list(map(int, data.split()))


# Input strategy: from file
class FileInputStrategy(InputStrategy):
    def __init__(self, file_name):
        self.file_name = file_name

    def get_data(self):
        with open(self.file_name, 'r') as file:
            data = file.read().strip()
        return list(map(int, data.split()))


# Output strategy: display on screen
class ScreenOutputStrategy(OutputStrategy):
    def display_data(self, data):
        print(f"Data: {data}")


# Output strategy: write to file
class FileOutputStrategy(OutputStrategy):
    def __init__(self, file_name):
        self.file_name = file_name

    def display_data(self, data):
        with open(self.file_name, 'w') as file:
            file.write(" ".join(map(str, data)))
        print(f"Data written to {self.file_name}")


# Class that uses strategy patterns for input, output and performs array operations
class ArrayOperations:
    def __init__(self, input_strategy: InputStrategy, output_strategy: OutputStrategy):
        self.input_strategy = input_strategy
        self.output_strategy = output_strategy
        self.data = []

    # Load data using the input strategy
    def load_data(self):
        self.data = self.input_strategy.get_data()

    # Display data using the output strategy
    def display_data(self):
        self.output_strategy.display_data(self.data)

    # Flip the data (reverse the array)
    def flip_data(self):
        self.data.reverse()

    # Find the maximum value in the array
    def find_max(self):
        return max(self.data)

    # Find the minimum value in the array
    def find_min(self):
        return min(self.data)


if __name__ == "__main__":
    # Example 1: Input from keyboard, output to screen
    keyboard_input = KeyboardInputStrategy()
    screen_output = ScreenOutputStrategy()
    array_ops = ArrayOperations(keyboard_input, screen_output)

    print("Test with Keyboard Input and Screen Output")
    array_ops.load_data()  # Get data from the keyboard
    array_ops.display_data()  # Display data on the screen
    print(f"Max value: {array_ops.find_max()}")
    print(f"Min value: {array_ops.find_min()}")

    array_ops.flip_data()  # Flip the data
    array_ops.display_data()  # Display flipped data
    print("-" * 40)

    # Example 2: Input from file, output to file
    file_input = FileInputStrategy('input.txt')
    file_output = FileOutputStrategy('output.txt')
    array_ops = ArrayOperations(file_input, file_output)

    print("Test with File Input and File Output")
    array_ops.load_data()  # Get data from a file
    array_ops.display_data()  # Write data to an output file
    print(f"Max value: {array_ops.find_max()}")
    print(f"Min value: {array_ops.find_min()}")

    array_ops.flip_data()  # Flip the data
    array_ops.display_data()  # Write flipped data to output file
