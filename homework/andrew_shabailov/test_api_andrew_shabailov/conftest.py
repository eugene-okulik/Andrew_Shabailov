import pytest
from endpoints.create_student import CreateStudent
from endpoints.read_student import ReadStudent
from endpoints.update_student import UpdateStudent
from endpoints.delete_student import DeleteStudent
from endpoints.patch_student import PatchStudent

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
