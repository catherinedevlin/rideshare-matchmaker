class Traveler:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def point(self):
        return self.latitude, self.longitude