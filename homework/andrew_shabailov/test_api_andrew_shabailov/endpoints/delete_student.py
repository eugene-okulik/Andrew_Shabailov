import requests
import allure
from endpoints.create_student import CreateStudent


class DeleteStudent(CreateStudent):
    delete_response = None
    base_url = CreateStudent.base_url

    @allure.title('Delete student')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("api", "smoke", "regression")
    @allure.step('Delete student')
    def delete_student(self, student_id):
        self.delete_response = requests.delete(f'{self.base_url}/{student_id}')
        return self.delete_response

    @allure.title('Delete student')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("api", "smoke", "regression")
    @allure.description("Проверяем удаление студента")
    @allure.step('Student is deleted successfully')
    def delete_status_code_is_200(self):
        self.check_status_code_is_200(self.delete_response)
