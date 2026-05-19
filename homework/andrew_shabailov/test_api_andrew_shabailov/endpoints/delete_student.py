import requests
import allure
from endpoints.create_student import CreateStudent


class DeleteStudent(CreateStudent):
    delete_response = None

    @allure.title('Delete student')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("api", "smoke", "regression")
    @allure.step('Delete student')
    def delete_student(self, student_id):
        self.base_url = CreateStudent.base_url
        self.delete_response = requests.delete(f'{self.base_url}/{student_id}')
        return self.delete_response

    @allure.title('Delete student')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("api", "smoke", "regression")
    @allure.description("Проверяем удаление студента")
    @allure.step('Student is deleted successfully')
    def check_student_is_deleted(self):
        assert self.delete_response.status_code == 200, \
            f'Deletion failed! Status: {self.delete_response.status_code}'
