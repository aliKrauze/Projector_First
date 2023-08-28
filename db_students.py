from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from create_engine import engine

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'

    student_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    subjects = relationship('StudentSubject', back_populates='student')


class Subject(Base):
    __tablename__ = 'subject'

    subject_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    students = relationship('StudentSubject', back_populates='subject')


class StudentSubject(Base):
    __tablename__ = 'student_subject'

    student_subject_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.student_id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subject.subject_id'), nullable=False)
    student = relationship('Student', back_populates='subjects')
    subject = relationship('Subject', back_populates='students')


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
