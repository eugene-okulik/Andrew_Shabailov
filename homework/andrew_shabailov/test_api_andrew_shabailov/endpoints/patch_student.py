import requests
import allure
from endpoints.create_student import CreateStudent


class PatchStudent(CreateStudent):
    base_url = CreateStudent.base_url
    patch_response = None

    @allure.title('Update student information partially')
    @allure.description("Проверяем обновление определенных данных о студенте")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("api", "smoke", "regression")
    @allure.step('Update new student partially')
    def patch_student(self, student_id, payload):
        self.patch_response = requests.patch(f'{self.base_url}/{student_id}', json=payload)
        return self.patch_response

    @allure.description("Проверяем обновление данных о студенте прошло успешно")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("api", "smoke", "regression")
    @allure.step('Check that student was updated partially')
    def patch_status_code_is_200(self):
        self.check_status_code_is_200(self.patch_response)
