from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi_pagination import Page, paginate
from . import models, schemas, database
from sqlalchemy import create_engine
engine = create_engine('sqlite:///mydatabase.db')  # usa SQLite com SQLAlchemy

app = FastAPI()

@app.post("/athletes/", response_model=schemas.AthleteDisplay, status_code=201)
def create_athlete(athlete: schemas.AthleteCreate, db: Session = Depends(database.get_db)):
    try:
        db_athlete = models.Athlete(**athlete.dict())
        db.add(db_athlete)
        db.commit()
        db.refresh(db_athlete)
        return db_athlete
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=303, detail=f"Já existe um atleta cadastrado com o cpf: {athlete.cpf}")

@app.get("/athletes/", response_model=Page[schemas.AthleteDisplay])
def read_athletes(skip: int = Query(0, alias="offset"), limit: int = Query(10), db: Session = Depends(database.get_db)):
    athletes = db.query(models.Athlete).offset(skip).limit(limit).all()
    return paginate(athletes)
