from helpers import make_request, get_user_id
from canvasapi import Canvas
import settings

import pandas as pd
import sys


def print_quizzes(course_id):
    """
    Queries the course (course_id) and print the quiz title, ID and time limit the the console.
    Users will select the quiz from this list.
    """
    response = make_request(f"courses/{course_id}/quizzes")
    quiz_ids = []
    print("List of quizzes:")
    for quiz in response:
        quiz_ids.append(quiz["id"])
        print("")  # line break
        print(quiz["title"])
        print(f"Quiz ID: {str(quiz['id'])}, Time limit: {str(quiz['time_limit'])}")


def moderate(course_id, quiz_id, user_ids, list_of_time_adjustments, choice):
    """
    Given a specific quiz, iterates through a list of students and
    """
    canvas = Canvas(settings.INSTANCE, settings.TOKEN)
    quiz = make_request(f"courses/{course_id}/quizzes/{quiz_id}")
    if choice == "2":
        list_of_time_adjustments = calc_time_multiplicative(
            quiz["time_limit"], list_of_time_adjustments
        )

    for n, user_id in enumerate(user_ids):

        make_request(
            f"courses/{course_id}/quizzes/{quiz_id}/extensions",
            method="POST",
            post_fields={
                "quiz_extensions[][user_id]": user_id,
                "quiz_extensions[][extra_time]": list_of_time_adjustments[n],
            },
        )


def calc_time_multiplicative(time_limit, time):
    """
    Given a list of integers representing multipliers, returns a list of
    the multipliers * the time limit - the initial time limit of the exam
    """
    return [n * time_limit - time_limit for n in time]


def main(input_csv):
    """
    Main entry point for moderate_students.py script
    """

    course_id = input("Enter course ID:")

    quiz_ids = []
    print_quizzes(course_id)

    user_quiz_ids = input("Enter quiz ids to moderate(seperate by space) to moderate: ")

    # READ DATA
    df = pd.read_csv(input_csv)

    user_ids = df["id"].tolist()
    list_of_time_adjustments = df["time"].tolist()

    choice = input("Enter 1 if time in file is additive or 2 if it is multiplicative:")
    if choice == "1" or choice == "2":
        # convert user input for quiz ids to list of integers
        quiz_ids = [int(x) for x in user_quiz_ids.split(" ")]
        for quiz_id in quiz_ids:
            moderate(course_id, quiz_id, user_ids, list_of_time_adjustments, choice)
        print("Finished")
    else:
        print("Invalid input")
        print("Exiting...")
        exit()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        print(
            "Please run the program again with the csv file passed as command-line arguments"
        )
        sys.exit()

    main(input_file)
