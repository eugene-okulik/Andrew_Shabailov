import requests
import allure
from endpoints.common_base import Base


class PatchStudent(Base):

    @allure.title('Update student information partially')
    @allure.description("Проверяем обновление определенных данных о студенте")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("api", "smoke", "regression")
    @allure.step('Update new student partially')
    def patch_student(self, student_id, payload):
        self.response = requests.patch(f'{self.base_url}/{student_id}', json=payload)
        return self.response

    @allure.description("Проверяем обновление данных о студенте прошло успешно")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("api", "smoke", "regression")
    @allure.step('Check that student was updated partially')
    def patch_status_code_is_200(self):
        self.check_status_code_is_200()
