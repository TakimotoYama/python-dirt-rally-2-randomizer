import random
from rally_session import RallySession
from rally_cross_locations import RALLY_LOCATIONS
from rally_cross_cars import RALLY_CLASSES, RALLY_CLASSES_CARS

class RallyCross():
    @staticmethod
    def get_random_session():
        location = RallyCross.get_random_location()
        car_class = RallyCross.get_random_class()
        car = RallyCross.get_random_car(car_class)

        return RallySession("Rally Cross", location, None, False, car_class, car)

    @staticmethod
    def get_random_location():
        return random.choice(RALLY_LOCATIONS)

    @staticmethod
    def get_random_class():
        return random.choice(RALLY_CLASSES)

    @staticmethod
    def get_random_car(car_class: RALLY_CLASSES):
        return random.choice(RALLY_CLASSES_CARS[car_class])