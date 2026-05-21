import pytest
from endpoints.create_student import CreateStudent
from endpoints.read_student import ReadStudent
from endpoints.update_student import UpdateStudent
from endpoints.delete_student import DeleteStudent
from endpoints.patch_student import PatchStudent
from endpoints.change_student import ChangeStudent
from endpoints.common_base import Base


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

n_data_d = {
    'name': '124*(&*)*(',
    'data': {
        'student': 'Python automation course',
        'teacher': 'Eugene_Okulik',
    }
}

n_data_upd = {
    'name': 'Andrew_UPD',
    'data': {},
}

n_patch_data = {
    'name': 'Andrew_PATCH',
    'data': {
        'student': 'Python automation course_PATCH',
        'teacher': 'Eugene_Okulik_PATCH',
        'EXTRA': 'FIELD^&%^&$%^$%^$'
    }
}

TEST_DATA = [data_d, data_upd, patch_data]
NEGATIVE_TEST_DATA = [n_data_d, n_data_upd, n_patch_data]


@pytest.mark.positive
def test_get_info_by_student_id(
        start_end_testing,
        before_after_testing,
        student_id,
        read_student_endpoint,
):
    read_student_endpoint.read_student(student_id)
    read_student_endpoint.read_status_code_is_200()


@pytest.mark.positive
def test_update_student(
        start_end_testing,
        before_after_testing,
        student_id,
        update_student_endpoint
):
    update_student_endpoint.update_student(student_id, payload=data_upd)
    update_student_endpoint.update_status_code_is_200()


@pytest.mark.positive
def test_patch_student(
        start_end_testing,
        before_after_testing,
        student_id,
        patch_student_endpoint,
):
    patch_student_endpoint.patch_student(student_id, payload=patch_data)
    patch_student_endpoint.patch_status_code_is_200()


@pytest.mark.positive
def test_delete_student(
        start_end_testing,
        before_after_testing,
        student_id_to_delete,
        delete_student_endpoint
):
    delete_student_endpoint.delete_student(student_id_to_delete)
    delete_student_endpoint.delete_status_code_is_200()


@pytest.mark.positive
@pytest.mark.parametrize('payload', TEST_DATA)
def test_add_student(
        start_end_testing,
        before_after_testing,
        payload,
        create_student_endpoint,
        delete_student_endpoint
):
    create_student_endpoint.create_student(payload=payload)

    student_id = create_student_endpoint.json['id']
    student_name = create_student_endpoint.json['name']
    student_data = create_student_endpoint.json['data']['student']
    teacher_data = create_student_endpoint.json['data']['teacher']

    create_student_endpoint.create_status_code_is_200()
    create_student_endpoint.check_studentID_is_created(student_id)

    change_student = ChangeStudent()
    change_student.check_student_name(student_id, student_name)
    change_student.check_student_data(student_id, student_data)
    change_student.check_teacher_data(student_id, teacher_data)

    delete_student_endpoint.delete_student(student_id)


@pytest.mark.negative
@pytest.mark.parametrize('payload', NEGATIVE_TEST_DATA)
def test_add_student_with_negative_data(
        start_end_testing,
        before_after_testing,
        payload,
        create_student_endpoint,
        delete_student_endpoint
):
    create_student_endpoint.create_student(payload=payload)

    student_id = create_student_endpoint.json['id']

    create_student_endpoint.create_status_code_is_200()
    create_student_endpoint.check_studentID_is_created(student_id)

    delete_student_endpoint.delete_student(student_id)
