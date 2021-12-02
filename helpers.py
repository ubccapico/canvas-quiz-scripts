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


def get_user_id(canvas, sis_id):
    sis_id = int(sis_id)
    user = canvas.get_user(sis_id, "sis_user_id")
    return user.id
