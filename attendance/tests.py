from django.test import TestCase,SimpleTestCase
from attendance.models import Student
from django.test import RequestFactory
# Create your tests here.

 
class TestMode(TestCase):
        
    def my_own_function(foo, foo1):
        queryset_response = Student.objects.filter(foo=foo, foo1=foo1)
        store = queryset_response[0].data
        return store
    
    def test_my_own_function(self):
        data = "mydata"
        sample_obj = Student.objects.create(foo="bar", foo1="bar1", data=data)
        result = my_own_function("bar", "bar1")
        self.assertEqual(result, data)
