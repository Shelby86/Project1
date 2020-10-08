from api_proj.Base import Base


class Positions(Base):


    def add_position(self):
        headers = self.headers
        url = "http://skryabin.com/recruit/api/v1/positions"
        with open ("post_position_info.json", "r") as file:
            position_info = file.read()

        response = self.sess.post(url=url, headers=headers, data=position_info)

        self.response_status = response.status_code
        response_dict = response.json()
        job_id = str(response_dict["id"])
        return job_id

        # print(response_status)
        # regex = '(id":)([0-9]{4})'
        # self.id = re.search(regex,response_body)
        # re.search
        # print(self.id.group(2))
        # return self.id.group(2)

    def remove_position(self,job_id):
        headers = self.headers
        url = f"http://skryabin.com/recruit/api/v1/positions/{job_id}"
        print(job_id)
        result = self.sess.delete(url=url, headers=headers)
        response_code = result.status_code

        return response_code

    def put_position(self,job_id):
        headers = self.headers
        url = f"http://skryabin.com/recruit/api/v1/positions/{job_id}"
        with open ("put_position.json", "r") as file:
            put_position_info = file.read()

        response = self.sess.put(url=url, headers=headers, data=put_position_info)
        response_dict = response.json()

        return response_dict

    def patch_position(self,job_id):
        headers = self.headers
        url = f"http://skryabin.com/recruit/api/v1/positions/{job_id}"
        with open("patch.json", "r") as file:
            patch_position_info = file.read()

        response = self.sess.patch(url=url, headers=headers, data=patch_position_info)
        response_dict = response.json()

        return response_dict

    def get_position(self, job_id):
        headers = self.headers
        url = f"http://skryabin.com/recruit/api/v1/positions/{job_id}"
        headers = self.headers
        response = self.sess.get(url=url, headers=headers)
        response_code = response.status_code
        response_body = response.json()
        responses = {
           "response_code": response_code,
           "response_body": response_body
        }

        return responses

    def get_all_positions(self):
        headers = {'Content-Type': 'application/json'}
        url = "https://skryabin.com/recruit/api/v1/positions"
        response = self.sess.get(url=url, headers=headers)
        response_code = response.status_code
        response_body = response.json()
        results = {
            "response_code":response_code,
            "response_body": response_body
        }

        return results
































