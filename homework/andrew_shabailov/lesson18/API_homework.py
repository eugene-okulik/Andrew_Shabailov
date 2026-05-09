import requests


base_url = 'http://objapi.course.qa-practice.com/object'

def get_all_objects():
    response = requests.get(base_url)
    object_id = response.json()['data'][0]['id']
    assert object_id == 1, 'No object found'
    return object_id


def get_info_by_id():
    object_id = get_all_objects()
    response = requests.get(f'{base_url}/{object_id}')
    assert response.status_code == 200, 'Object not found'


def post_object():
    name = 'Andrew Shabailov'
    data = {'name': name,
            'data': {
                'student': 'Python automation course',
                'teacher': 'Eugene_Okulik',
            }}
    response = requests.post(url=base_url, json=data)
    post_id = response.json()['id']
    assert response.status_code == 200, 'Item was not created'
    return post_id


def put_object():
    post_id = post_object()
    name = 'Andrew Shabailov'
    data = {'name': name,
            'data': {
                'student': 'Python automation course_UPD',
                'teacher': 'Eugene_Okulik_UPD',
            }}
    response = requests.put(f'{base_url}/{post_id}', json=data)
    assert response.status_code == 200, 'Item was not updated'


def patch_object():
    post_id = post_object()
    name = 'Andrew Shabailov'
    data = {'name': name,
            'data': {
                'student': 'Python automation course_PATCH',
                'teacher': 'Eugene_Okulik_PATCH',
            }}
    response = requests.patch(f'{base_url}/{post_id}', json=data)
    assert response.status_code == 200, 'Item was not patched'


def delete_object():
    post_id = post_object()
    response = requests.delete(f'{base_url}/{post_id}')
    assert response.text == f'Object with id {post_id} successfully deleted', 'Wrong response text'
