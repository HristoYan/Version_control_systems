# Това е от ChatGPT не схванах каво точно искат пък и исках да спестя време да си работя по курсовия проект.
# Доста сложничка задача за начинаещи, не мислиш ли?

import simpy
import random
import numpy as np


class BoatLandingSimulation:
    def __init__(self, env, passenger_arrival_rate, boat_arrival_rate, max_pier_capacity, boat_capacity_dist, N):
        self.env = env
        self.passenger_arrival_rate = passenger_arrival_rate  # Avg time between passenger appearances
        self.boat_arrival_rate = boat_arrival_rate  # Avg time between boat arrivals
        self.max_pier_capacity = max_pier_capacity  # Max people allowed on the pier at a time
        self.boat_capacity_dist = boat_capacity_dist  # Distribution of boat seat capacity
        self.N = N  # Maximum number of people on the pier allowed
        self.pier = []  # People waiting at the pier
        self.passengers_waiting_times = []  # Track passenger waiting times

    def passenger_generator(self):
        """Generates passengers arriving at the pier."""
        passenger_id = 0
        while True:
            yield self.env.timeout(random.expovariate(1.0 / self.passenger_arrival_rate))
            if len(self.pier) < self.max_pier_capacity:
                passenger_id += 1
                arrival_time = self.env.now
                self.pier.append((passenger_id, arrival_time))
                print(
                    f"Passenger {passenger_id} arrived at the pier at {arrival_time:.2f}. Total passengers: {len(self.pier)}")

    def boat_generator(self):
        """Generates boats arriving at the pier."""
        boat_id = 0
        while True:
            yield self.env.timeout(random.expovariate(1.0 / self.boat_arrival_rate))
            boat_id += 1
            boat_capacity = random.choice(self.boat_capacity_dist)  # Boat arrives with random capacity
            print(f"Boat {boat_id} arrived at {self.env.now:.2f} with {boat_capacity} seats.")
            self.board_passengers(boat_capacity)

    def board_passengers(self, boat_capacity):
        """Boards passengers onto the boat, if seats are available."""
        boarded_passengers = 0
        while boat_capacity > 0 and self.pier:
            passenger_id, arrival_time = self.pier.pop(0)
            wait_time = self.env.now - arrival_time
            self.passengers_waiting_times.append(wait_time)
            boat_capacity -= 1
            boarded_passengers += 1
            print(f"Passenger {passenger_id} boarded the boat after waiting {wait_time:.2f} time units.")

        print(f"Boat departs with {boarded_passengers} passengers onboard, remaining seats: {boat_capacity}")

    def run_simulation(self, simulation_time):
        """Runs the simulation for a specified amount of time."""
        self.env.process(self.passenger_generator())
        self.env.process(self.boat_generator())
        self.env.run(until=simulation_time)

    def calculate_results(self):
        """Calculates and displays average waiting time and other metrics."""
        if self.passengers_waiting_times:
            avg_waiting_time = np.mean(self.passengers_waiting_times)
            print(f"Average waiting time for passengers: {avg_waiting_time:.2f} time units.")
        else:
            print("No passengers boarded the boats during the simulation.")

        if len(self.pier) > self.N:
            print(f"Warning: There were more than {self.N} passengers on the pier at some point.")
        else:
            print(f"At no point were there more than {self.N} passengers on the pier.")


# Simulation parameters
random.seed(42)
env = simpy.Environment()
passenger_arrival_rate = 5  # Passengers arrive every 5 time units (on average)
boat_arrival_rate = 15  # Boats arrive every 15 time units (on average)
max_pier_capacity = 50  # Maximum 50 passengers on the pier at a time
boat_capacity_dist = [10, 20, 30]  # Boats have random capacity of 10, 20, or 30 seats
N = 40  # We want to ensure no more than 40 passengers on the pier

# Create simulation instance
simulation = BoatLandingSimulation(env, passenger_arrival_rate, boat_arrival_rate, max_pier_capacity,
                                   boat_capacity_dist, N)

# Run the simulation for 100 time units
simulation.run_simulation(100)

# Display results
simulation.calculate_results()
