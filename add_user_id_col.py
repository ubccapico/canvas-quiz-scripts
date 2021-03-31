import pandas as pd
import csv
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError
import json

_BASE_URL = "https://canvas.ubc.ca/api/v1"

with open("token") as t:
    _TOKEN = t.read()


def make_request(url, method="GET", post_fields={}):
    request = Request(
        "{base_url}/{call_url}".format(base_url=_BASE_URL, call_url=url))
    request.add_header('Authorization', 'Bearer {token}'.format(token=_TOKEN))
    request.method = method
    if post_fields:
        request.data = urlencode(post_fields, doseq=True).encode()
        print(request.data)

    try:
        response = urlopen(request)
    except HTTPError as e:
        print(e)
        return

    decoded_response = response.readline().decode("utf-8")
    response_body = json.loads(decoded_response, object_pairs_hook=dict)
    return response_body


def get_student(course_id, student_id):
    response = make_request(
        "courses/{course_id}/users/sis_user_id:{user_id}?include[]=enrollments".format(course_id=course_id, user_id=student_id,))
    return response['id']


def add_canvas_ids(input_file, course_id):
    df = pd.read_csv(input_file)
    try:

        user_ids = df['ID']

    except KeyError:
        sis_ids = df['SIS_ID']
        user_ids = []

        for id in sis_ids:
            user_ids.append(get_student(course_id, id))

        df['ID'] = user_ids
        df.to_csv(input_file, index=False)
