# Script to edit assignment overrides for a given course.

import json
import pandas as pd
import sys
from json import JSONDecodeError
from canvasapi import Canvas
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import add_user_id_col

#Enter corresponding canvas url
url = 'https://ubc.instructure.com' 

_BASE_URL = "https://canvas.ubc.ca/api/v1"

edited_students_list = []

with open("token") as t:
    _TOKEN = t.read()

canvas_access = {'Authorization': 'Bearer ' + _TOKEN}
canvas = Canvas(url, _TOKEN)

course_id = input("Enter course id: ")
course = canvas.get_course(course_id)

if len(sys.argv) > 1:
    add_user_id_col.add_canvas_ids(sys.argv[1], course_id)
    df = pd.read_csv(sys.argv[1])
    edited_students_list = list(map(int, (df['ID']).tolist()))

print(edited_students_list)


def make_request(url, method="GET", post_fields={}):
    # build request
    request = Request(
        "{base_url}/{call_url}".format(base_url=_BASE_URL, call_url=url))
    request.add_header('Authorization', 'Bearer {token}'.format(token=_TOKEN))
    request.method = method
    if post_fields:
        # request.data = urlencode(post_fields).encode()
        request.data = urlencode(post_fields, doseq=True).encode()

    # open request
    try:
        response = urlopen(request)
        # logging.debug("HTTP {code} {reason}".format(
        # code=response.code, reason=response.reason, url=request.full_url))
    except HTTPError as e:
        # logging.error("{}".format(e))
        return

    # decode response
    decoded_response = response.readline().decode("utf-8")
    response_body = json.loads(decoded_response, object_pairs_hook=dict)
    return response_body


def edit_without_attributes():
    response = make_request("courses/{course_id}/assignments/{assignment_id}/overrides/{override_id}"
                            .format(course_id=course_id, assignment_id=assignment_id, override_id=override_id),
                            method="PUT",
                            post_fields={"assignment_override[student_ids][]": curr_students})


assignments = course.get_assignments()
print('List of assignments:')
for assignment in assignments:
    print(assignment)

# Id of assignment in () beside the name
assignment_id = input("Enter ID of assignment to edit: ")

assignment = course.get_assignment(assignment_id)

data = assignment.get_overrides()

print("Current Overrides with IDs")


all_students = []
for element in data:
    all_students.extend(element.student_ids)
    print(str(len(element.__getattribute__('student_ids')))+ ' students ('+ str(element.__getattribute__('id'))+')')


override_id = input("Enter ID of override to edit: ")
override = assignment.get_override(override_id)

print(override)


print("Current list of students:")
curr_students = override.__getattribute__('student_ids')
print(curr_students)

user_inp = input(
    "Enter 0 to delete override, 1 to remove students, 2 to add students: ")

if user_inp == '0':
    try:
        override.delete()
        print("deleted!")

    except JSONDecodeError:
        print('Error! Delete failed')
else:
    if user_inp == '1':
        for student in edited_students_list:
            try:
                curr_students.remove(student)
            except ValueError:
                print("Student does not exist: " + str(student))
    else:
        for student in edited_students_list:
            if student not in curr_students and student not in all_students:
                curr_students.append(student)

    print("Updated list of students:")
    print(curr_students)

    if len(curr_students)==0:
        override.delete()
        print("All students were removed so the override was deleted")
        sys.exit()


try:
    unlock_at = override.__getattribute__('unlock_at')
except AttributeError:
    unlock_at = None

try:
    due_at = override.__getattribute__('due_at')
    print(due_at)
except AttributeError:
    due_at = None 

try:
    lock_at = override.__getattribute__('lock_at')
except AttributeError:
    lock_at = None 

post_fields={}
post_fields["assignment_override[student_ids][]"] = curr_students
if(unlock_at!= None):
    post_fields["assignment_override[unlock_at][]"]=unlock_at
if(due_at!= None):
    post_fields["assignment_override[due_at][]"]=due_at
if(lock_at!= None):
    post_fields["assignment_override[lock_at][]"]=lock_at



response = make_request("courses/{course_id}/assignments/{assignment_id}/overrides/{override_id}"
                            .format(course_id=course_id, assignment_id=assignment_id, override_id=override_id),
                            method="PUT",
                            post_fields= post_fields)

if(response.status_code == 200):
print("successful")
else
print("unsuccessful")