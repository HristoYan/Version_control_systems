# Product class
class Computer:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None
        self.storage = None
        self.power_supply = None
        self.operating_system = None

    def __str__(self):
        return (f"Computer Specifications:\n"
                f"CPU: {self.cpu}\n"
                f"GPU: {self.gpu}\n"
                f"RAM: {self.ram} GB\n"
                f"Storage: {self.storage} GB\n"
                f"Power Supply: {self.power_supply} Watts\n"
                f"Operating System: {self.operating_system}\n")


# Builder class
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_power_supply(self, power_supply):
        self.computer.power_supply = power_supply
        return self

    def set_operating_system(self, operating_system):
        self.computer.operating_system = operating_system
        return self

    # Method to get the final product
    def build(self):
        return self.computer


# Test the Builder Pattern
if __name__ == "__main__":
    # Build a gaming computer
    gaming_computer = (ComputerBuilder()
                       .set_cpu("Intel i9")
                       .set_gpu("NVIDIA RTX 4090")
                       .set_ram(32)
                       .set_storage(2000)
                       .set_power_supply(850)
                       .set_operating_system("Windows 11")
                       .build())

    print("Gaming Computer:")
    print(gaming_computer)

    # Build an office computer
    office_computer = (ComputerBuilder()
                       .set_cpu("Intel i5")
                       .set_gpu("Integrated Intel Graphics")
                       .set_ram(8)
                       .set_storage(500)
                       .set_power_supply(450)
                       .set_operating_system("Windows 10")
                       .build())

    print("\nOffice Computer:")
    print(office_computer)

    # Build a budget computer
    budget_computer = (ComputerBuilder()
                       .set_cpu("AMD Ryzen 3")
                       .set_ram(4)
                       .set_storage(256)
                       .set_power_supply(300)
                       .set_operating_system("Linux")
                       .build())

    print("\nBudget Computer:")
    print(budget_computer)
