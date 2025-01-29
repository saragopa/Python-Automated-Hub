# Taxi class definition
class Taxi:
    def __init__(self, taxi_id, driver_name, availability=True):
        self.taxi_id = taxi_id  # Unique taxi identifier
        self.driver_name = driver_name  # Driver's name
        self.availability = availability  # Is the taxi available for booking
        self.passenger = None  # Passenger currently in the taxi (if any)

    # Method to book the taxi for a passenger
    def book_taxi(self, passenger):
        if self.availability:
            self.passenger = passenger
            self.availability = False  # Taxi is now unavailable
            print(f"Taxi {self.taxi_id} booked by {passenger.name}.")
        else:
            print(f"Taxi {self.taxi_id} is not available right now.")
    
    # Method to end the ride and make the taxi available again
    def end_ride(self):
        if self.passenger:
            print(f"Ride for {self.passenger.name} completed.")
            self.passenger = None
            self.availability = True  # Taxi is available for the next ride
        else:
            print("No ride to end for this taxi.")


# Passenger class definition
class Passenger:
    def __init__(self, name, contact_info):
        self.name = name  # Passenger's name
        self.contact_info = contact_info  # Passenger's contact info (e.g., phone number)

    # Method for a passenger to request a taxi from a list of taxis
    def request_taxi(self, taxi_list):
        available_taxis = [taxi for taxi in taxi_list if taxi.availability]
        
        if available_taxis:
            chosen_taxi = available_taxis[0]  # Choose the first available taxi
            chosen_taxi.book_taxi(self)
        else:
            print(f"No taxis available for {self.name}. Please try again later.")


# Main function to run the simulation
if __name__ == "__main__":
    # Create some taxis
    taxi1 = Taxi(101, "John Doe")
    taxi2 = Taxi(102, "Jane Smith")

    # Create some passengers
    passenger1 = Passenger("Alice", "555-1234")
    passenger2 = Passenger("Bob", "555-5678")

    # Passenger 1 requests a taxi
    passenger1.request_taxi([taxi1, taxi2])

    # Passenger 2 requests a taxi
    passenger2.request_taxi([taxi1, taxi2])

    # End ride for taxi1 (completing the ride for passenger1)
    taxi1.end_ride()

    # Passenger 2 requests a taxi again after taxi1 became available
    passenger2.request_taxi([taxi1, taxi2])
