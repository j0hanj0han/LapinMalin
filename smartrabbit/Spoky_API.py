import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from smartrabbit.config import SPOKY_ID
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


#Set the RGB color
red = {
              "r": 255,
              "b": 0,
              "g": 0
            }

blue = {
              "r": 0,
              "b": 255,
              "g": 0
            }


def put_spoky_color(color):
    payload = color
    response = requests.put('https://labhcs.sbx-aas.gotocloud.io/spoky/' + SPOKY_ID + '/color', verify=False, json=payload)
    print("The new color put is " + response.json())


# get the list of all Spoky
def get_spoky():
    response = requests.get("https://labhcs.sbx-aas.gotocloud.io/spoky", verify=False)
    print(response.status_code)
    print(response.json())


#  get the color of a Spoky
def get_spoky_color():
    response=requests.get('https://labhcs.sbx-aas.gotocloud.io/spoky/' + SPOKY_ID + '/color', verify=False)
    color = response.json()
    return color


# check if the color of a Spoky is blue or red
def check_spoky_color():
    if get_spoky_color() == red:
        print("the color is red")
    elif get_spoky_color() == blue:
        print(" the color is blue")
