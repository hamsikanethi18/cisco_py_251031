from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column,String,Integer,Float,create_engine


Base = declarative_base()


class Employee(Base):
 __tablename__ = 'employees'
 id = Column(Integer,primary_key=True)
 name = Column(String(255), nullable=False)
 job_title = Column(String(255),nullable=False)
 salary = Column(Float,nullable=False)


 def __repr__(self):
  return f'[id= {self.id}, name={self.name}, job_title={self.job_title}, salary={self.salary}]'



#setup database


engine = create_engine('sqlite:///employees_db.sqlite', echo=True) #create a db if not exist


Base.metadata.create_all(engine) #create a table for the model classes


#setup thing for transaction like crud operation
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()


#crud operation
dravid = Employee(name = 'dravid', job_title= 'old coach', salary = 1200)
session.add(dravid)


abhishek = Employee(name = 'abhi', job_title= 'old coach', salary = 1000)
session.add(dravid)
session.commit()


employees = session.query(Employee).all()
print(employees)


abhi = session.query(Employee).filter_by(name='abhishek').first()
print(abhi)


abhishek.salary = 20001
session.commit()




