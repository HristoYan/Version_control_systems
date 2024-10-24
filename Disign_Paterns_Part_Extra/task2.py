# Abstract Product: Button
class Button:
    def click(self):
        pass


# Abstract Product: Checkbox
class Checkbox:
    def select(self):
        pass


# Concrete Product: Windows Button
class WindowsButton(Button):
    def click(self):
        print("Windows Button clicked.")


# Concrete Product: MacOS Button
class MacButton(Button):
    def click(self):
        print("MacOS Button clicked.")


# Concrete Product: Windows Checkbox
class WindowsCheckbox(Checkbox):
    def select(self):
        print("Windows Checkbox selected.")


# Concrete Product: MacOS Checkbox
class MacCheckbox(Checkbox):
    def select(self):
        print("MacOS Checkbox selected.")


# Abstract Factory
class UIFactory:
    def create_button(self):
        pass

    def create_checkbox(self):
        pass


# Concrete Factory: Windows UI Factory
class WindowsFactory(UIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


# Concrete Factory: MacOS UI Factory
class MacFactory(UIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


# Client Code
class Application:
    def __init__(self, factory):
        self.factory = factory
        self.button = None
        self.checkbox = None

    def create_ui(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()

    def interact(self):
        self.button.click()
        self.checkbox.select()


if __name__ == "__main__":
    # Example of using Windows factory
    windows_factory = WindowsFactory()
    app1 = Application(windows_factory)
    app1.create_ui()
    print("Windows UI Interaction:")
    app1.interact()

    print("\n")

    # Example of using MacOS factory
    mac_factory = MacFactory()
    app2 = Application(mac_factory)
    app2.create_ui()
    print("MacOS UI Interaction:")
    app2.interact()
