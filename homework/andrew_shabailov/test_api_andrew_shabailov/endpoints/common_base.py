import allure
import requests


class Base:
    base_url = 'http://objapi.course.qa-practice.com/object'
    headers = {'Content-Type': 'application/json'}

    def __init__(self):
        self.response = None

    @property
    def json(self):
        if self.response is not None:
            return self.response.json()
        return None

    @allure.step('Check that status code is 200')
    def check_status_code_is_200(self):
        assert self.response.status_code == 200, \
            f'Expected status code 200, but got {self.response.status_code}'

    @allure.title('Read student name')
    @allure.description("Проверяем ожидаемое имя студента")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("api", "smoke", "regression")
    @allure.story("Get student information")
    @allure.step('There is appropriate student name')
    def check_student_name(self, student_id, student_name):
        self.response = requests.get(f'{self.base_url}/{student_id}')
        assert self.response.json()['name'] == student_name, \
            'Student names not match'

    @allure.title('Read student data')
    @allure.description("Проверяем ожидаемые данные о курсе студента")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("api", "smoke", "regression")
    @allure.story("Get student information")
    @allure.step('There is appropriate student information')
    def check_student_data(self, student_id, student_data):
        self.response = requests.get(f'{self.base_url}/{student_id}')
        assert self.response.json()['data']['student'] == student_data, \
            'Student data not match'

    @allure.title('Read teacher name')
    @allure.description("Проверяем ожидаемые данные об учителе студента")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("api", "smoke", "regression")
    @allure.story("Get student information")
    @allure.step('There is appropriate teacher data')
    def check_teacher_data(self, student_id, teacher_data):
        self.response = requests.get(f'{self.base_url}/{student_id}')
        assert self.response.json()['data']['teacher'] == teacher_data, \
            'Teacher data not match'
