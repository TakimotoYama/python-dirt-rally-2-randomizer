from session_randomizer import SessionRandomizer
from rally_csv import CSVHelper

def main():
    session = SessionRandomizer.get_random_session()

    print(session)

    leggy_time = input("Enter Leggy's Time: ")
    roo_time = input("Enter Roo's Time: ")

    CSVHelper.SaveRecord(session, leggy_time, roo_time)

if __name__ == '__main__':
    main()