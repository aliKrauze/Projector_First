from sqlalchemy.orm import sessionmaker
from create_engine import engine
from db_students import Subject, Student, StudentSubject

Session = sessionmaker(bind=engine)
session = Session()

students_data = [
    {'name': 'Bae', 'age': 18},
    {'name': 'Eddy', 'age': 21},
    {'name': 'Lily', 'age': 22},
    {'name': 'Jenny', 'age': 19}
]

for data in students_data:
    student = Student(**data)
    session.add(student)

subjects_data = [
    {'name': 'English'},
    {'name': 'Math'},
    {'name': 'Spanish'},
    {'name': 'Ukrainian'}
]

for data in subjects_data:
    subject = Subject(**data)
    session.add(subject)

student_subject_data = [
    {'student_id': 1, 'subject_id': 1},
    {'student_id': 2, 'subject_id': 2},
    {'student_id': 3, 'subject_id': 3},
    {'student_id': 4, 'subject_id': 4},
    {'student_id': 1, 'subject_id': 3},
]

for data in student_subject_data:
    student_subject = StudentSubject(**data)
    session.add(student_subject)

session.commit()
session.close()
