import sqlite3
db_name = 'quiz.sqlite'
conn = None
curor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()

def clear_db():
    ''' видаляє всі таблиці '''
    open()
    query = '''DROP TABLE IF EXISTS students'''
    do(query)
    query = '''DROP TABLE IF EXISTS courses'''
    do(query)
    
    close()

    
def create():
    open()    
    
    query = '''CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                Name Text,
                age INTEGER,
                major Text
                
                )'''
     
    do(query)
    query = '''CREATE TABLE IF NOT EXISTS courses (
                course_id INTEGER PRIMARY KEY,
                course_name TEXT,
                instructor TEXT
                
                )'''
     
    do(query)
    query = '''CREATE TABLE IF NOT EXISTS relation (
                course_id INTEGER,
                student_id INTEGER,
                PRIMARY KEY(
                    course_id, student_id
                ),
                foreign KEY(student_id) REFERENCES students(id), foreign KEY(course_id) REFERENCES courses(course_id)
                )'''
     
    do(query)


def show(table):
    query = 'SELECT * FROM ' + table
    open()
    cursor.execute(query)
    print(cursor.fetchall())
    close()

def show_tables():
    show('students')
    show('courses')

def new_course(cours_data):
    query = '''
            INSERT INTO courses(
            course_name,
            instructor
            )
            VALUES(?,?)
    '''
    cursor.execute(query, cours_data)
    conn.commit()

def new_student(student_data):
    query = '''INSERT INTO students(
            name,
            age,
            major
    )
    VALUES(?,?,?)
    '''
    cursor.execute(query, student_data)
    conn.commit()

def main():
    clear_db()
    create()
    
    while True:
        try:
            ans = int(input("1 - новий курс, 2 - новий студент, 3 - зв'язок, 0 - завершити: "))
            if  ans == 1:
                new_course(input('Введіть назву курсу та інструктора через ,: ').split(', '))
            elif ans == 2:
                new_student(input('Ім’я, вік і спеціальність через ,: ').split(', '))
            elif ans == 0:
                break
            elif ans == 3:
                pass
            
            else:
                print('Не вірний ввід, спробуйте ще раз:(')
        except:
            print('Не вірний ввід, спробуйте ще раз:(')

    


if __name__ == "__main__":
    main()
