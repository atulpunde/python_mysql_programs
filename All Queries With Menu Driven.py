import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",passwd="root123",database="studentdb")

cur = con.cursor()

def Insert():
    try:
        n = int(input("How Many record you want to insert = "))
        for i in range(n):
            print(f"\nFor Employee {i+1}:")
            empid = int(input("Employee id = "))
            name = input("Name = ")
            age = int(input("Age = "))
            cur.execute("insert into employee(empid,name,age) values(%s,%s,%s)",(empid,name,age))
    except:
        con.rollback()
    print("\nRecord Inserted Successfully..")
    con.commit()

    ##First Way To Insert Record
    empid = int(input("Enter Employee id = "))
    name = input("Enter name = ")
    age = int(input("Enter age = "))
    query = "insert into employee(empid,name,age) values(%s,%s,%s)"
    args = (empid,name,age)
    cur.execute(query,args)

    ### Second Way To Insert Record
    # empid = int(input("Enter Employee id = "))
    # name = input("Enter name = ")
    # age = int(input("Enter age = "))
    # cur.execute("insert into employee(empid,name,age) values(%s,%s,%s)",(empid,name,age))

def Update():
    print("\t1. Update Employee Id")
    print("\t2. Update Name")
    print("\t3. Update Age")
    print("\t4. Previous Menu")
    ch = int(input("Enter Your Choice = "))
    
    if ch==1:
        empid = int(input("Update Employee set  empid = "))
        name = input("Where name = ")
        cur.execute("update Employee set empid = %s where name = %s",(empid,name))
    
    if ch==2:
        name = input("Update Employee set  name = ")
        empid = input("Where empid = ")
        cur.execute("update Employee set name = %s where empid = %s",(name,empid))

    if ch==3:
        age = input("Update Employee set  age = ")
        name = input("Where name = ")
        cur.execute("update Employee set age = %s where name = %s",(age,name))

    if ch==4:
        pass

    con.commit()

def Delete():
    print("Delete By ")
    print("\t1. Employee Id")
    print("\t2. Name")
    print("\t3. Age")
    print("\t4. Previous Menu")
    ch=int(input("Enter Your Choice = "))

    if ch==1:
        empid = int(input("Enter empid to delete ="))
        cur.execute("delete from employee where empid=%s",(empid,))
        print(f"\nRecord of {empid} deleted Successfully..")

    if ch==2:
        name = int(input("Enter Name to delete ="))
        cur.execute("delete from employee where name=%s",(name,))
        print(f"\nRecords of {name} deleted Successfully..")

    if ch==3:
        age = int(input("Enter Age to delete ="))
        cur.execute("delete from employee where age=%s",(age,))
        print(f"\nRecords of {age} deleted Successfully..")

    if ch>=4:
        pass
    con.commit()
    

def Search():
    name  = input("Enter name to search = ")
    cur.execute("select * from Employee")
    res = cur.fetchall()
    f = True
    for i in res:
        if name == i[1]:
            print(f"\n{name} is Found In Database ..\n")
            f = False
    if f == True:
        print(f"\n{name} is Unavailable In Database ..\n")
    con.commit()


def ShowTable():
    print("\nShowing Table :\n")
    cur.execute("select * from Employee")
    res = cur.fetchall()
    for i in res:
        empid = i[0]
        name= i[1]
        age = i[2]
        print(empid,name,age)
    print("\nDisplayed Successfully..")

def isContinue():
    ic = input("\nDo You Want To Continue..?(Y/N) ")
    if ic=='y' or ic=='Y':
        return True
    else:
        return False


while True:
    print("\n1. Insert ")
    print("2. Update ")
    print("3. Delete ")
    print("4. Search ")
    print("5. Show Table ")
    print("6. EXIT ")
    ch = int(input("Enter Your Choice = "))

    if ch==1:
        Insert()
        if isContinue():
            continue
        else:
            break
    if ch==2:
        Update()
        if isContinue():
            continue
        else:
            break
    if ch==3:
        Delete()
        if isContinue():
            continue
        else:
            break
    if ch==4:
        Search()
        if isContinue():
            continue
        else:
            break
    if ch==5:
        ShowTable()
        if isContinue():
            continue
        else:
            break
    if ch==6:
        break
    if ch>=7:
        print("\nEnter Proper Choice..")
        if isContinue():
            continue
        else:
            break
con.close()    
print("\nConnection Closed..") 
print("\nProgram Terminated..\n")   