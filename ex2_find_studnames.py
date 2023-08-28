from sqlalchemy.orm import sessionmaker
from create_engine import engine
from db_students import Subject, Student, StudentSubject

Session = sessionmaker(bind=engine)
session = Session()

english_students = session.query(Student.name).join(StudentSubject).join(Subject).filter(Subject.name == 'English').all()


for student_name in english_students:
    print(student_name[0])

session.close()
