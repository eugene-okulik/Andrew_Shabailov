import requests
import allure
from endpoints.common_base import Base


class UpdateStudent(Base):

    @allure.title('Update student information fully')
    @allure.description("Проверяем обновление всей информации о студенте")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("api", "smoke", "regression")
    @allure.step('Update student information')
    def update_student(self, student_id, payload):
        self.response = requests.put(f'{self.base_url}/'
                                            f'{student_id}', json=payload)
        return self.response

    @allure.title('Update student information partially')
    @allure.description("Проверяем обновление данных о студенте прошло успешно")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("api", "smoke", "regression")
    @allure.step('Success updating student information')
    def update_status_code_is_200(self):
        self.check_status_code_is_200()
