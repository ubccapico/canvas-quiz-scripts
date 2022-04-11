import pandas as pd
import canvasapi
import sys

import settings


def assign_quiz(canvas, assignment_id, course_id, student_id):
    """
    Function to assign quiz in Canvas. Takes assignment ID, course ID and students' Canvas user ID.
    """
    try:
        course = canvas.get_course(course_id)
        assignment = course.get_assignment(assignment_id)
    except canvasapi.exceptions.Unauthorized as e:
        print(
            f"ERROR: Course ({course_id}) does not exist OR user is not authorized to access"
        )
        return
    except TypeError:
        print(f"ERROR: Course ID must be an INTEGER. Instead given: {course_id}")
        return
    except Exception as e:
        print(
            f"ERROR: Unable to fetch assignment, please check assignment ID: {assignment_id}"
        )
        return

    # Filter out students who could not be found
    student_id = list(filter(lambda x: x != None, student_id))
    if len(student_id) == 0:
        print(
            f"No valid student ids provided for course ({course_id}), assignment ({assignment_id})"
        )
        return

    try:
        assignment.create_override(assignment_override={"student_ids": student_id})
    except canvasapi.exceptions.BadRequest:
        print(
            f"ERROR Unable to add students with ids: {student_id} to assignment. Please ensure all students don't already belong to assignment"
        )


def process_input(canvas, input_csv):
    """
    Creates an dictionary of all assignment IDs and assigns a list containing student IDs for each assignment ID
    """
    df = pd.read_csv(input_csv)

    assignment_dict = {}

    for _, row in df.iterrows():
        assignment_id = row["assignment_id"]
        try:
            user_id = row["id"]
        except canvasapi.exceptions.ResourceDoesNotExist as e:
            print(e)
            print(f"unable to find student: {sis_id}")

        if assignment_id in assignment_dict:
            assignment_dict[assignment_id].append(user_id)

        else:
            assignment_dict[assignment_id] = [user_id]

    return assignment_dict


def main(input_csv):
    """
    Main entry point for assign_quiz.py script
    """

    # Prompt the user for a course ID
    course_id = input("Enter course ID: ")

    canvas = canvasapi.Canvas(settings.INSTANCE, settings.TOKEN)

    # add_canvas_ids(input_csv, course_id)
    assignment_dict = process_input(canvas, input_csv)

    # Calls assign_quiz function once for every assignment ID
    for key in assignment_dict:
        assign_quiz(canvas, key, course_id, assignment_dict.get(key))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_csv = sys.argv[1]
    else:
        print(
            "Please run the program again with the csv file passed as command-line arguments"
        )
        sys.exit()

    main(input_csv)
