import requests
import pytest
import allure


base_url = 'http://objapi.course.qa-practice.com/object'

data_d = {
    'name': 'Andrew',
    'data': {
        'student': 'Python automation course',
        'teacher': 'Eugene_Okulik',
    }
}

data_upd = {
    'name': 'Andrew_UPD',
    'data': {
        'student': 'Python automation course_UPD',
        'teacher': 'Eugene_Okulik_UPD',
    }
}

patch_data = {
    'name': 'Andrew_PATCH',
    'data': {
        'student': 'Python automation course_PATCH',
        'teacher': 'Eugene_Okulik_PATCH',
    }
}


@pytest.fixture()
def create_new_item():
    response = requests.post(url=base_url, json=data_d)
    new_item_id = response.json()['id']
    yield new_item_id
    print('Item deleting')
    requests.delete(url=f'{base_url}/{new_item_id}')


@pytest.fixture(scope='session')
def start_end_testing():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def before_after_testing():
    print('Before test')
    yield
    print('After test')


@allure.story("Get item by ID")
@allure.title('Get all objects')
@allure.description("Получаем весь список студентов, проверяем что есть студент с ID = 1")
@allure.severity(allure.severity_level.NORMAL)
def test_get_all_objects(start_end_testing, before_after_testing):
    response = requests.get(base_url)
    object_id = response.json()['data'][0]['id']
    assert object_id == 1, 'Object not found'


@allure.story("Get item by ID")
@allure.title(f"Check student {'payload'} has acceptable data for the post request")
@allure.description("Добавляем студента с различным описанием")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("api", "smoke", "regression")
@pytest.mark.parametrize('payload', [data_d, data_upd, patch_data])
def test_add_student(before_after_testing, start_end_testing, payload):
    with allure.step("Отправляем запрос"):
        response = requests.post(url=base_url, json=payload)
    with allure.step("Получаем ID созданного студента для последующего удаления записи"):
        new_item_id = response.json()['id']
    with allure.step("Ожидаем что запрос прошел успешно и имеет статус код - 200"):
        assert response.status_code == 200, 'Item was not created'
    with allure.step("Объявляем что студент будет удален"):
        print('Item deleting')
    with allure.step("Удаляем созданного студента"):
        requests.delete(url=f'{base_url}/{new_item_id}')


@allure.story("Get item by ID")
@allure.title('Get student information by ID')
@allure.description("Получаем информацию о студенте по его ID")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("api", "smoke", "regression")
def test_get_info_by_id(before_after_testing, start_end_testing, create_new_item):
    response = requests.get(f'{base_url}/{create_new_item}')
    assert response.status_code == 200, 'Object not found'


@allure.story("Get item by ID")
@allure.title('Update student information')
@allure.description("Проверяем обновление данных о студенте")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("api", "smoke", "regression")
@pytest.mark.critical
def test_put_object(before_after_testing, start_end_testing, create_new_item):
    response = requests.put(f'{base_url}/{create_new_item}', json=data_upd)
    assert response.status_code == 200, 'Item was not updated'


@allure.story("Get item by ID")
@allure.title('Update student information partially')
@allure.description("Проверяем обновление определенных данных о студенте")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("api", "smoke", "regression")
@pytest.mark.medium
def test_patch_object(before_after_testing, start_end_testing, create_new_item):
    response = requests.patch(f'{base_url}/{create_new_item}', json=patch_data)
    assert response.status_code == 200, 'Item was not patched'


@allure.story("Get item by ID")
@allure.title('Delete student')
@allure.description("Проверяем удаление студента")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("api", "smoke", "regression")
def test_delete_object(before_after_testing, start_end_testing, create_new_item):
    response = requests.delete(f'{base_url}/{create_new_item}')
    assert response.text == f'Object with id {create_new_item} successfully deleted', 'Wrong response text'
