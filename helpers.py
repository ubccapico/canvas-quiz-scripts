import pandas as pd
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError
import json
import settings

BASE_URL = settings.INSTANCE + "/api/v1"


def make_request(url, method="GET", post_fields={}):
    request = Request("{base_url}/{call_url}".format(base_url=BASE_URL, call_url=url))
    request.add_header("Authorization", f"Bearer {settings.TOKEN}")
    request.method = method
    if post_fields:
        request.data = urlencode(post_fields, doseq=True).encode()
        print(request.data)
    try:
        response = urlopen(request)
    except HTTPError as e:
        print(e)
        raise (e)

    decoded_response = response.readline().decode("utf-8")
    response_body = json.loads(decoded_response, object_pairs_hook=dict)

    return response_body


# def get_student(course_id, student_id):
#     try:
#         response = make_request(
#         "courses/{course_id}/users/sis_user_id:{user_id}?include[]=enrollments".format(course_id=course_id, user_id=student_id,))
#         return response['id']
#     except Exception as e:
#         print(f"ERROR: Unable to get student with ID: {student_id}")
#         return "NOT FOUND"


# def add_canvas_ids(input_file, course_id):
#     df = pd.read_csv(input_file)
#     try:

#         user_ids = df["canvas_id"]

#     except KeyError:
#         sis_ids = df['sis_id']
#         user_ids = []

#         for student_id in sis_ids:
#             user_ids.append(get_student(course_id, student_id))

#         df['canvas_id'] = user_ids
#         df.to_csv(input_file, index=False)
