import requests
import allure
from endpoints.create_student import CreateStudent


class ReadStudent(CreateStudent):
    base_url = CreateStudent.base_url
    read_response = None

    @allure.story("Get student information")
    @allure.title('Read student information')
    @allure.description("Проверяем наличие информации о студенте")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("api", "smoke", "regression")
    @allure.step('There is student data')
    def read_student(self, student_id):
        self.read_response = requests.get(f'{self.base_url}/{student_id}')
        assert self.read_response.status_code == 200, 'Student not read'

    @allure.title('Read student name')
    @allure.description("Проверяем ожидаемое имя студента")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("api", "smoke", "regression")
    @allure.story("Get student information")
    @allure.step('There is appropriate student name')
    def check_student_name(self, student_id, student_name):
        self.read_response = requests.get(f'{self.base_url}/{student_id}')
        assert self.read_response.json()['name'] == student_name, 'Student names not match'

    @allure.title('Read student data')
    @allure.description("Проверяем ожидаемые данные о курсе студента")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("api", "smoke", "regression")
    @allure.story("Get student information")
    @allure.step('There is appropriate student information')
    def check_student_data(self, student_id, student_data):
        self.read_response = requests.get(f'{self.base_url}/{student_id}')
        assert self.read_response.json()['data']['student'] == student_data, 'Student data not match'

    @allure.title('Read teacher name')
    @allure.description("Проверяем ожидаемые данные об учителе студента")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("api", "smoke", "regression")
    @allure.story("Get student information")
    @allure.step('There is appropriate teacher data')
    def check_teacher_data(self, student_id, teacher_data):
        self.read_response = requests.get(f'{self.base_url}/{student_id}')
        assert self.read_response.json()['data']['teacher'] == teacher_data, 'Teacher data not match'
