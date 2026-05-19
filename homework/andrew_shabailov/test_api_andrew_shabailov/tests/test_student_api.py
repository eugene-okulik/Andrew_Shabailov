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
@pytest.mark.parametrize('payload', TEST_DATA)
def test_add_student(
        start_end_testing,
        before_after_testing,
        payload,
        create_student_endpoint,
        read_student_endpoint,
        delete_student_endpoint
):
    create_student = CreateStudent()
    create_student.create_student(payload=payload)

    student_id = create_student.json['id']
    student_name = create_student.json['name']
    student_data = create_student.json['data']['student']
    teacher_data = create_student.json['data']['teacher']

    create_student.check_student_is_created(
        create_student.post_response.status_code
    )
    create_student.check_studentID_is_created(student_id)

    read_student = ReadStudent()
    read_student.check_student_name(student_id, student_name)
    read_student.check_student_data(student_id, student_data)
    read_student.check_teacher_data(student_id, teacher_data)

    delete_student = DeleteStudent()
    delete_student.delete_student(student_id)


@pytest.mark.positive
def test_get_info_by_student_id(
        start_end_testing,
        before_after_testing,
        create_student_endpoint,
        read_student_endpoint,
        delete_student_endpoint
):
    create_student = CreateStudent()
    create_student.create_student(payload=data_d)

    student_id = create_student.json['id']

    read_student = ReadStudent()
    read_student.read_student(student_id)

    delete_student = DeleteStudent()
    delete_student.delete_student(student_id)


@pytest.mark.positive
def test_update_student(
        start_end_testing,
        before_after_testing,
        create_student_endpoint,
        delete_student_endpoint
):
    create_student = CreateStudent()
    create_student.create_student(payload=data_d)

    student_id = create_student.json['id']

    update_student = UpdateStudent()
    update_student.update_student(student_id, payload=data_upd)
    update_student.update_status_code_is_200()

    delete_student = DeleteStudent()
    delete_student.delete_student(student_id)


@pytest.mark.positive
def test_patch_student(
        start_end_testing,
        before_after_testing,
        create_student_endpoint,
        delete_student_endpoint
):
    create_student = CreateStudent()
    create_student.create_student(payload=data_d)

    student_id = create_student.json['id']

    patch_student = PatchStudent()
    patch_student.patch_student(student_id, payload=patch_data)
    patch_student.patch_status_code_is_200()

    delete_student = DeleteStudent()
    delete_student.delete_student(student_id)


@pytest.mark.positive
def test_delete_student(
        start_end_testing,
        before_after_testing,
        create_student_endpoint,
        delete_student_endpoint
):
    create_student = CreateStudent()
    create_student.create_student(payload=data_d)

    student_id = create_student.json['id']

    delete_student = DeleteStudent()
    delete_student.delete_student(student_id)
    delete_student.check_student_is_deleted()


@pytest.mark.negative
@pytest.mark.parametrize('payload', NEGATIVE_TEST_DATA)
def test_add_student_with_negative_data(
        start_end_testing,
        before_after_testing,
        payload,
        create_student_endpoint,
        read_student_endpoint,
        delete_student_endpoint
):
    create_student = CreateStudent()
    create_student.create_student(payload=payload)

    student_id = create_student.json['id']

    create_student.check_student_is_created(
    create_student.post_response.status_code
    )
    create_student.check_studentID_is_created(student_id)

    delete_student = DeleteStudent()
    delete_student.delete_student(student_id)
