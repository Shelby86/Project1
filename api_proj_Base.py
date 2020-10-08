import json

import requests

import re




# url = "https://skryabin.com/recruit/api/v1/applications"
#
# response = requests.get(url)
#
# content = response.text
# print(content)
#
# status_code = response.status_code
# print(status_code)

class Base:

    def __init__(self,client = None):
        self.client = client
        self.sess = requests.Session()
        self.headers = {"Content-Type": "application/json",
                   "Authorization": "Basic b3dlbkBleGFtcGxlLmNvbTp3ZWxjb21l"}

        if client and isinstance(client, Base):
            self.session = client.session
        else:
            self.session = requests.session

    def login(self):
        with open("login_info.json", "r") as file:
            login_info = file.read()

        url = "https://skryabin.com/recruit/api/v1/login"
        response = requests.post(url = url, headers = self.headers, data= login_info)
        # returns the response as a dictionary
        response_dict = response.json()
        code = response.status_code

        return code















