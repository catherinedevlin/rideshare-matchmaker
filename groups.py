from geopy.distance import vincenty
from traveler import Traveler

class CarpoolMatcher:
    def __init__(self, destination, travelers, min_distance = 1, relative_distance_percent = .10):
        self.destination = destination
        self.travelers = travelers
        self.min_distance = min_distance
        self.relative_distance_percent = relative_distance_percent

    def make_groups(self):
        carpool_groups = {}

        for traveler in self.travelers:
            carpool_groups[traveler] = self.get_nearby_travelers(traveler)

        return carpool_groups

    def get_nearby_travelers(self, traveler):
        return [traveler2 for traveler2 in self.travelers if self.carpool_match(traveler, traveler2)]

    def carpool_match(self, traveler1, traveler2): 
        if traveler1 is traveler2: return False
        distance = vincenty(traveler1.geolocation, traveler2.geolocation)
        return distance.miles < self.acceptable_miles_away(traveler1)

    def acceptable_miles_away(self, traveler):
        traveler_to_destination_distance = vincenty(traveler.geolocation, self.destination).miles
        return max(self.min_distance, self.relative_distance_percent * traveler_to_destination_distance)


if __name__ == '__main__':
    ohio_union = (39.997794, -83.008511)
    adam_from_france = Traveler(46.333423, 2.798206)
    face_from_columbus = Traveler(39.960956, -82.994692)
    dave_from_columbus = Traveler(39.961589, -82.992026)
    bill_from_des_moines = Traveler(41.554605, -93.636682)
    susy_from_des_moines = Traveler(41.554854, -93.634928)

    test_travelers = [adam_from_france, face_from_columbus, dave_from_columbus,
                      bill_from_des_moines, susy_from_des_moines]

    matcher = CarpoolMatcher(ohio_union, test_travelers)
    carpool_groups = matcher.make_groups()
    
    assert carpool_groups[adam_from_france] == []
    assert carpool_groups[face_from_columbus] == [dave_from_columbus]
    assert carpool_groups[bill_from_des_moines] == [susy_from_des_moines]
