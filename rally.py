import random
from rally_session import RallySession
from rally_locations import RALLY_LOCATIONS, RALLY_SUBLOCATIONS
from rally_cars import RALLY_CLASSES, RALLY_CLASSES_CARS

class Rally():
    @staticmethod
    def get_random_session():
        location = Rally.get_random_location()
        sublocation = Rally.get_random_sublocation(location)
        car_class = Rally.get_random_class()
        car = Rally.get_random_car(car_class)

        return RallySession("Rally", location, sublocation, True, car_class, car)

    @staticmethod
    def get_random_location():
        return random.choice(RALLY_LOCATIONS)

    @staticmethod
    def get_random_sublocation(location: RALLY_LOCATIONS):
        return random.choice(RALLY_SUBLOCATIONS[location])

    @staticmethod
    def get_random_class():
        return random.choice(RALLY_CLASSES)

    @staticmethod
    def get_random_car(car_class: RALLY_CLASSES):
        return random.choice(RALLY_CLASSES_CARS[car_class])