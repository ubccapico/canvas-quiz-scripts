import json
import csv
from canvasapi import Canvas
import pandas as pd
import sys
import add_user_id_col


with open("token") as t:
    token = t.read()

url = 'https://ubc.instructure.com'

if (len(sys.argv) > 1):
    input_file = sys.argv[1]
else:
    print("Please run the program again with the csv file passed as command-line arguments")
    sys.exit()

course_id = input("Enter course ID:")
add_user_id_col.add_canvas_ids(input_file, course_id)
canvas = Canvas(url, token)


# Function to assign quiz in Canvas. Takes assignment ID, course ID and students' Canvas user ID.


def assign_quiz(assignment_id, course_id, student_id):
    course = canvas.get_course(course_id)
    assignment = course.get_assignment(assignment_id)
    override = assignment.create_override(
        assignment_override={"student_ids": student_id})


# Creates an array of all assignment IDs and creates a list of arrays containing student IDs for each assignment ID

def process_input(input_file):
    df = pd.read_csv(input_file)
    try:
        user_ids = (df['ID']).tolist()
        assignment_ids = (df['assignment_id']).tolist()
    except NameError:
        print("Column titles not recognized")

    assignment_dict = {}
    # creates dictionary
    for n, id in enumerate(assignment_ids):
        if id in assignment_dict:
            assignment_dict[id].append(user_ids[n])

        else:
            assignment_dict[id] = [user_ids[n]]

    return assignment_dict


assignment_dict = process_input(input_file)

# Calls assign_quiz function once for every assignment ID
for key in assignment_dict:
    assign_quiz(key, course_id, assignment_dict.get(key))
