from django.test import TestCase
from fbvApp.models import Student

# Create your tests here.
class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(id=2, name="Shiela", score=89.91)
        Student.objects.create(id=3, name="Ram", score=87.23)

    def test_student_created(self):
        """Student created"""
        student_Shiela = Student.objects.get(id=2)
        student_Ram = Student.objects.get(id=3)
        self.assertEqual(student_Shiela.name, 'Shiela')
        self.assertEqual(student_Ram.name, 'Ram')

    def test_student_created_with_given_score(self):
        student_Shiela = Student.objects.get(id=2)
        student_Ram = Student.objects.get(id=3)
        self.assertEqual(float(student_Shiela.score), 89.91)
        self.assertEqual(float(student_Ram.score), 87.23)