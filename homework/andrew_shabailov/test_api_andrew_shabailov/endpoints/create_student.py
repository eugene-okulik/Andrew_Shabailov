import requests
import allure
from endpoints.status_code import StatusCode


class CreateStudent(StatusCode):
    base_url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Create new student')
    def create_student(self, payload):
        self.response = requests.post(
            url=self.base_url,
            json=payload,
        )
        self.json = self.response.json()
        return self.response

    @allure.step('Check that student created successfully')
    def create_status_code_is_200(self):
        self.check_status_code_is_200(self.response)

    @allure.step('Check that student has appropriate ID')
    def check_studentID_is_created(self, student_id):
        assert student_id == self.json['id'], 'Student was not created'
