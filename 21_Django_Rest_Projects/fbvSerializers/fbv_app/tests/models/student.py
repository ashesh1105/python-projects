from django.test import TestCase

from fbv_app.models import Student
from fbv_app.tests.factories import StudentFactory

class StudentModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.Student = StudentFactory._meta.model

    def test_creation_student(self):
        # create
        student = StudentFactory()
        print(f'student.id: {student.id}')
        # read
        student_obj = Student.objects.first()
        print(f'student_obj.id: {student_obj.id}')
        self.assertEqual(student.id, student_obj.id)
        self.assertQuerysetEqual(self.Student.objects.all(), ['<Student: {}>'.format(student)])
