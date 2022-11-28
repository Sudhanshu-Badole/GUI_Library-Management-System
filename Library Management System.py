# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 20:12:13 2022

@author: sudha
"""

from tkinter import*
from tkinter import ttk

import pymysql
import datetime
from tkinter import messagebox

root = Tk()
root.title('Student Management System')
root.geometry('1520x780+0+0')
root.resizable(False,False)

#=========================================Function===============================================

def add_data():

    con = pymysql.connect(host='localhost', user='root', password='password')
    mycursor = con.cursor()

    query = 'use librarymangement'
    mycursor.execute(query)
    query = 'insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    mycursor.execute(query, (
        MemberType_var.get(),
                            PRN_NO_var.get(),
                            IDNo_var.get(),
                            FirstName_var.get(),
                            LastName_var.get(),
                            Address1_var.get(),
                            Address2_var.get(),
                            Mobile_var.get(),
                            BookId_var.get(),
                            BookTitle_var.get(),
                            AutherName_var.get(),
                            DateIssued_var.get(),
                            DueDate_var.get(),
                            DaysOnBook_var.get(),
                            Fine_var.get(),
                            ActualPrice_var.get()))
    con.commit()
    fatch_data()
    result = messagebox.showinfo('Success', 'Data added successfully')



def fatch_data():
    con = pymysql.connect(host='localhost', user='root', password='password')
    mycursor = con.cursor()

    query = 'use librarymangement'
    mycursor.execute(query)
    mycursor.execute('select * from library')
    rows=mycursor.fetchall()
    if len(rows)!=0:
        library_table.delete(*library_table.get_children())
        for i in rows:
            library_table.insert('', END,values=i)
        con.commit()
    con.close()
    
    
def get_cursor(event=""):
    cursor_row=library_table.focus()
    content=library_table.item(cursor_row)
    row=content['values']
    
    MemberType_var.set(row[0])
    PRN_NO_var.set(row[1]),
    IDNo_var.set(row[2])
    FirstName_var.set(row[3]),
    LastName_var.set(row[4]),
    Address1_var.set(row[5]),
    Address2_var.set(row[6]),
    Mobile_var.set(row[7]),
    BookId_var.set(row[8]),
    BookTitle_var.set(row[9]),
    AutherName_var.set(row[10]),
    DateIssued_var.set(row[11]),
    DueDate_var.set(row[12]),
    DaysOnBook_var.set(row[13]),
    Fine_var.set(row[14]),
    ActualPrice_var.set(row[15])
    
def showData():
    TextBox.insert(END,'Member Type\t\t'+MemberType_var.get()+'\n')
    TextBox.insert(END,'PRN No: \t\t'+PRN_NO_var.get()+'\n')
    TextBox.insert(END,'ID No: \t\t'+IDNo_var.get()+'\n')
    TextBox.insert(END,'FirstName\t\t'+FirstName_var.get()+'\n')
    TextBox.insert(END,'LastName\t\t'+LastName_var.get()+'\n')
    TextBox.insert(END,'Address1\t\t'+Address1_var.get()+'\n')
    TextBox.insert(END,'Address2\t\t'+Address2_var.get()+'\n')
    TextBox.insert(END,'Mobile No:\t\t'+Mobile_var.get()+'\n')
    TextBox.insert(END,'Book ID: \t\t'+BookId_var.get()+'\n')
    TextBox.insert(END,'Book Title: \t\t'+BookTitle_var.get()+'\n')
    TextBox.insert(END,'Auther: \t\t'+AutherName_var.get()+'\n')
    TextBox.insert(END,'Date Issued: \t\t'+DateIssued_var.get()+'\n')
    TextBox.insert(END,'Due date: \t\t'+DueDate_var.get()+'\n')
    TextBox.insert(END,'Days On Books: \t\t'+DaysOnBook_var.get()+'\n')
    TextBox.insert(END,'Fine: \t\t'+Fine_var.get()+'\n')
    TextBox.insert(END,'Actual Price: \t\t'+ActualPrice_var.get()+'\n')
    
    
def reset():
    MemberType_var.set('')
    PRN_NO_var.set(''),
    IDNo_var.set('');
    FirstName_var.set(''),
    LastName_var.set(''),
    Address1_var.set(''),
    Address2_var.set(''),
    Mobile_var.set(''),
    BookId_var.set(''),
    BookTitle_var.set(''),
    AutherName_var.set(''),
    DateIssued_var.set(''),
    DueDate_var.set(''),
    DaysOnBook_var.set(''),
    Fine_var.set(''),
    ActualPrice_var.set('')
    TextBox.delete('1.0','end')
    
def iExit():
    iExit=messagebox.askyesno('Library Management System','Do you want to exit?')
    if iExit:
        root.destroy()
def delete():
    if PRN_NO_var.get()==''or IDNo_var.get()=='':
        messagebox.showerror('Error','First Select the Member')
    else:
        con = pymysql.connect(host='localhost', user='root', password='password')
        mycursor = con.cursor()

        query = 'use librarymangement'
        mycursor.execute(query)
        query1='delete from library where PRN_no=%s'
        value=PRN_NO_var.get()
        mycursor.execute(query1,value)
        con.commit()
        fatch_data()
        reset()
        con.close()
        
        messagebox.showinfo('Success','Member has been Deleted')
        
def update():
    con = pymysql.connect(host='localhost', user='root', password='password')
    mycursor = con.cursor()

    query = 'use librarymangement'
    mycursor.execute(query)
    mycursor.execute('update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,Mobile=%s,BookId=%s,BookTitle=%s,Auther=%s,DateIssued=%s,datedue=%s,daysonbook=%s,fine=%s,Actualprice=%s where PRN_No=%s', (
        MemberType_var.get(),
                            IDNo_var.get(),
                            FirstName_var.get(),
                            LastName_var.get(),
                            Address1_var.get(),
                            Address2_var.get(),
                            Mobile_var.get(),
                            BookId_var.get(),
                            BookTitle_var.get(),
                            AutherName_var.get(),
                            DateIssued_var.get(),
                            DueDate_var.get(),
                            DaysOnBook_var.get(),
                            Fine_var.get(),
                            ActualPrice_var.get(),
                            PRN_NO_var.get()))
    
    con.commit()
    fatch_data()
    reset()
    con.close()
    messagebox.showinfo('Success','Member has been updated')
# =======================================================Variables===================================================
MemberType_var = StringVar()
PRN_NO_var = StringVar()
IDNo_var = StringVar()
FirstName_var = StringVar()
LastName_var = StringVar()
Address1_var = StringVar()
Address2_var = StringVar()
Mobile_var = StringVar()
BookId_var = StringVar()
BookTitle_var = StringVar()
AutherName_var = StringVar()
DateIssued_var = StringVar()
DueDate_var = StringVar()
DaysOnBook_var = StringVar()
Fine_var = StringVar()
ActualPrice_var = StringVar()


lbltitle=Label(root,text='LIBRARY MANAGEMENT SYSTEM',bg='silver',fg='black',bd=20,relief=RIDGE,font=('times new roman',50,'bold'), padx=2,pady=6)
lbltitle.pack(side=TOP,fill=X)

frame=Frame(root,bd=12,relief=RIDGE,padx=20,bg='silver')
frame.place(x=0,y=130,width=1510,height=400)

#===============================================DataframeLeft======================================================
DataFrameLeft=LabelFrame(frame,text='Library Membership Information',bg='silver',fg='black',bd=12,relief=RIDGE,font=('times new roman',12,'bold'))
DataFrameLeft.place(x=0,y=5,width=900,height=350)

lblMembr=Label(DataFrameLeft,bg='silver',text='Member Type',font=('times new roman',15,'bold'),padx=2,pady=6)
lblMembr.grid(row=0,column=0,sticky=W)

comMember=ttk.Combobox(DataFrameLeft,textvariable=MemberType_var,font=('times new roman',15,'bold'),width=27,state='readonly')
comMember['value']=('Admin Staff','Student','Lecturer')
comMember.grid(row=0,column=1)

lblPRN_NO=Label(DataFrameLeft,text="PRN NO:",font=('arial',15,'bold'),bg="silver",padx=2,pady=6)
lblPRN_NO.grid(row=1,column=0,sticky=W)
txtPRN_NO=Entry(DataFrameLeft,font=('arial',15,'bold'),textvariable=PRN_NO_var,width=25)
txtPRN_NO.grid(row=1,column=1)

lblTitle=Label(DataFrameLeft,text="ID No:",font=('arial',15,'bold'),bg="silver",padx=2,pady=6)
lblTitle.grid(row=2,column=0,sticky=W)
txtTitle=Entry(DataFrameLeft,font=('arial',15,'bold'),textvariable=IDNo_var,width=25)
txtTitle.grid(row=2,column=1)

lblFirstName=Label(DataFrameLeft,text="FirstName:",font=('arial',15,'bold'),bg="silver",padx=2,pady=6)
lblFirstName.grid(row=3,column=0,sticky=W)
txtFirstName=Entry(DataFrameLeft,font=('arial',15,'bold'),textvariable=FirstName_var,width=25)
txtFirstName.grid(row=3,column=1)

lblLastName=Label(DataFrameLeft,text="LastName:",font=('arial',15,'bold'),bg="silver",padx=2,pady=6)
lblLastName.grid(row=4,column=0,sticky=W)
txtLastName=Entry(DataFrameLeft,font=('arial',15,'bold'),textvariable=LastName_var,width=25)
txtLastName.grid(row=4,column=1)

lblAddress1=Label(DataFrameLeft,text="Address1:",font=('arial',15,'bold'),bg="silver",padx=2,pady=6)
lblAddress1.grid(row=5,column=0,sticky=W)
txtAddress1=Entry(DataFrameLeft,font=('arial',15,'bold'),textvariable=Address1_var,width=25)
txtAddress1.grid(row=5,column=1)

lblAddress2=Label(DataFrameLeft,text="Address2:",font=('arial',15,'bold'),bg="silver",padx=2,pady=6)
lblAddress2.grid(row=6,column=0,sticky=W)
txtAddress2=Entry(DataFrameLeft,font=('arial',15,'bold'),textvariable=Address2_var,width=25)
txtAddress2.grid(row=6,column=1)

lblMobile=Label(DataFrameLeft,text="Mobile:",font=('arial',15,'bold'),bg="silver",padx=2,pady=4)
lblMobile.grid(row=7,column=0,sticky=W)
txtMobile=Entry(DataFrameLeft,font=('arial',15,'bold'),textvariable=Mobile_var,width=25)
txtMobile.grid(row=7,column=1)

lblBookId=Label(DataFrameLeft,text="Book Id:",font=('arial',15,'bold'),bg="silver",padx=2,pady=6)
lblBookId.grid(row=0,column=2,sticky=W)
txtBookId=Entry(DataFrameLeft,font=('arial',15,'bold'),textvariable=BookId_var,width=26)
txtBookId.grid(row=0,column=3)

lblBookTitle=Label(DataFrameLeft,text="Book Title:",font=('arial',15,'bold'),bg="silver",padx=2,pady=6)
lblBookTitle.grid(row=1,column=2,sticky=W)
txtBookTitle=Entry(DataFrameLeft,font=('arial',15,'bold'),textvariable=BookTitle_var,width=26)
txtBookTitle.grid(row=1,column=3)

lblAutherName=Label(DataFrameLeft,text="Auther Name:",font=('arial',15,'bold'),bg="silver",padx=2,pady=6)
lblAutherName.grid(row=2,column=2,sticky=W)
txtAutherName=Entry(DataFrameLeft,font=('arial',15,'bold'),textvariable=AutherName_var,width=26)
txtAutherName.grid(row=2,column=3)

lblDateIssued=Label(DataFrameLeft,text="Date Issued:",font=('arial',15,'bold'),bg="silver",padx=2,pady=6)
lblDateIssued.grid(row=3,column=2,sticky=W)
txtDateIssued=Entry(DataFrameLeft,font=('arial',15,'bold'),textvariable=DateIssued_var,width=26)
txtDateIssued.grid(row=3,column=3)

lblDateDue=Label(DataFrameLeft,text="Date Due:",font=('arial',15,'bold'),bg="silver",padx=2,pady=6)
lblDateDue.grid(row=4,column=2,sticky=W)
txtDateDue=Entry(DataFrameLeft,font=('arial',15,'bold'),textvariable=DueDate_var,width=26)
txtDateDue.grid(row=4,column=3)

lblDaysOnBook=Label(DataFrameLeft,text="Days On Book:",font=('arial',15,'bold'),bg="silver",padx=2,pady=6)
lblDaysOnBook.grid(row=5,column=2,sticky=W)
txtDaysOnBook=Entry(DataFrameLeft,font=('arial',15,'bold'),textvariable=DaysOnBook_var,width=26)
txtDaysOnBook.grid(row=5,column=3)

lblFine=Label(DataFrameLeft,text="Fine:",font=('arial',15,'bold'),bg="silver",padx=2,pady=6)
lblFine.grid(row=6,column=2,sticky=W)
txtFine=Entry(DataFrameLeft,font=('arial',15,'bold'),textvariable=Fine_var,width=26)
txtFine.grid(row=6,column=3)

lblActualPrice=Label(DataFrameLeft,text="Actual Price:",font=('arial',15,'bold'),bg="silver",padx=2,pady=6)
lblActualPrice.grid(row=7,column=2,sticky=W)
txtActualPrice=Entry(DataFrameLeft,font=('arial',15,'bold'),textvariable=ActualPrice_var,width=26)
txtActualPrice.grid(row=7,column=3)

#================================================DataFrameRight====================================================

DataFrameRight=LabelFrame(frame,text='Book Details',bg='silver',fg='black',bd=12,relief=RIDGE,font=('times new roman',12,'bold'))
DataFrameRight.place(x=910,y=5,width=540,height=350)

TextBox=Text(DataFrameRight,font=('arial',12,'bold'),width=32,height=16,padx=2,pady=6)
TextBox.grid(row=0,column=2)

listScrollbar=Scrollbar(DataFrameRight)
listScrollbar.grid(row=0,column=1,sticky='ns')

listBooks=['Python Programming','Into Machin Learning','Advance Python','Structures','Let Us C','The Design of Everyday Things',
         'Sustainable Materials','Engineer to Win','An Astronuts Guide to Life','Success Through failure',
         'How to Fail at almost Everything','Engineering Mathematics','Advance Mechanics','Power Electronics',
         'Engineering Physics','Advance Mathematics','Macroeconimics','Advanced economic Theories','Lakshmikant',
         'Mishra and Puri','Spectrum','Sanjiv Verma','Ramesh Singh','Unfinished','You Can Win', 'Wings of Fire']

def SelectBook(event=""):
    value=str(listBox.get(listBox.curselection()))
    x=value
    if (x=='Python Programming'):
        BookId_var.set('BKID1122')
        BookTitle_var.set('python programming')
        AutherName_var.set('Paul Berry')
        d1=datetime.date.today()
        d2=datetime.timedelta(days=15)
        d3=d1+d2
        DateIssued_var.set(d1) 
        DueDate_var.set(d3)
        DaysOnBook_var.set(15)
        Fine_var.set('Rs.50\-')
        ActualPrice_var.set('Rs.500\-')
    
    elif (x=='Into Machin Learning'):
        BookId_var.set('BKID1525')
        BookTitle_var.set('machine learning')
        AutherName_var.set('Andrew Phawl')
        d1=datetime.date.today()
        d2=datetime.timedelta(days=15)
        d3=d1+d2
        DateIssued_var.set(d1) 
        DueDate_var.set(d3)
        DaysOnBook_var.set(15)
        Fine_var.set('Rs.30\-')
        ActualPrice_var.set('Rs.700\-')
    
    elif (x=='Advance Python'):
        BookId_var.set('BKID1262')
        BookTitle_var.set('Advance Python')
        AutherName_var.set('Brain Jones')
        d1=datetime.date.today()
        d2=datetime.timedelta(days=15)
        d3=d1+d2
        DateIssued_var.set(d1) 
        DueDate_var.set(d3)
        DaysOnBook_var.set(15)
        Fine_var.set('Rs.100\-')
        ActualPrice_var.set('Rs.750\-')
    
    elif (x=='Structures'):
        BookId_var.set('BKID1150')
        BookTitle_var.set('Structures and Theories')
        AutherName_var.set('Merry Com')
        d1=datetime.date.today()
        d2=datetime.timedelta(days=15)
        d3=d1+d2
        DateIssued_var.set(d1) 
        DueDate_var.set(d3)
        DaysOnBook_var.set(15)
        Fine_var.set('Rs.No\-')
        ActualPrice_var.set('Rs.250\-')
    
    elif (x=='Let Us C'):
        BookId_var.set('BKID1520')
        BookTitle_var.set('Let Us C')
        AutherName_var.set('Yashwant Kanetkar')
        d1=datetime.date.today()
        d2=datetime.timedelta(days=15)
        d3=d1+d2
        DateIssued_var.set(d1) 
        DueDate_var.set(d3)
        DaysOnBook_var.set(15)
        Fine_var.set('Rs.70\-')
        ActualPrice_var.set('Rs.650\-')

listBox=Listbox(DataFrameRight,font=('arial',12,'bold'),width=20,height=16)
listBox.bind("<<ListboxSelect>>",SelectBook)
listBox.grid(row=0,column=0,padx=4)
listScrollbar.config(command=listBox.yview)

for item in listBooks:
    listBox.insert(END,item)
    
    
# ==================================================Buttons Frame=====================================================



Framebutton=Frame(root,bd=12,relief=RIDGE,padx=20,bg='silver')
Framebutton.place(x=0,y=530,width=1530,height=70)

btnAddData=Button(Framebutton,command=add_data,text='Add Data',font=('arial',12,'bold'),width=23,bg='black',fg='white')
btnAddData.grid(row=0,column=0)

btnShowData=Button(Framebutton,command=showData,text='Show Data',font=('arial',12,'bold'),width=23,bg='black',fg='white')
btnShowData.grid(row=0,column=1)

btnUpdate=Button(Framebutton,command=update,text='Update',font=('arial',12,'bold'),width=23,bg='black',fg='white')
btnUpdate.grid(row=0,column=2)

btnDelete=Button(Framebutton,command=delete,text='Delete',font=('arial',12,'bold'),width=23,bg='black',fg='white')
btnDelete.grid(row=0,column=3)

btnReset=Button(Framebutton,command=reset,text='Reset',font=('arial',12,'bold'),width=23,bg='black',fg='white')
btnReset.grid(row=0,column=4)

btnExit=Button(Framebutton,command=iExit,text='Exit',font=('arial',12,'bold'),width=23,bg='black',fg='white')
btnExit.grid(row=0,column=5)

#======================================Information Frame=================================================
FrameDetails=Frame(root,bd=12,padx=20,bg="#ffe6ff",relief=RIDGE)
FrameDetails.place(x=0,y=600,width=1530,height=175)

Tableframe=Frame(FrameDetails,bd=6,bg="silver")
Tableframe.place(x=0,y=2,width=1460,height=195)

xscroll=ttk.Scrollbar(Tableframe,orient=HORIZONTAL)
yscroll=ttk.Scrollbar(Tableframe,orient=VERTICAL)

library_table=ttk.Treeview(Tableframe,column=('member','prnno','ID','first name','last name','address1',
                                'address2','mobile','book id',
                                'book title','auther name','date issued','due date','days on book','fine','actual price'),
                                xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

xscroll.pack(side=BOTTOM,fill=X)
yscroll.pack(side=RIGHT,fill=Y)

xscroll.config(command=library_table.xview)
yscroll.config(command=library_table.yview)


library_table.heading('member',text='MemberType')
library_table.heading('prnno',text='PRN_NO')
library_table.heading('ID',text='IDNo')
library_table.heading('first name',text='FirstName')
library_table.heading('last name',text='LastName')
library_table.heading('address1',text='Address1')
library_table.heading('address2',text='Address2')
library_table.heading('mobile',text='Mobile')
library_table.heading('book id',text='BookId')
library_table.heading('book title',text='BookTitle')
library_table.heading('auther name',text='AutherName')
library_table.heading('date issued',text='DateIssued')
library_table.heading('due date',text='DueDate')
library_table.heading('days on book',text='DaysOnBook')
library_table.heading('fine',text='Fine')
library_table.heading('actual price',text='ActualPrice')

library_table['show']='headings'
library_table.pack(fill=BOTH,expand=1)

library_table.column('member',width=100)
library_table.column('prnno',width=100)
library_table.column('ID',width=100)
library_table.column('first name',width=100)
library_table.column('last name',width=100)
library_table.column('address1',width=100)
library_table.column('address2',width=100)
library_table.column('mobile',width=100)
library_table.column('book id',width=100)
library_table.column('book title',width=100)
library_table.column('auther name',width=100)
library_table.column('date issued',width=100)
library_table.column('due date',width=100)
library_table.column('days on book',width=100)
library_table.column('fine',width=100)
library_table.column('actual price',width=100)


fatch_data()
library_table.bind('<ButtonRelease-1>',get_cursor)



























root.mainloop()