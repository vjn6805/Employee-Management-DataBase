print()
print()
print('-------------WELCOME TO EMPLOYEE MANEGMENT PROGRAMME---------------')
print()
print()
import mysql.connector as msql
con=msql.connect(host='localhost',user='root',password='veersql@computer',database='data')
zz=con.cursor()

def regis():
    print()
    import pickle
    print('REGISTER--1')
    print('LOGIN--2')
    a=int(input("Enter: "))
    if a==1:
        f=open('register.dat','ab')
        d={}
        b=input("Enter user name: ")
        c=input("Enter password: ")
        print()
        d['uname']=b
        d['pass']=c
        pickle.dump(d,f)
        f.close()
        print("User Created Successfully.Please Login to use the Programme")
        print()
        regis()
    elif a==2:
        f1=open('register.dat','rb')
        b=input("Enter user name: ")
        c=input("Enter password: ")
        print()
        try:
            while True:
                s=pickle.load(f1)
                if s['uname']==b and s['pass']==c:
                    print("Login succesfull")
                    
                    print()
                    choice()
        except:
            f1.close()
def insertinfo():
    print("Enter employee details")
    print()
    ss=int(input("Enter no. of records: "))
    for i in range(ss):
        a=int(input("Enter employee ID: "))
        b=input("Enter First name: ")
        c=input("Enter Last name: ")
        g=int(input("Enter Age: "))
        d=input("Enter Designation: ")
        z=input("Enter Department: ")
        e=int(input("Enter Salary (per month): "))
        h=int(input("Enter Phone number: "))
        q="insert into employeeinfo values({},'{}','{}',{},'{}','{}',{},{})".format(a,b,c,g,d,z,e,h)
        zz.execute(q)
        con.commit()
    print()
    print()
    print("----------Employee data entered succesfully-------------")
    print()
    print("Do you want to print the records?....y/n")
    a=input("Enter: ")
    if a=='y':
        totalinfo()
    else:
        print("Thank You")
def totalinfo():

    q='select * from employeeinfo'
    zz.execute(q)
    a=zz.fetchall()
    con.commit()
    print('(Eid, FName, LName, Age, Desig., Dept., Salary, PhNo.)')
    for j in a:
        print()
        print(j)
def salary():
   ss=input("enter your name :")
   print()
   a="select Salary from employeeinfo where First_Name='{}'".format(ss)
   zz.execute(a)
   salary=zz.fetchall()
   for x in salary:
       print(x,"is your current salary",ss)
def updatesalary():
    
    nam=int(input("enter EID: "))
    ww=input("Enter First Name")
    zz.execute("update employeeinfo set Salary=Salary+Salary*10/100 where E_ID={} and First_Name='{}'".format(nam,ww))
    
    con.commit()
    print()
    print("Updation Successfull")
    
    f=input("Do you want to print the entire data?...y/n:")
    print()
    if f=='y':
        totalinfo()
def updatedesig():
    nam=int(input("enter EID: "))
    ww=input("Enter First Name")
    q=input("Enter new Designation: ")
    w=input("Enter Department: ")
    zz.execute("update employeeinfo set Designation='{}' and Department='{}' where E_ID={} and First_Name='{}'".format(q,w,nam,ww))
    
    con.commit()
    print()
    print("Updation Successfull")
    
    f=input("Do you want to print the entire data?...y/n:")
    print()
    if f=='y':
        totalinfo()
def getinfo():       
   a=int(input("Enter EID: "))
   b=input("Enter Name: ")
   print()
   q="select * from employeeinfo where E_ID={} and First_Name='{}'".format(a,b)
   zz.execute(q)
   e=zz.fetchall()
   print('(Eid, FName, LName, Age, Desig., Dept., Salary, PhNo.)')
   print()
   for x in e:
       print(x)
def logout():
    print()
    print("Thank you for using the programme")
    print()
    print("Logout successfull")
def choice():
    print()
    print("------Choose Option to Proceed------")
    print()
    print("Insert values into Database....1")
    print("Print Data....2")
    print("Know Salary....3")
    print("Get Employee Info....4")
    print("Update Data....5")
    print("Logout....6")
    print()
    a=int(input("Enter your choice: "))
    if a==1:
        print()
        insertinfo()
    elif a==2:
        print()
        totalinfo()
    elif a==3:
        print()
        salary()
    elif a==4:
        print()
        getinfo()
    elif a==5:
        print()
        print("Enter '1' to update Salary or '2' to update Designation")
        b=int(input("Enter your choice: "))
        if b==1:
            updatesalary()
        else:
            updatedesig()
    elif a==6:
        logout()

regis()

print()
print()

choice()
