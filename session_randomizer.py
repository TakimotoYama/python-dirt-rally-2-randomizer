import random
from rally import Rally
from rally_cross import RallyCross

class SessionRandomizer():
    @staticmethod
    def get_random_session():
        if random.randint(0, 3) == 0:
            return RallyCross.get_random_session()
        else:
            return Rally.get_random_session()