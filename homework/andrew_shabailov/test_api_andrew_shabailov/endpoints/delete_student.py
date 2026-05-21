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

    @allure.title('Delete student')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("api", "smoke", "regression")
    @allure.description("Проверяем удаление студента")
    @allure.step('Student is deleted successfully')
    def delete_status_code_is_200(self):
        self.check_status_code_is_200()
