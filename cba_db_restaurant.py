import os
import sys
import datetime 
from sqlalchemy import Column,ForeignKey,Integer,String,Date,Float,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class RestaurantList(Base):
    __tablename__ = 'restaurant_master'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    r_id = Column(Integer, primary_key=True)
    profile_name = Column(String(80), nullable=False)
    address = Column(String(255) , nullable=True)
    pincode = Column(String(30) , nullable=True)
    phone = Column(String(80), nullable=False)
    #city_name = Column(String(80), nullable=False)
    city_id = Column(String(80), nullable=False)
    #area_name = Column(String(80), nullable=False)
    area_id = Column(String(80), nullable=False)
    locality_name = Column(String(80), nullable=False)
    locality_id = Column(String(80), nullable=False)
    #state_name = Column(String(80), nullable=False)
    status =  Column(String(80), nullable=True)
    #created_on = Column(Date ,default=datetime.datetime.now)
    #updated_on = Column(Date , onupdate=datetime.datetime.now)
    #entity_id = Column(Integer , ForeignKey('legal_entity.id'))
    #entity = relationship(LegalEntity)
 

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'r_id': self.r_id,
            'profile_name' : self.profile_name,
            'address'      : self.address,
            'pincode'      : self.pincode,
            'phone'        : self.phone,
            #'city_name'    : self.city_name,
            #'state_name'   : self.state_name,
            #'locality_name': self.locality_name,
            #'area_name'    : self.area_name,
            'area_id'    : self.area_id,
            'city_id'    : self.city_id,
            'locality_id'    : self.locality_id,
            #'created_on'   : self.created_on,
            #'updated_on'   : self.updated_on

        }


class City(Base):
    __tablename__ = 'city'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    c_id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, nullable=False)
    state_id = Column(Integer , nullable=True)
    state_name = Column(String(30) , nullable=True)
    name = Column(String(30) , nullable=True)
    std_code = Column(Integer, nullable=False)
    priority = Column(Integer, nullable=False)
    is_live = Column(Integer, nullable=False)
    is_doplus_city = Column(Integer, nullable=False)
    status =  Column(Integer, nullable=True)
    date_added = Column(Date ,default=datetime.datetime.now)
    date_modified = Column(Date ,default=datetime.datetime.now)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'c_id': self.c_id,
            'parent_id' : self.parent_id,
            'state_id'      : self.state_id,
            'state_name'      : self.state_name,
            'std_code'        : self.std_code,
            'priority'    : self.priority,
            'is_live'   : self.is_live,
            'is_doplus_city': self.is_doplus_city,
            'status'    : self.status,
            'date_added'   : self.date_added,
            'date_modified'   : self.date_modified

        }

class Locality(Base):
    __tablename__ = 'locality'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    l_id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, nullable=False)
    name = Column(String(30) , nullable=True)
    alias = Column(String(30), nullable=False)
    city_id = Column(Integer, nullable=False)
    std_code = Column(Integer, nullable=False)
    status =  Column(Integer, nullable=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'l_id': self.l_id,
            'parent_id' : self.parent_id,
            'name'      : self.name,
            'alias'     : self.alias,
            'city_id'   : self.city_id,
            'std_code'  : self.std_code

        }

class Area(Base):
    __tablename__ = 'area'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    a_id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, nullable=False)
    name = Column(String(30) , nullable=True)
    alias = Column(String(30), nullable=False)
    status =  Column(Integer, nullable=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'a_id': self.a_id,
            'parent_id' : self.parent_id,
            'name'      : self.name,
            'alias'     : self.alias,
            'status'    : self.status
    }

class BookingList(Base):
    __tablename__ = 'booking_master'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    b_id = Column(Integer, primary_key=True)
    disp_id = Column(String(30), nullable=False)
    diner_id = Column(Integer , nullable=True)
    diner_name = Column(String(30), nullable=False)
    diner_phone =  Column(String(30), nullable=True)
    diner_email =  Column(String(30), nullable=True)
    booking_status =  Column(String(30), nullable=True)
    dining_dt_time = Column(Date ,default=datetime.datetime.now)
    tbl_alloc_status=Column(String(30), nullable=True)
    bill_amount=Column(Integer , nullable=True)
    cnt_covers = Column(Integer , nullable=True)
    offer_id= Column(Integer , nullable=True)
    cnt_covers_males= Column(Integer , nullable=True)
    restaurant_id= Column(Integer , nullable=True)

    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'b_id': self.b_id,
            'disp_id' : self.disp_id,
            'diner_id'      : self.diner_id,
            'diner_name'     : self.diner_name,
            'diner_phone'    : self.diner_phone,
            'diner_email'    : self.diner_email,
            'dining_dt_time' : self.dining_dt_time,
            'booking_status' : self.booking_status,
            'tbl_alloc_status' : self.tbl_alloc_status,
            'bill_amount' : self.bill_amount,
            'cnt_covers' : self.cnt_covers,
            'offer_id' : self.offer_id,
            'cnt_covers_males' : self.cnt_covers_males,
            'restaurant_id' : self.restaurant_id,
    }

class DinerList(Base):
    __tablename__ = 'diner'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    d_id = Column(Integer, primary_key=True)
    d_first_name = Column(String(30), nullable=False)
    d_last_name = Column(String(30), nullable=False)
    d_email = Column(String(30), nullable=False)
    d_phone = Column(String(30) , nullable=False)
    booking_cnt = Column(Integer, nullable=False)
    d_password = Column(String(30), nullable=False)
    is_verified = Column(Integer, nullable=False)
    is_do_plus_member = Column(Integer, nullable=True  )
    d_city_id = Column(Integer, nullable=False)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'd_id': self.d_id,
            'd_first_name' : self.d_first_name,
            'd_last_name'  : self.d_last_name,
            'd_email'      : self.d_email,
            'd_phone'      : self.d_phone,
            'booking_cnt'  : self.booking_cnt,
            'is_verified'  : self.is_verified,
            'd_city_id'  : self.d_city_id,
            'd_password'  : self.d_password,
            'is_do_plus_member'  : self.is_do_plus_member,
    }

class OrderList(Base):
    __tablename__ = 'order_master'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    diner_id = Column(String(30), nullable=False)
    obj_id = Column(String(30), nullable=False)
    paid_status = Column(Integer, nullable=False)
    promocode = Column(String(30), nullable=False)
    amount = Column(Integer , nullable=False)
    gst_number = Column(String(20), nullable=False)
    created_on = Column(Date ,default=datetime.datetime.now)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'diner_id' : self.diner_id,
            'obj_id' : self.obj_id,
            'paid_status'  : self.paid_status,
            'promocode'      : self.promocode,
            'amount'      : self.amount,
            'gst_number'  : self.gst_number,
            'created_on'  : self.created_on,
    }

class OfferList(Base):
    __tablename__ = 'offer_master'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    offer_id = Column(Integer, primary_key=True)
    title = Column(String(30), nullable=False)
    restaurant_id = Column(Integer, nullable=False)
    is_active = Column(Integer, nullable=False)
    st_dt = Column(Date ,default=datetime.datetime.now)
    en_dt = Column(Date ,default=datetime.datetime.now)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'offer_id': self.offer_id,
            'title' : self.title,
            'restaurant_id' : self.restaurant_id,
            'is_active'  : self.is_active,
            'st_dt'  : self.st_dt,
            'en_dt'  : self.en_dt,
    }

#engine = create_engine('sqlite :///cba.db')

#engine = create_engine('mysql://root@127.0.0.1:3306/cba')      
engine = create_engine('mysql://DineOutStg:Dine0utStg@35.154.78.220/shokuji_tc')      

Base.metadata.create_all(engine)
