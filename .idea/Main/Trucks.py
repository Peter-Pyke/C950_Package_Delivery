
# This is my Truck class which allows me to create instances of trucks with the following attributes
class Truck:
    # Truck class constructor
    def __init__(self, distance_traveled, current_time, truck_number):
        self.distance_traveled = distance_traveled
        self.current_time = current_time
        self.table = []
        self.current_location = "4001 South 700 East"
        self.not_full = True
        self.truck_number = truck_number

    # This function inserts a packageID into the table attribute of the truck
    def insert(self, item):
        package_id = item
        self.table.append(package_id)
        return True

    # This function updates the location attribute of the truck
    def update_location(self, address):
        self.current_location = address

    # This function updates the current time attribute of the truck
    def update_time(self, time):
        self.current_time = time

    # This function updates the distance traveled attribute of the truck
    def update_distance(self, distance_to_add):
        self.distance_traveled += distance_to_add

    # This function returns the total miles traveled by the truck
    def truck_miles(self):
        return self.distance_traveled