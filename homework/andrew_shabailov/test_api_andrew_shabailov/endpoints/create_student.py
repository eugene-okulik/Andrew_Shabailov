import requests
import allure


class CreateStudent:
    base_url = 'http://objapi.course.qa-practice.com/object'
    post_response = None
    json = None
    headers = {'Content-Type': 'application/json'}
    data_d = {
        'name': 'Andrew',
        'data': {
            'student': 'Python automation course',
            'teacher': 'Eugene_Okulik',
        }
    }

    @allure.step('Create new student')
    def create_student(self, payload):
        self.post_response = requests.post(
            url=self.base_url,
            json=payload,
        )
        self.json = self.post_response.json()
        return self.post_response

    @allure.step('Check that student created successfully')
    def check_student_is_created(self, status_code):
        assert status_code == 200, 'Status code is NOT 200'

    @allure.step('Check that student has appropriate ID')
    def check_studentID_is_created(self, student_id):
        assert student_id == self.json['id'], 'Student was not created'
