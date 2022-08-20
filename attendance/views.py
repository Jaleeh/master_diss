from django.shortcuts import render
import pandas as pd
from django.contrib import messages
from attendance.models import Student
from sqlalchemy import create_engine
from .filters import StudentFilter
import plotly.express as px
from attendance.cleaningdata import process_file
from django.http import HttpResponseRedirect,HttpResponse



#function to upload csv file
def index(request):
   template =  "attendance/index.html"
   prompt = {"warning" : "must be in sussex university attendance csv format"}
   if request.method == "GET":
        return render(request,template ,prompt)
        
   csv_file = request.FILES['file'] #uploaded file
  
   if not csv_file.name.endswith('.csv'): #error if not csv
        messages.error(request,'This is not a CSV file')
        return HttpResponseRedirect('/attendance/error') 

   saving = process_file(csv_file) #from cleaningdata.py cleans data

#code to save as 'file.csv' ,read and store into database
   if not saving.empty :
      saved_csv = saving.to_csv('file.csv')#convert to csv

      data = pd.read_csv('file.csv')
      engine = create_engine('sqlite:///db.sqlite3') #connection to sqlite3 database
         
      data.to_sql(Student._meta.db_table,if_exists = 'replace',con=engine,index = False)
      return HttpResponseRedirect('/attendance/visuals') # navigates to visuals page after uploading file
   else:
      return HttpResponseRedirect('/attendance/error')#error page

def errorpage(request):
   return render(request, "attendance/error.html")


#filtering data from filters.py
def visBar(request):
 
   student = Student.objects.all()
   student_filter = StudentFilter(request.GET,queryset=student)
   ps = student_filter.qs
   project_data = [ {
               'Users': str(s.User),
               'Teaching Sessions': s.Teaching_Sessions,
               'Attended Sessions': s.Attended ,
               'Course Title': s.Course_Title, 
               'Submitted':s.Submitted 
         }  for s in ps
      ]

   df = pd.DataFrame(project_data)
  
   chartt = barPlot(df)
   context = {'student_filter':student_filter, 'gra': chartt }
   return render(request, 'attendance/visuals.html', context)

def visAvg(request):
 
   student = Student.objects.all()
   student_filter = StudentFilter(request.GET,queryset=student)
   ps = student_filter.qs
   project_data = [ {
               'Users': str(s.User),
               'Teaching Sessions': s.Teaching_Sessions,
               'Attended Sessions': s.Attended ,
               'Course Title': s.Course_Title, 
               'Submitted':s.Submitted 
         }  for s in ps
      ]

   df = pd.DataFrame(project_data)
  
   chartt = avgPlot(df)
   context = {'student_filter':student_filter, 'gra': chartt }
   return render(request, 'attendance/averagebar.html', context)

def visBox(request):
 
   student = Student.objects.all()
   student_filter = StudentFilter(request.GET,queryset=student)
   ps = student_filter.qs
   project_data = [ {
               'Users': str(s.User),
               'Teaching Sessions': s.Teaching_Sessions,
               'Attended Sessions': s.Attended ,
               'Course Title': s.Course_Title, 
               'Submitted':s.Submitted 
         }  for s in ps
      ]

   df = pd.DataFrame(project_data)
  
   chartt = boxPlot(df)

   context = {'student_filter':student_filter, 'gra': chartt }
   return render(request, 'attendance/boxplot.html', context)




def visScatter(request):
 
   student = Student.objects.all()
   student_filter = StudentFilter(request.GET,queryset=student)
   ps = student_filter.qs
   project_data = [ {
               'Users': str(s.User),
               'Teaching Sessions': s.Teaching_Sessions,
               'Attended Sessions': s.Attended ,
               'Course Title': s.Course_Title, 
               'Submitted':s.Submitted 
         }  for s in ps
      ]

   df = pd.DataFrame(project_data)
  
   chartt = scatterPlot(df)
   context = {'student_filter':student_filter, 'gra': chartt }
   return render(request, 'attendance/scatterplot.html', context)

#functions for different data visuals

def barPlot(df):#bar chart which 
   if not df.empty:
      fig = px.bar(df, x="Users", y="Teaching Sessions", title='Attendance Data', color="Attended Sessions")
      chartt = fig.to_html()
      return chartt

def boxPlot(df): #box plot graph
   if not df.empty:
      fig = px.box(df, x="Users", y="Attended Sessions")
      chartt = fig.to_html()
      return chartt

def avgPlot(df): #bar chart which shows student average attended sessions over a term
   if not df.empty:
      fig = px.bar(df.groupby(['Users']).mean().reset_index(), x="Users", y="Attended Sessions")
      avg = df["Attended Sessions"].mean()# calculates average of selected columns
      fig.add_hline(y=avg) #produces a line to compare against average over a 
      chartt = fig.to_html()
      return chartt

def scatterPlot(df):#combine student attended and assessments submitted
   if not df.empty:
      fig = px.scatter(df, x="Submitted", y="Attended Sessions",color = 'Users')
      chartt = fig.to_html()
      return chartt

