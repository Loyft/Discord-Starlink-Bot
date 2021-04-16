import json
import urllib.request
from keys import positionstack_api_key

POS_ENDPOINT = "http://api.positionstack.com/v1"


def get_iss_pos():
    print("hi")
    req = urllib.request.Request("http://api.open-notify.org/iss-now.json")
    response = urllib.request.urlopen(req)
    obj = json.loads(response.read())
    pos_long = obj["iss_position"]["longitude"]
    pos_lat = obj["iss_position"]["latitude"]

    req_pos = urllib.request.Request(f"{POS_ENDPOINT}/reverse?access_key={positionstack_api_key}&query={pos_lat},{pos_long}")
    response_pos = urllib.request.urlopen(req_pos)
    obj_pos = json.loads(response_pos.read())

    current_pos = obj_pos["data"][0]

    return current_pos
