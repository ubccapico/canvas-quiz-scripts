import itertools
import pandas as pd
import json
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import sys
import settings
from canvasapi import Canvas


def make_request(url, method="GET", post_fields={}):
    BASE_URL = settings.INSTANCE + "/api/v1"
    # build request
    request = Request("{base_url}/{call_url}".format(base_url=BASE_URL, call_url=url))
    request.add_header("Authorization", "Bearer {token}".format(token=settings.TOKEN))
    request.method = method
    if post_fields:
        request.data = urlencode(post_fields).encode()

    # open request
    try:
        response = urlopen(request)
    except HTTPError as e:
        return

    # decode response
    decoded_response = response.readline().decode("utf-8")
    response_body = json.loads(decoded_response, object_pairs_hook=dict)
    return response_body


# Functions:


def get_quizzes(course_id):
    response = make_request("courses/{course_id}/quizzes".format(course_id=course_id))
    print("List of quizzes:")
    for quiz in response:
        quiz_ids.append(quiz["id"])
        print("")  # line break
        print(quiz["title"])
        print(
            "Quiz ID: "
            + str(quiz["id"])
            + ", "
            + "Time limit: "
            + str(quiz["time_limit"])
        )


def moderate(quiz_id, student_ids, time, choice):
    quiz = make_request(
        "courses/{course_id}/quizzes/{quiz_id}".format(
            course_id=course_id, quiz_id=quiz_id
        )
    )
    if choice == "2":
        time = calc_time_multiplicative(quiz["time_limit"])

    for n, sis_id in enumerate(student_ids):
        canvas = Canvas(settings.INSTANCE, settings.TOKEN)

        user = canvas.get_user(sis_id, "sis_user_id")
        user_id = user.id

        response = make_request(
            "courses/{course_id}/quizzes/{quiz_id}/extensions".format(
                course_id=course_id, quiz_id=quiz_id
            ),
            method="POST",
            post_fields={
                "quiz_extensions[][user_id]": user_id,
                "quiz_extensions[][extra_time]": time[n],
            },
        )


def calc_time_multiplicative(time_limit):
    return [n * time_limit - time_limit for n in time]


if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    print(
        "Please run the program again with the csv file passed as command-line arguments"
    )
    sys.exit()

course_id = input("Enter course ID:")

quiz_ids = []
get_quizzes(course_id)

user_quiz_ids = input("Enter quiz ids to moderate(seperate by space) to moderate: ")


# READ DATA
df = pd.read_csv(input_file)

student_ids = df["sis_id"].tolist()
time = df["time"].tolist()

choice = input("Enter 1 if time in file is additive or 2 if it is multiplicative:")
if choice == "1" or choice == "2":
    quiz_ids = list(map(int, user_quiz_ids.split()))
    for quiz_id in quiz_ids:
        moderate(quiz_id, student_ids, time, choice)
    print("Finished")
else:
    print("Invalid input")
