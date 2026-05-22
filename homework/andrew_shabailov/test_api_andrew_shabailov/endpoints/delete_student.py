import requests
import allure
from endpoints.common_base import Base


class DeleteStudent(Base):

    @allure.title('Delete student')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("api", "smoke", "regression")
    @allure.step('Delete student')
    def delete_student(self, student_id):
        self.response = requests.delete(f'{self.base_url}/{student_id}')
        return self.response
