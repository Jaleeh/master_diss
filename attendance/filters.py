import django_filters
from .models import Student

class StudentFilter(django_filters.FilterSet):
    
    class Meta:
        model = Student
        fields = {
        'User':['iexact'],
        'Level_of_Study':['exact'],
        'Year_of_Course':['exact'],
        'Course_Title':['iexact'],
        'Course_Code':['iexact'],
        
        }