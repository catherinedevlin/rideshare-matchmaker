from geopy.distance import vincenty
from traveler import Traveler
import pdb

def make_groups(destination, travelers):
    carpool_groups = {}

    for traveler in travelers:
        carpool_groups[traveler] = get_nearby_travelers(traveler, travelers)

    return carpool_groups

def get_nearby_travelers(traveler, travelers):
    return [traveler2 for traveler2 in travelers if carpool_match(traveler, traveler2)]

def carpool_match(traveler1, traveler2):
    if traveler1 is traveler2: return False
    distance = vincenty(traveler1.point(), traveler2.point())
    return distance.miles < acceptable_miles_away()

def acceptable_miles_away():
    return 10 # placeholder because later this might be complicated

if __name__ == '__main__':
    ohio_union = (39.997794, -83.008511)
    adam_from_france = Traveler(46.333423, 2.798206)
    face_from_columbus = Traveler(39.960956, -82.994692)
    dave_from_columbus = Traveler(39.961589, -82.992026)
    bill_from_des_moines = Traveler(41.554605, -93.636682)
    susy_from_des_moines = Traveler(41.554854, -93.634928)

    test_travelers = [adam_from_france, face_from_columbus, dave_from_columbus,
                      bill_from_des_moines, susy_from_des_moines]

    carpool_groups = make_groups(ohio_union, test_travelers)
    
    assert carpool_groups[adam_from_france] == []
    assert carpool_groups[face_from_columbus] == [dave_from_columbus]
    assert carpool_groups[bill_from_des_moines] == [susy_from_des_moines]
