import mysql.connector as connection

con = connection.connect(host="localhost", user="root", database="test", password="password")


def execute(q):
    cursor = con.cursor()
    cursor.execute(q)
    con.commit()


def test(q):
    cursor = con.cursor()
    cursor.execute(q)
    # cursor.execute(q)
    data = cursor.fetchall()
    for i in data:
        pass
        # print(i)
    return data


def INSERT(username, password):
    values_query = '''
    INSERT INTO login
    values("%s","%s");''' % (username, password)
    print(values_query)
    execute(values_query)



#########################################################
'''initial_query=
CREATE TABLE login
(username varchar(20) primary key,
password varchar(20));
initial_query=
CREATE TABLE EMPLOYEE
(employee_name varchar(20),
employee_id int primary key,
doj date,
Cost_to_Company int,
80C int,
80D int,
rent int);
'''


#execute(initial_query)
def create_new_user(username, password):
    # Y=check(username)
    # if Y == "access "
    INSERT(username, password)


def check(USERNAME, passw):
    q = "SELECT PASSWORD FROM LOGIN WHERE USERNAME = '%s';" % USERNAME
    y = test(q)
    # print(y)
    if [(passw,)] == y:
        return "access granted"
    else:
        return "access denied"
    # return q
# INSERT("a","p")

def add_employee(name,id,doj,ctc,C_80Exemption,D_80Exemption,rent):
    values_query = '''
    INSERT INTO EMPLOYEE
    values("%s","%s","%s","%s","%s","%s","%s");''' % (name,id,doj,ctc,C_80Exemption,D_80Exemption,rent)
    execute(values_query)

def info(id):
    q = "Select * from EMPLOYEE where employee_id = '%s';" % id
    y = test(q)
    return y

add_employee("p3",8,"2023-04-22",400000,4040,404,204)