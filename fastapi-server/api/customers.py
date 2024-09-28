from fastapi import APIRouter, HTTPException, status
from api.crud import get_brands
from api.models import CarBrand
from api.models import Customer
from sqlalchemy.orm import Session
from .database import db_dependency
from pydantic import BaseModel

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


# Schemas

class CreateCustomerSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str



# CRUD Operations

def get_customers(db: Session):
    return db.query(Customer).all()   

def get_customer_by_id(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.id == customer_id).first()

def create_customer(db: Session, customer: CreateCustomerSchema):
    new_customer = Customer(
        first_name=customer.first_name,
        last_name=customer.last_name,
        email = customer.email,
        phone_number = customer.phone_number
    )
    db.add(new_customer)
    db.commit()

def delete_customer(db: Session, customer: Customer):
    db.delete(customer)
    db.commit()


# Routes

@router.get('/')
async def show_all(db: db_dependency):
    customers = get_customers(db)
    return customers

@router.get('/{customer_id}')
async def show_by_id(customer_id: int, db: db_dependency):
    customer = get_customer_by_id(db, customer_id)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return customer

@router.post('/')
async def create(customer: CreateCustomerSchema, db: db_dependency):
    create_customer(db, customer)
    raise HTTPException(status_code=status.HTTP_201_CREATED, detail="User successfuly created")

@router.delete('/{customer_id}')
async def delete_by_id(customer_id: int, db: db_dependency):
    customer = get_customer_by_id(db, customer_id)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    delete_customer(db, customer)
    raise HTTPException(status_code=status.HTTP_200_OK, detail="User deleted successfuly")


# Authorization & Authentication
# Sorting, Filtering, Searchin - Search Query

# JWT Tokens
# REST API
# GraphQL


# LINK: Enpoint
# HEADER: Search Params
# BODY: Body