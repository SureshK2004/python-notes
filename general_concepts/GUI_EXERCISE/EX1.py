from tkinter import *
from tkcalendar import DateEntry
from suresh.general_concepts.CRUD_OP import insertstuendt
a=Tk()
a.title('web page')
a.geometry('600x600')
a.config(bg='lightblue')
id=IntVar()
name=StringVar()
mark1=IntVar()
mark2=IntVar()
mark3=IntVar()
gender=StringVar()
id.set('')
#name.set('')
mark1.set('')
mark2.set('')
mark3.set('')
Label(a,text='student_id',bg='lightgreen').grid(row=0,column=0)
Entry(a,textvariable=id,bg='lightgrey').grid(row=0,column=1)
Label(a,text='Student_name',bg='lightgreen').grid(row=1,column=0)
Entry(a,textvariable=name,bg='lightgrey').grid(row=1,column=1)
Label(a,text='student_mark1',bg='lightgreen').grid(row=2,column=0)
Entry(a,textvariable=mark1,bg='lightgrey').grid(row=2,column=1)
Label(a,text='student_mark2',bg='lightgreen').grid(row=3,column=0)
Entry(a,textvariable=mark2,bg='lightgrey').grid(row=3,column=1)
Label(a,text='student_mark3',bg='lightgreen').grid(row=4,column=0)
Entry(a,textvariable=mark3,bg='lightgrey').grid(row=4,column=1)
Label(a,text='gender',bg='lightgreen').grid(row=5,column=0)
Radiobutton(a,variable=gender,text='male',value=1).grid(row=5,column=1)
Radiobutton(a,variable=gender,text='female',value=2).grid(row=5,column=2)
Label(a,text='dob',bg='lightgreen').grid(row=6,column=0)
dateofbirth=DateEntry(a)
dateofbirth.grid(row=6,column=1)
Label(a,text='state',bg='lightgreen').grid(row=7,column=0)
statelist=['Tamilnadu','Andhra pradesh','kerala','goa','delhi']
student_loc=StringVar(a)
student_loc.set('select a state')
OptionMenu(a,student_loc,*statelist).grid(row=7,column=1)
Label(a,text='course_intrusted',bg='lightgreen').grid(row=8,column=0)
sql_value=IntVar()
python_value=IntVar()
Django_value=IntVar()
Flask_value=IntVar()
rest_api=IntVar()
Checkbutton(a,variable=sql_value,text='sql',onvalue=1,offvalue=0).grid(row=8,column=1)
Checkbutton(a,variable=python_value,text='python',onvalue=1,offvalue=0).grid(row=8,column=2)
Checkbutton(a,variable=Django_value,text='Django',onvalue=1,offvalue=0).grid(row=8,column=3)
Checkbutton(a,variable=Flask_value,text='Flask',onvalue=1,offvalue=0).grid(row=8,column=4)
Checkbutton(a,variable=rest_api,text='RestAPI',onvalue=1,offvalue=0).grid(row=8,column=5)


def SavetoDB():
    idv=id.get()
    namev=name.get()
    mark1v=mark1.get()
    mark2v=mark2.get()
    mark3v=mark3.get()
    if gender.get()=='1':
        genderv='male'
    else:
        genderv='female'
    dojv=dateofbirth.get()
    loc=student_loc.get()
    ci=[]
    if sql_value.get():
        ci.append('Sql')
    if python_value.get() == 1:
        ci.append('Python')
    if Django_value.get() == 1:
        ci.append('Django')
    if Flask_value.get() == 1:
        ci.append('Flask')
    if rest_api.get() == 1:
        ci.append('RestAPI')
    cifinal="-".join(ci)
        #print(dojv)
    insertstuendt(idv,namev,mark1v,mark2v,mark3v,genderv,dojv,loc,cifinal)
    a.destroy()
    #print(idv,namev,mark1v,mark2v,mark3v,total,average,grade)
Button(a,text='Submit',command=SavetoDB,bg='yellow').grid(row=9,column=1)
a.mainloop()


# steps to add
#1.alter table tablename add column datatype();
#2.open crud operation:
#        goto insertstatement and add column at last
#3.create a box or button or dropdown