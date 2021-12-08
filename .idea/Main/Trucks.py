class Truck:
    def __init__(self, distance_traveled, current_time, initial_capacity=16):
        self.distance_traveled = distance_traveled
        self.current_time = current_time
        self.table = []
        for i in range(initial_capacity):
            self.table.append(0)

    def insert(self, item):
        package_id = item
        self.table.append(package_id)
        return True