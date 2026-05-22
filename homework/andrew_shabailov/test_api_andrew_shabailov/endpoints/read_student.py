import requests
import allure
from endpoints.common_base import Base


class ReadStudent(Base):

    @allure.step('Send GET request for student')
    def read_student(self, student_id):
        self.response = requests.get(f'{self.base_url}/{student_id}')
        return self.response
