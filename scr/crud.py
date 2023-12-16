import models
from sqlalchemy.orm import Session

def get_vacpoints(db: Session):
    return db.query(models.Vaccination).all()

def get_cities(db:Session):
    return db.query(models.City).all()
