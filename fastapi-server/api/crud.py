from sqlalchemy.orm import Session

from api.models import CarBrand


def get_brands(db: Session) :
    brands = db.query(CarBrand).all()
    return brands