from django.test import TestCase
from course import models
from students.models import Enrollment

from course.models import Course

from students.models import Enrollment, Student
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your tests here.


class CourseTest(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create(username='TestAdmin')

    def test_sig(self):
        c1 = models.Course.objects.create(
            title="django for baby", description="", status='p',created_by=self.admin_user,updated_by=self.admin_user)
        self.assertEqual(c1.description, "dessscccc")
        c1.description="Learnnnnnnn(new desc.. )"
        c1.save()
        
