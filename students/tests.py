from django.test import TestCase
from django.contrib.auth.models import User
from students.models import Student, Enrollment
# Create your tests here.
class StudentEnrollmentTest(TestCase):
    def setUp(self):
        admin_user = User.objects.create_superuser(username='TestAdmin',password='1234567')
        return super().setUp()
    
    def test_admin(self):
        count = User.objects.count()
        self.assertEqual(count, 1)

