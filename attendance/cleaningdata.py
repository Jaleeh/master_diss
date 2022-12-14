import pandas as pd
from django.http import HttpResponseRedirect
import collections


#cleaning function for excel data
def process_file(file_handle):  
    try:
        df =  pd.read_excel(file_handle)
        df.columns =df.columns.str.replace(' ','_').str.replace('%','Percentage').str.replace('(','').str.replace(')','').str.replace('-','_')
    

        handles = ['study_choice','User','Level_of_Study','Year_of_Course',
        'Registration_Status','Course_Title',
        'Course_Code','Teaching_Sessions','Attended',
        'Explained_Absences','Non_Attendance','Percentage_Attendance',
        'Percentage_Attendance_Unexcused','Last_Attendence',
        'Submitted','Explained_Non_Submission','Non_Submission',
        'Within_Late_Period_Flag','Percentage_Submitted','Last_Submitted',
        'Academic_Advising_Sessions','Attended_AA','Explained_Non_Attendances_AA',
        'Non_Attendances_AA','Attendance_Not_Recorded_AA','Percentage_Attendance_AA',
        'Last_Attended_AA']
        
        dataColumns = df.columns
        if collections.Counter(dataColumns) != collections.Counter(handles):
            HttpResponseRedirect('/attendance/error')
        
        #fill out empty rows,columns
        df['Last_Attendence'].fillna("16/10/2017 09:00:00",inplace=True)
        df['Assessments'].fillna(0,inplace=True)
        df['Submitted'].fillna(0,inplace=True)
        df['Explained_Non_Submission'].fillna(0,inplace=True)
        df['Non_Submission'].fillna(0,inplace=True)
        df['Within_Late_Period_Flag'].fillna(0,inplace=True)
        df['Percentage_Submitted'].fillna(0,inplace=True)
        df['Last_Submitted'].fillna("16/10/2017 09:00:00",inplace=True)
        df['Academic_Advising_Sessions'].fillna(0,inplace=True)
        df['Attended_AA'].fillna(0,inplace=True)
        df['Explained_Non_Attendances_AA'].fillna(0,inplace=True)
        df['Non_Attendances_AA'].fillna(0,inplace=True)
        df['Attendance_Not_Recorded_AA'].fillna(0,inplace=True)
        df['Percentage_Attendance_AA'].fillna(0,inplace=True)
        df['Last_Attended_AA'].fillna("16/10/2017 09:00:00",inplace=True)

        #changes format of date
        df['Last_Attendence'] =df['Last_Attendence'].dt.strftime('%Y-%m-%dT%H:%M:%S.%f')
        df['Last_Submitted'] =df['Last_Submitted'].dt.strftime('%Y-%m-%dT%H:%M:%S.%f')
        df['Last_Attended_AA'] =df['Last_Attended_AA'].dt.strftime('%Y-%m-%dT%H:%M:%S.%f')
        dfs = df 
        return dfs
    except:
        HttpResponseRedirect('/attendance/error')   



    #correct column names to match models
