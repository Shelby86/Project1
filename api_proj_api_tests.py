import unittest
import json


import requests


from api_proj.Base import Base
from api_proj.Positions import Positions


class MyTestCase(unittest.TestCase):


    def add_position(self):
        self.positions = Positions()
        self.positions.login()
        job_id = self.positions.add_position()

        assert job_id is not None
        return job_id

    def remove_position(self, job_id):
        self.positions = Positions()
        self.positions.login()
        response = self.positions.remove_position(job_id)

        assert response in range(200,400)

    def put_position(self,job_id):
        self.positions = Positions()
        self.positions.login()
        changes = self.positions.put_position(job_id)

        assert changes["title"] == "Super Senior QA Automation"
        assert changes["address"] == "308 West Way"
        assert changes["state"] == "CA"
        assert changes["zip"] == "94099"
        assert changes["title"] == "Super Senior QA Automation"
        assert changes["description"] == "Must have 7 years experience in Python, Java, C, Cobol, Alogol60, C++, Swift, Rust and LOLCODE"

    def patch_position(self,job_id):
        self.positions = Positions()
        self.positions.login()
        changes = self.positions.patch_position(job_id)

        assert changes["city"] == "Palo Alto"

    def get_position(self,job_id):
        self.positions = Positions()
        self.positions.login()
        response = self.positions.get_position(job_id)
        # return nested dictionary value
        assert response["response_body"]["id"] == int(job_id)
        assert response["response_code"] == 200

    def get_all_poitions(self):
        self.positions = Positions()
        self.positions.login()
        response = self.positions.get_all_positions()

        assert response["response_code"] == 200
        assert len(response["response_body"]) > 0

    def get_non_existing_position(self,job_id):
        self.positions = Positions()
        self.positions.login()
        response = self.positions.get_position(job_id)

        assert response["response_code"] == 400

    def test_position(self):
        job_id= self.add_position()
        self.put_position(job_id)
        self.patch_position(job_id)
        self.get_position(job_id)
        self.get_all_poitions()
        self.remove_position(job_id)
        self.get_non_existing_position(job_id)

if __name__ == '__main__':
    unittest.main()
