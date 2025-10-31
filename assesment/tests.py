from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime, timezone

from course.models import Course
from staff.models import Teacher
from students.models import Enrollment


from .models import Assignment

# Create your tests here.
class AssessmentModelTest(TestCase):
   

    def setUp(self):
        self.teacher_user = User.objects.create_user(
            username='testteacher',
            password='password123'
        )
        self.teacher = Teacher.objects.create(
            user=self.teacher_user,
            first_name='sidd',
            last_name='s'
        )
        self.course = Course.objects.create(
            title='Introduction to Django',
        )
        self.assignment = Assignment.objects.create(
            course=self.course,
            teacher=self.teacher,
            title='Test Assignment 1',
            description='This is a test assignment.',
            due_date=datetime.now(timezone.utc)
        )

    def test_assignment_creation(self):
        self.assertEqual(Assignment.objects.count(), 1)
        self.assertEqual(self.assignment.title, 'Test Assignment 1')
        self.assertEqual(self.assignment.course.title, 'Introduction to Django')
        self.assertEqual(self.assignment.teacher.first_name, 'sidd')

