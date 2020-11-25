import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",passwd="root123",database="studentdb")

# try:
#     cur = con.cursor()
#     cur.execute("show databases")
#     for i in cur:
#         print(i)
#     print()
# except :
#     con.rollback()

# try:
#     cur = con.cursor()
#     cur.execute("show tables")
#     for i in cur:
#         print(i)
# except :
#     con.rollback()

# try:
#     cur = con.cursor()
#     cur.execute("create table student(roll int , name varchar(20),mks int)")
#     cur.execute("insert into student values (101,'Ajit',80)")
#     cur.execute("insert into student values (102,'Amit',60)")
#     cur.execute("insert into student values (103,'Abhi',40)")
#     cur.execute("insert into student values (104,'Atul',88)")
#     print("Record Inserted Successfully..")
#     con.commit()
# except :
#     if t == True:
#         print("Table Already Exist..")
#     else:
#         print("Some Error..")
#     con.rollback()
# con.close()

# try:
#     cur = con.cursor()
#     cur.execute("select * from student")
#     res = cur.fetchall()
#     for i in res:
#         roll = i[0]
#         name= i[1]
#         mks = i[2]
#         print(roll,name,mks)
#     print("Displayed Successfully..")
#     con.commit()
# except :
#     con.rollback()
# con.close()

try:
    cur = con.cursor()
    # cur.execute("update student set roll = 123 where name = 'ajit'")
    cur.execute("select * from student")
    res = cur.fetchall()

    for i in res:
        roll = i[0]
        name= i[1]
        mks = i[2]

        print(roll,name,mks)

    print("Displayed Successfully..")
    con.commit()
    
except :
    con.rollback()
con.close()    
    
print("Connection Closed..")    
