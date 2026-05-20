import requests
import allure
from endpoints.create_student import CreateStudent


class ReadStudent(CreateStudent):
    base_url = CreateStudent.base_url
    read_response = None

    @allure.step('Send GET request for student')
    def read_student(self, student_id):
        self.read_response = requests.get(f'{self.base_url}/{student_id}')
        return self.read_response

    @allure.story("Get student information")
    @allure.title('Read student information')
    @allure.description("Проверяем наличие информации о студенте")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("api", "smoke", "regression")
    @allure.step('Check status code is 200')
    def read_status_code_is_200(self):
        self.check_status_code_is_200(self.read_response)
