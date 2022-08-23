from django.db import models
from django.utils.translation import gettext as _

#models here
class Student(models.Model):
    study_choice = (('UG', 'Undergraduate'),('PGT', 'Postgraduate'))
    User = models.IntegerField(_("User"),primary_key=True)
    Level_of_Study = models.CharField(max_length =3,choices = study_choice)
    Year_of_Course = models.IntegerField(_("Year of Course"))
    Registration_Status = models.CharField(_("Registration Status"),max_length = 100)
    Course_Title = models.CharField(_("Course Title"),max_length = 100)
    Course_Code = models.SlugField(_("Course Code"),max_length = 6)
    Teaching_Sessions =  models.IntegerField(_("Teaching Sessions"))
    Attended = models.IntegerField(_("Sessions Attended"))
    Explained_Absences = models.IntegerField(_("Explained Absences"))
    Non_Attendance = models.IntegerField(_("Non Attendance"))
    Percentage_Attendance = models.FloatField(_("% Attendance"))
    Percentage_Attendance_Unexcused = models.FloatField(_("Percentage attendance (Unexcused)"))
    Last_Attendence = models.DateTimeField(_("Last Attendance"))
    Submitted = models.IntegerField(_("Submitted"))
    Explained_Non_Submission = models.IntegerField(_("Explained Non Submission"))
    Non_Submission = models.IntegerField(_("Non Submission"))
    Within_Late_Period_Flag = models.IntegerField(_("Within Late Period Flag"))
    Percentage_Submitted = models.FloatField(_("Percentage Submitted"))
    Last_Submitted = models.DateTimeField(_("Last Submitted"))
    Academic_Advising_Sessions = models.IntegerField(_("Academic Advising Sessions"))
    Attended_AA = models.IntegerField(_("Attended AA"))
    Explained_Non_Attendances_AA = models.IntegerField(_("Explained Non Attended AA"))
    Non_Attendances_AA = models.IntegerField(_("Non Attendances AA"))
    Attendance_Not_Recorded_AA = models.IntegerField(_("Attendance Not Recorded AA"))
    Percentage_Attendance_AA = models.FloatField(_("Percentage Attendance AA"))
    Last_Attended_AA = models.DateTimeField(_("Last Attended AA"))
