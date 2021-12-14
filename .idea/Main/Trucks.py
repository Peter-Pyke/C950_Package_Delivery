class Truck:
    def __init__(self, distance_traveled, current_time, truck_number):
        self.distance_traveled = distance_traveled
        self.current_time = current_time
        self.table = []
        self.current_location = "4001 South 700 East"
        self.not_full = True
        self.truck_number = truck_number

    def insert(self, item):
        package_id = item
        self.table.append(package_id)
        return True

    def update_location(self, address):
        self.current_location = address

    def update_time(self, time):
        self.current_time = time

    def update_distance(self, distance_to_add):
        self.distance_traveled += distance_to_add