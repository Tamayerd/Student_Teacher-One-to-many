from sqlalchemy import create_engine, Integer, Column, String, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, Session

Base = declarative_base()


class Teacher(Base):
     __tablename__= "teacher"
     id = Column(Integer, primary_key = True ) 
     teacher_name = Column('Teacher Name',String(30), nullable= False)
     teacher_field = Column('Teacher Field', String(30))

     def __str__(self):
        return "{} - {}".format(self.id, self.teacher_name,self.teacher_field)

     def __repr__(self):
        return self.__str__()

     
class  Student(Base) :
   
   __tablename__ = "student"

   id = Column(Integer(), primary_key = True ) 
   name = Column('Name', String(100) , nullable = False) 
   student_class = Column('Student Class', String(4), nullable = False)
   student_note = Column('Student Note', String(4))
   
   teacher_id = Column('Teacher ID', Integer, ForeignKey("teacher.id"))
   teacher = relationship("Teacher", backref = 'students')
   #teacher_name = Column('Teacher Name',String, Session.query(Teacher).filter(Teacher.id).)


 

     
db = 'sqlite:///okul.db'
engine = create_engine(db, echo = True)
Base.metadata.create_all(engine) #database oluşturma
session = Session(bind=engine)



session.add_all([
      Teacher(teacher_name = "Melda", teacher_field = "History"),
      Teacher(teacher_name = "Serkan", teacher_field = "English"),
      Teacher(teacher_name = "Mehmet", teacher_field = "Turkish")])

new_teacher = session.query(Teacher).filter(Teacher.teacher_name == "Serkan").one()

new_teacher.students = [Student(name = "Ali", student_class = "1-A",student_note = "60")]
session.commit()






