from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Athlete(Base):
    __tablename__ = 'athletes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    cpf = Column(String, unique=True, index=True)
    training_center = Column(String)
    category = Column(String)

# Configuração do banco de dados
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
