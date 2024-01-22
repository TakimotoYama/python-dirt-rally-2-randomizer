import os.path
import csv

from rally_session import RallySession

# Create class with static methods
class CSVHelper:
    FILE_NAME = 'results.csv'
    HEADER = ['Type', 'Location', 'Course', 'Class', 'Car', 'Leggy\'s Time', 'Roo\'s Time']

    @staticmethod
    def SaveRecord(session: RallySession, leggy_time: str, roo_time: str):
        create_header = False

        if not os.path.exists(CSVHelper.FILE_NAME):
            create_header = True

        file = open(CSVHelper.FILE_NAME, 'a+', encoding='UTF8', newline='')
        writer = csv.writer(file)

        if create_header:
            writer.writerow(CSVHelper.HEADER)

        writer.writerow([session.type, \
            session.location, \
            session.sublocation, \
            session.car_class, \
            session.car, \
            leggy_time, \
            roo_time])
        