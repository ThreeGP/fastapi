from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, DECIMAL, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta
from api.database import Base



class CarBrand(Base):
    __tablename__ = 'brands'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(55), nullable=False)
    

class CarColor(Base):
    __tablename__ = 'colors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(55), nullable=False)


# class Car(Base):
#     __tablename__ = 'cars'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     brand_id = Column(Integer, ForeignKey("brands.id", ondelete="RESTRICT"), nullable=False)
#     color_id = Column(Integer, ForeignKey("colors.id", ondelete="RESTRICT"), nullable=False)
#     model = Column(String(55), nullable=False)
#     year = Column(Integer, nullable=False)
#     registration_number = Column(String(20), unique=True, nullable=False)
#     availability = Column(Boolean, default=True)
#     daily_cost = Column(DECIMAL(7, 2), nullable=False)
#     date_created = Column(DateTime, default=datetime.now)
#     date_updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
#     brand = relationship("CarBrand")
#     color = relationship("CarColor")

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(55), nullable=False)
    last_name = Column(String(55), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone_number = Column(String(55), nullable=False)


# class Rentals(Base):
#     __tablename__ = 'rentals'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     customer_id = Column(Integer, ForeignKey("customers.id", ondelete="DO NOTHING"), nullable=False)
#     car_id = Column(Integer, ForeignKey("cars.id", ondelete="DO NOTHING"), nullable=False)
#     date_rented = Column(DateTime, default=datetime.now)
#     date_returned = Column(DateTime, default=lambda: datetime.now() + timedelta(days=7))
    
#     customer = relationship("Customer")
#     car = relationship("Car")



# SubscriptionPlan.metadata.create_all(bind=engine)

