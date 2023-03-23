from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy import  Column, Integer, String, ForeignKey
  
# строка подключения
sqlite_database = "sqlite:///exel.db"
# создаем движок SqlAlchemy
engine = create_engine(sqlite_database, echo=True)
 
# создаем модель, объекты которой будут храниться в бд
class Base(DeclarativeBase): pass

engine = create_engine(f"sqlite:///exel.db")

class Company(Base):
    __tablename__ = "companies"
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    
    
    
class Fact(Base):
    __tablename__ = "facts"
 
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(ForeignKey("companies.id"))
    


class Forecast(Base):
    __tablename__ = "forecasts"
 
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(ForeignKey("companies.id"))
    
    
  
class Qliq(Base):
    __tablename__ = "qliqs" 
    
    id = Column(Integer, primary_key=True, index=True)
    data_1 = Column(Integer) 
    data_2 = Column(Integer) 
    fact_id = Column(ForeignKey("facts.id"))
    forecast_id = Column(ForeignKey("forecasts.id"))
    
class Qoil(Base):
    __tablename__ = "qoils" 
    
    id = Column(Integer, primary_key=True, index=True)
    data_1 = Column(Integer) 
    data_2 = Column(Integer)
    fact_id = Column(ForeignKey("facts.id")) 
    forecast_id = Column(ForeignKey("forecasts.id")) 
     

# for t in Base.metadata.tables:
#     print(Base.metadata.tables[t])

# print('-------------')  

Base.metadata.create_all(bind=engine)