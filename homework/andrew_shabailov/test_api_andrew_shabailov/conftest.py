import pytest
from endpoints.create_student import CreateStudent
from endpoints.read_student import ReadStudent
from endpoints.update_student import UpdateStudent
from endpoints.delete_student import DeleteStudent
from endpoints.patch_student import PatchStudent


data_d = {
        'name': 'Andrew',
        'data': {
            'student': 'Python automation course',
            'teacher': 'Eugene_Okulik',
        }
    }


@pytest.fixture()
def create_student_endpoint():
    return CreateStudent()


@pytest.fixture()
def read_student_endpoint():
    return ReadStudent()


@pytest.fixture()
def update_student_endpoint():
    return UpdateStudent()


@pytest.fixture()
def delete_student_endpoint():
    return DeleteStudent()


@pytest.fixture()
def patch_student_endpoint():
    return PatchStudent()


@pytest.fixture()
def student_id():
    create_student = CreateStudent()
    create_student.create_student(payload=data_d)
    student_id = create_student.json['id']
    yield student_id
    print('Item deleting')
    delete_student = DeleteStudent()
    delete_student.delete_student(student_id)


@pytest.fixture()
def student_id_to_delete():
    create_student = CreateStudent()
    create_student.create_student(payload=data_d)
    student_id_to_delete = create_student.json['id']
    return student_id_to_delete


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
