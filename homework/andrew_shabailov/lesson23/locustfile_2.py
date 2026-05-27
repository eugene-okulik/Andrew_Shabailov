from locust import HttpUser, task, between


class Student(HttpUser):
    student_id = 1
    wait_time = between(1, 2)


    @task
    def get_all_students(self):
        self.client.get("/")


    @task
    def get_student_by_id(self):
        self.client.get("/student_id")
