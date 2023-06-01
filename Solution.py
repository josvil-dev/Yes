from xml.dom import UserDataHandler

from datetime import datetime

def user_details():

    """

    Prompt user input

    """

    first_name = input("Insert your first name: ")

    while len(first_name) < 3:

        print("Invalid first name")

        first_name = input("Insert your first name: ")

    last_name = input("Insert your last name: ")

    while len(last_name) < 3:

        print("Invalid last name")

        last_name = input("Insert your last name: ")

    cohort = input("Insert your cohort: ")

    while not cohort.isnumeric() or len(cohort) != 4:

        print("Invalid cohort")

        cohort = input("Insert your cohort: ")

    campus = input("Insert the campus you will be attending in: ")

    while campus.lower() not in ["johannesburg", "cape town", "durban", "phokeng"]:

        print("Invalid campus")

        campus = input("Insert the campus you will be attending in: ")

    username = create_user_name(first_name, last_name, cohort, campus)

    print("Your username is:", username)

def create_user_name(first_name, last_name, cohort, final_campus):

    """

    Create and return a valid username

    """

    first_initial = first_name[:1]

    last_initials = last_name[:2]

    cohort_last_two = cohort[-2:]

    campus_abbreviation = user_campus(final_campus)

    return first_initial.lower() + last_initials.lower() + cohort_last_two + campus_abbreviation

def user_campus(campus):

    """

    Return valid campus abbreviations

    """

    campus_abbreviations = {

        "johannesburg": "JHB",

        "cape town": "CPT",

        "durban": "DBN",

        "phokeng": "PHO"

    }

    return campus_abbreviations[campus.lower()]

if __name__ == '__main__':

    user_details()
