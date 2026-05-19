import requests
import allure
from endpoints.create_student import CreateStudent

class UpdateStudent(CreateStudent):
    base_url = CreateStudent.base_url
    update_response = None

    @allure.title('Update student information fully')
    @allure.description("Проверяем обновление всей информации о студенте")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("api", "smoke", "regression")
    @allure.step('Update student information')
    def update_student(self, student_id, payload):
        self.update_response = requests.put(f'{self.base_url}/'
                                            f'{student_id}', json=payload)
        return self.update_response

    @allure.title('Update student information partially')
    @allure.description("Проверяем обновление данных о студенте прошло успешно")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("api", "smoke", "regression")
    @allure.step('Success updating student information')
    def update_status_code_is_200(self):
        assert self.update_response.status_code == 200, 'Item was not updated'
