import logging


class Logger:
    def __init__(self, log_destination='screen'):
        self.log_destination = log_destination
        self.logger = logging.getLogger("NumberProcessorLogger")
        self.logger.setLevel(logging.INFO)

        # Set up logging to either file or console
        if log_destination == 'file':
            handler = logging.FileHandler('operations.log')
        else:  # Default to screen
            handler = logging.StreamHandler()

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log(self, message):
        self.logger.info(message)


class NumberProcessor:
    def __init__(self, logger):
        self.numbers = []
        self.logger = logger

    def input_numbers(self):
        # Input numbers from the user
        input_data = input("Enter numbers separated by spaces: ")
        self.numbers = list(map(float, input_data.split()))
        self.logger.log(f"Input numbers: {self.numbers}")

    def save_numbers_to_file(self, file_path):
        # Save numbers and their max/min to the specified file
        max_num = max(self.numbers) if self.numbers else None
        min_num = min(self.numbers) if self.numbers else None

        with open(file_path, 'w') as file:
            file.write("Numbers:\n")
            file.write(" ".join(map(str, self.numbers)) + "\n")
            file.write(f"Maximum: {max_num}\n")
            file.write(f"Minimum: {min_num}\n")

        self.logger.log(f"Numbers saved to {file_path}. Max: {max_num}, Min: {min_num}")

    def display_numbers(self):
        print("Numbers:", self.numbers)
        self.logger.log(f"Displayed numbers: {self.numbers}")

    def display_max_min(self):
        max_num = max(self.numbers) if self.numbers else None
        min_num = min(self.numbers) if self.numbers else None
        print(f"Maximum: {max_num}, Minimum: {min_num}")
        self.logger.log(f"Displayed max: {max_num}, min: {min_num}")


def main():
    # Create a logger instance
    log_destination = input("Where do you want to log? (screen/file): ").strip().lower()
    logger = Logger(log_destination)

    # Create a NumberProcessor instance
    processor = NumberProcessor(logger)

    # Input numbers
    processor.input_numbers()

    # Get file path to save the numbers
    file_path = input("Enter the file path to save the numbers: ")

    # Save numbers and log the operation
    processor.save_numbers_to_file(file_path)

    # Display numbers and their max/min
    processor.display_numbers()
    processor.display_max_min()


if __name__ == "__main__":
    main()
