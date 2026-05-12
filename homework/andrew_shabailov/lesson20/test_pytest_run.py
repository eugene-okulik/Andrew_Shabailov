import requests
import pytest


base_url = 'http://objapi.course.qa-practice.com/object'

data_d = {'name': 'Andrew',
            'data': {
                'student': 'Python automation course',
                'teacher': 'Eugene_Okulik',
            }}

data_upd = {'name': 'Andrew_UPD',
            'data': {
                'student': 'Python automation course_UPD',
                'teacher': 'Eugene_Okulik_UPD',
            }}

patch_data = {'name': 'Andrew_PATCH',
            'data': {
                'student': 'Python automation course_PATCH',
                'teacher': 'Eugene_Okulik_PATCH',
            }}


@pytest.fixture()
def new_post_id():
    response = requests.post(url=base_url, json=data_d)
    new_post_id = response.json()['id']
    yield new_post_id
    print('Item deleting')
    requests.delete(url=f'{base_url}/{new_post_id}')


@pytest.fixture()
def created_item_id(request):
    payload = request.param
    response = requests.post(url=base_url, json=payload)
    item_id = response.json()['id']
    yield item_id
    print('Item deleting')
    requests.delete(url=f'{base_url}/{item_id}')


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


def test_get_all_objects(start_end_testing, before_after_testing):
    response = requests.get(base_url)
    object_id = response.json()['data'][0]['id']
    assert object_id == 1, 'Object not found'


@pytest.mark.parametrize('created_item_id', [data_d, data_upd, patch_data], indirect=True)
def test_add_item(before_after_testing, start_end_testing, created_item_id):
    assert created_item_id is not None, 'Item was not added'


def test_get_info_by_id(before_after_testing, start_end_testing, new_post_id):
    response = requests.get(f'{base_url}/{new_post_id}')
    assert response.status_code == 200, 'Object not found'


@pytest.mark.critical
def test_put_object(before_after_testing, start_end_testing, new_post_id):
    response = requests.put(f'{base_url}/{new_post_id}', json=data_upd)
    assert response.status_code == 200, 'Item was not updated'


@pytest.mark.medium
def test_patch_object(before_after_testing, start_end_testing, new_post_id):
    response = requests.patch(f'{base_url}/{new_post_id}', json=patch_data)
    assert response.status_code == 200, 'Item was not patched'
