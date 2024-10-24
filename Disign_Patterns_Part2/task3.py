# Subsystem: DVD Player
class DVDPlayer:
    def on(self):
        print("DVD Player is ON")

    def play(self, movie):
        print(f"Playing movie: {movie}")

    def off(self):
        print("DVD Player is OFF")

# Subsystem: Projector
class Projector:
    def on(self):
        print("Projector is ON")

    def set_input(self, input_device):
        print(f"Projector input set to {input_device}")

    def off(self):
        print("Projector is OFF")

# Subsystem: Sound System
class SoundSystem:
    def on(self):
        print("Sound System is ON")

    def set_volume(self, volume):
        print(f"Sound System volume set to {volume}")

    def off(self):
        print("Sound System is OFF")

# Subsystem: Lights
class Lights:
    def dim(self, level):
        print(f"Lights dimmed to {level}%")

    def on(self):
        print("Lights are ON")


# Facade: Home Theater
class HomeTheaterFacade:
    def __init__(self, dvd_player, projector, sound_system, lights):
        self.dvd_player = dvd_player
        self.projector = projector
        self.sound_system = sound_system
        self.lights = lights

    def watch_movie(self, movie):
        print("Setting up movie experience...\n")
        self.lights.dim(20)
        self.projector.on()
        self.projector.set_input("DVD Player")
        self.sound_system.on()
        self.sound_system.set_volume(50)
        self.dvd_player.on()
        self.dvd_player.play(movie)
        print("\nMovie is now playing!")

    def end_movie(self):
        print("\nShutting down movie experience...\n")
        self.dvd_player.off()
        self.sound_system.off()
        self.projector.off()
        self.lights.on()
        print("Movie experience ended.")


if __name__ == "__main__":
    # Create instances of the subsystems
    dvd_player = DVDPlayer()
    projector = Projector()
    sound_system = SoundSystem()
    lights = Lights()

    # Create the home theater facade
    home_theater = HomeTheaterFacade(dvd_player, projector, sound_system, lights)

    # Test: Watch a movie
    home_theater.watch_movie("Inception")

    # Test: End the movie
    home_theater.end_movie()
