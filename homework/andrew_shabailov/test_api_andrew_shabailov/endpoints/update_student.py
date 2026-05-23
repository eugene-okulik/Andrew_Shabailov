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
        self.response = requests.put(
            f'{self.base_url}/{student_id}', json=payload
        )
        return self.response
