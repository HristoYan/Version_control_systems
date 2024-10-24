class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None

    def __str__(self):
        return (f"Computer Specifications:\n"
                f"CPU: {self.cpu}\n"
                f"RAM: {self.ram}\n"
                f"Storage: {self.storage}\n"
                f"GPU: {self.gpu}")


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def build(self):
        return self.computer


if __name__ == "__main__":
    gaming_computer = (ComputerBuilder()
                       .set_cpu("Intel i9")
                       .set_ram("32GB")
                       .set_storage("1TB SSD")
                       .set_gpu("NVIDIA RTX 3080")
                       .build())

    print(gaming_computer)

    office_computer = (ComputerBuilder()
                       .set_cpu("Intel i5")
                       .set_ram("8GB")
                       .set_storage("512GB SSD")
                       .build())

    print(office_computer)
