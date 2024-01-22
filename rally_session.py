class RallySession():
    def __init__(self, type, location, sublocation, has_sublocation, car_class, car):
        self.type               = type
        self.location           = location
        self.sublocation        = sublocation
        self.has_sublocation    = has_sublocation
        self.car_class          = car_class
        self.car                = car

    def __str__(self):
        new_line = '\n'
        tab = '\t'
        return  ("\n===========================================\n"
                f"Type:{tab}{tab}{self.type}{new_line}"
                f"Location:{tab}{self.location}{new_line}"
                f"{f'Course:{tab}{tab}{self.sublocation}{new_line}' if self.has_sublocation else ''}"
                f"Class:{tab}{tab}{self.car_class}{new_line}"
                f"Car:{tab}{tab}{self.car}{new_line}"
                "===========================================\n")