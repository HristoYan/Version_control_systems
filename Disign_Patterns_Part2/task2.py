# Old printer class (Adaptee)
class OldPrinter:
    def print_text(self, text):
        print(f"Old Printer: {text}")


# Modern printer interface (Target)
class ModernPrinter:
    def print_document(self, document):
        pass


# Adapter class
class PrinterAdapter(ModernPrinter):
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def print_document(self, document):
        # Convert the request for the new method to the old method
        self.old_printer.print_text(document)


if __name__ == "__main__":
    # Create an instance of the old printer
    old_printer = OldPrinter()

    # Use the adapter to adapt the old printer to the modern printer interface
    printer_adapter = PrinterAdapter(old_printer)

    # Test the adapter with the modern interface method
    print("Using the Adapter to print with the ModernPrinter interface:")
    printer_adapter.print_document("This is a test document.")
