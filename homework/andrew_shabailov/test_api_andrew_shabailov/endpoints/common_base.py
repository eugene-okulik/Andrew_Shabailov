import allure


class Base:
    base_url = 'http://objapi.course.qa-practice.com/object'
    headers = {'Content-Type': 'application/json'}

    def __init__(self):
        self.response = None
        self.json = None

    @allure.step('Check that status code is 200')
    def check_status_code_is_200(self):
        assert self.response.status_code == 200, \
            f'Expected status code 200, but got {self.response.status_code}'
