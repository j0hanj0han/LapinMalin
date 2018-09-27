import requests

SPOKY_ID = "14"


def put_spoky_colors():
    payload = {
              "r": 100,
              "b": 200,
              "g": 100
            }

    response = requests.put('https://labhcs.sbx-aas.gotocloud.io/spoky/14/color', verify=False, json=payload)
    print(response.status_code)

put_spoky_colors()


def get_spoky():
    response = requests.get("https://labhcs.sbx-aas.gotocloud.io/spoky", verify=False)
    print(response.status_code)
    print(response.json())

#get_spoky()