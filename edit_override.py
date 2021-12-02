from helpers import make_request, get_user_id
import settings

from json import JSONDecodeError
from canvasapi import Canvas
from canvasapi.exceptions import ResourceDoesNotExist
import pandas as pd
import sys


def main(input_csv):
    """
    Main entry point for the edit_overrid.py script
    Script to edit assignment overrids for a given course
    """

    canvas = Canvas(settings.INSTANCE, settings.TOKEN)

    course_id = input("Enter course id: ")

    try:
        course = canvas.get_course(course_id)
    except Exception:
        print(f"ERROR Unable to find course with ID: {course_id}")
        sys.exit()

    df = pd.read_csv(input_csv)
    student_sis_ids = df["sis_id"].to_list()
    student_canvas_ids = [get_user_id(canvas, x) for x in student_sis_ids]

    print(f"\nStudent Canvas ids: {student_canvas_ids}")

    # Print list of assignments
    assignments = course.get_assignments()
    print("\nList of assignments:")
    for assignment in assignments:
        print(assignment)

    # Id of assignment in () beside the name
    assignment_id = input("Enter ID of assignment to edit: ")

    try:
        assignment = course.get_assignment(assignment_id)
    except ResourceDoesNotExist:
        print(f"ERROR Unable to find assignment with ID: {assignment_id}")
        sys.exit()

    overrides = assignment.get_overrides()

    print("\nCurrent Overrides with IDs")

    all_students = []
    for override in overrides:
        student_ids = override.student_ids
        override_id = override.id
        all_students.extend(student_ids)
        print(f"{len(student_ids)} students ({override_id})")

    override_id = input("\nEnter ID of override to edit: ")

    try:
        override = assignment.get_override(override_id)
    except ResourceDoesNotExist:
        print(f"ERROR Unable to find override with ID: {override_id}")
        sys.exit()

    print(override)

    print("\nCurrent list of students:")
    curr_students = override.student_ids
    for student_id in curr_students:
        print(student_id)

    user_inp = input(
        "Enter 0 to delete override, 1 to remove students, 2 to add students: "
    )

    valid_inputs = {"0", "1", "2"}

    if user_inp not in valid_inputs:
        print("ERROR: Expected input to be either 0, 1 or 2")
        print("Exiting...")
        sys.exit()

    if user_inp == "0":
        try:
            override.delete()
            print("deleted!")
            sys.exit()

        except JSONDecodeError:
            print("Error! Delete failed")
    else:
        if user_inp == "1":
            for student in student_canvas_ids:
                try:
                    curr_students.remove(student)
                except ValueError:
                    print("Student does not exist: " + str(student))
        else:
            for student in student_canvas_ids:
                if student not in curr_students and student not in all_students:
                    curr_students.append(student)

        print("\nUpdated list of students:")
        print(curr_students)

        if len(curr_students) == 0:
            override.delete()
            print("All students were removed so the override was deleted")
            sys.exit()

    post_fields = create_post_fields(override, curr_students)

    response = make_request(
        f"courses/{course_id}/assignments/{assignment_id}/overrides/{override_id}",
        method="PUT",
        post_fields=post_fields,
    )

    if response != None:
        print("successful")


def create_post_fields(override_obj, curr_students):
    """
    Creates post fields object that will be used in the PUT request to update the overrides on the assignment
    """
    try:
        unlock_at = override_obj.__getattribute__("unlock_at")
    except AttributeError:
        unlock_at = None

    try:
        due_at = override_obj.__getattribute__("due_at")
    except AttributeError:
        due_at = None

    try:
        lock_at = override_obj.__getattribute__("lock_at")
    except AttributeError:
        lock_at = None

    post_fields = {}
    post_fields["assignment_override[student_ids][]"] = curr_students
    if unlock_at != None:
        post_fields["assignment_override[unlock_at][]"] = unlock_at
    if due_at != None:
        post_fields["assignment_override[due_at][]"] = due_at
    if lock_at != None:
        post_fields["assignment_override[lock_at][]"] = lock_at

    return post_fields


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_csv = sys.argv[1]
    else:
        print(
            "Please run the program again with the csv file passed as command-line arguments"
        )
        sys.exit()

    main(input_csv)
