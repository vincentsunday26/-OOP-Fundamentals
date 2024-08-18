# Task 1. Vehicle Registration System

class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.registration_number = reg_num
        self.type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

# Example usage:
if __name__ == "__main__":
    # Create a few instances of Vehicle
    car1 = Vehicle("ABC123", "Sedan", "John Doe")
    car2 = Vehicle("XYZ789", "SUV", "Jane Smith")

    # Demonstrate changing the owner
    print(f"Before update: Car1 owner is {car1.owner}")
    car1.update_owner("Alice Brown")
    print(f"After update: Car1 owner is {car1.owner}")


# Task 2.  Event Management System Enhancement

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  # Initialize participant count

    def add_participant(self):
        """Increase participant count."""
        self.participant_count += 1

    def get_participant_count(self):
        """Retrieve the current participant count."""
        return self.participant_count

