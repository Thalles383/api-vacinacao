from fastapi import FastAPI, Depends, status
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/cities/', response_model=list[schemas.CitySchema])
async def home(db: Session = Depends(get_db)):
    vacpoints = crud.get_cities(db)
    return vacpoints

@app.get('/vaccination-points/maceio/', response_model=list[schemas.VaccinationSchema])
async def list_vacpoints(db: Session = Depends(get_db)):
    vacpoints = crud.get_vacpoints(db)
    return vacpoints

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)

