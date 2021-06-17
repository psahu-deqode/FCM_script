import json

import requests

with open("event.csv") as f:
    list2 = [str(row.split()[0]) for row in f]


def send_fcm_with_rest(list2, title=None, body=None, image=None, data_message=None):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=AAAAfRVjqX8:APA91bHtxxpFWg33uD4Wj-Vlp915l6WZVjOZrbpkwgTlP5GnIrgLLHnDRlxTcrg9-Y'
                         '-7f95PTR6AB_GwF5BahUtPjsi3_f3aRIrAFXcQH5HoK-B9suEqXPikQr8tLBbgCjnNAR-oGPgR',
        'Content-Type': 'application/json'
    }
    url = 'https://fcm.googleapis.com/fcm/send'
    payload = {
        "registration_ids": list2,
        "collapse_key": "type_a",
        "data": {
            "notification": {
                "title": "Title of Your Notification",
                "body": "Body of Your Notification",
            }
        }

    }
    print(json.dumps(payload))
    resp = requests.post(url, headers=headers, data=json.dumps(payload))

    print(resp.text.encode('utf8'), flush=True)
    return resp


send_fcm_with_rest(list2)
