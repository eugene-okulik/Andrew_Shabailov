import allure


class StatusCode:

    @allure.step('Check that status code is 200')
    def check_status_code_is_200(self, response):
        assert response.status_code == 200, \
            f'Expected status code 200, but got {response.status_code}'
