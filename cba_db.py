import os
import sys
import datetime 
from sqlalchemy import Column,ForeignKey,Integer,String,Date,Float,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Territory(Base):
    __tablename__ = 'territory'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    code = Column(String(50), nullable=False, primary_key=True)
    name = Column(String(80), nullable=False)
    language = Column(String(20) , nullable=True)
    source_language = Column(String(20) , nullable=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {

            'code': self.code,
            'name': self.name,
            'language' : self.language,
            'source_language' : self.source_language

        }


class Location(Base):
    __tablename__ = 'location'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    city = Column(String(80), nullable=True)
    street = Column(String(80), nullable=True)
    state_province = Column(String(80), nullable=True)
    zip_code = Column(String(80), nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    country = Column(String(50) , ForeignKey('territory.code'))
    territory = relationship(Territory)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {

            'id': self.id,
            'city': self.city,
            'street': self.street,
            'state_province' : self.state_province,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on            

        }


class Bank(Base):
    __tablename__ = 'bank'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    code = Column(String(50), nullable=True)
    bank = Column(String(80), nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    country = Column(String(50) , ForeignKey('territory.code'))
    territory = relationship(Territory)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            
            'id': self.id,
            'code': self.code,
            'bank': self.bank,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on            

        }


class Document(Base):
    __tablename__ = 'document'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    code = Column(String(50), nullable=True)
    description = Column(String(80), nullable=True)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'code': self.code,
            'name': self.description

        }

class Chart(Base):
    __tablename__ = 'chart'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    code = Column(String(20), nullable=True)
    chart = Column(String(80), nullable=True)
    language = Column(String(20) , nullable=True)
    description = Column(String(255) , nullable=True)
    start_date = Column(Date , nullable=True)
    end_date = Column(Date , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {

            'id': self.id,
            'code' : self.code,
            'chart': self.chart,
            'language' : self.language,
            'description' : self.description,
            'start_date' : self.start_date,
            'end_date' : self.end_date,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on

        }

class ChartAccount(Base):
    __tablename__ = 'chart_account'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    code = Column(String(250), nullable=False)
    account = Column(String(250), nullable=False)
    type = Column(String(80), nullable=False)
    posting = Column(Boolean, nullable=False)
    budgeting = Column(Boolean, nullable=False)
    status = Column(Boolean, nullable=False)
    level = Column(Integer, nullable=False)
    start_date = Column(Date , nullable=True)
    end_date = Column(Date , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    chart_id = Column(Integer , ForeignKey('chart.id'))
    chart = relationship(Chart) 

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {

            'id': self.id,
            'code': self.code,
            'account': self.account,
            'type' : self.type,
            'posting' : self.posting,
            'budgeting' : self.budgeting,
            'status' : self.status,
            'level' : self.level,
            'start_date' : self.start_date,
            'end_date' : self.end_date,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on
            
        }

class Currency(Base):
    __tablename__ = 'currency'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    code = Column(String(20), nullable=False)
    currency = Column(String(80), nullable=False)
    status = Column(Boolean, nullable=False)
    start_date = Column(Date , nullable=True)
    end_date = Column(Date , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    territory_id = Column(String(50) , nullable=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {

            'id': self.id,
            'currency': self.currency,
            'status' : self.status,
            'start_date' : self.start_date,
            'end_date' : self.end_date,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on
        }

class LegalEntity(Base):
    __tablename__ = 'legal_entity'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    code = Column(String(20), nullable=False)
    entity = Column(String(80), nullable=False)
    national_id = Column(String(80), nullable=True)
    fiscal_id = Column(String(80), nullable=True)
    entity_status = Column(Boolean, nullable=False)
    start_date = Column(Date , nullable=True)
    end_date = Column(Date , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    chart_id = Column(Integer , ForeignKey('chart.id') )
    chart = relationship(Chart)
    headquarter = Column(Integer , ForeignKey('location.id') )
    location = relationship(Location)     
    currency_id = Column(Integer , ForeignKey('currency.id') )
    currency = relationship(Currency) 

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {

            'id': self.id,
            'code' : self.code,
            'entity': self.entity,
            'national_id' : self.national_id,
            'fiscal_id' : self.fiscal_id,
            'status' : self.status,
            'start_date' : self.start_date,
            'end_date' : self.end_date,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on
        }

class Calendar(Base):
    __tablename__ = 'calendar'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    calendar = Column(String(80), nullable=False)
    status = Column(Boolean, nullable=False)
    year = Column(String(20) , nullable=False)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {

            'id': self.id,
            'calendar': self.calendar,
            'status' : self.status,
            'start_date' : self.start_date,
            'end_date' : self.end_date,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on
        }

class CalendarPeriod(Base):
    __tablename__ = 'calendar_period'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    period = Column(String(80), nullable=False)
    period_start = Column(Date , nullable=False)
    period_end = Column(Date , nullable=False)
    status = Column(String(20) , nullable=False)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    calendar_id = Column(Integer , ForeignKey('calendar.id'))
    calendar = relationship(Calendar) 

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'period': self.period,
            'period_start' : self.period_start,
            'period_end' : self.period_end,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on

        }

class Tax(Base):
    __tablename__ = 'tax'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    code = Column(String(20), nullable=False)
    tax = Column(String(80), nullable=False)
    status = Column(Boolean, nullable=False)
    rate = Column(Float , nullable=False)
    start_date = Column(Date , nullable=True)
    end_date = Column(Date , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    territory_id = Column(String(50) , nullable=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            
            'id': self.id,
            'code': self.code,
            'tax': self.tax,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on

        }

class Journal(Base):
    __tablename__ = 'journal'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    memo = Column(String(80), nullable=False)
    source = Column(String(20) , nullable=False)
    status = Column(String(20) , nullable=False)
    actual = Column(String(20) , nullable=False)
    balanced = Column(Boolean , nullable=True)
    total_debit = Column(Float , nullable=True)
    total_credit = Column(Float , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    currency_id = Column(Integer , ForeignKey('currency.id'))
    currency = relationship(Currency) 
    entity_id = Column(Integer , ForeignKey('legal_entity.id'))
    entity = relationship(LegalEntity)
    period_id = Column(Integer , ForeignKey('calendar_period.id'))
    period = relationship(CalendarPeriod)  


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'memo' : self.memo,
            'source' : self.source,
            'status' : self.status,
            'actual' : self.actual,
            'balanced' : self.actual,
            'total_debit' : self.total_debit,
            'total_credit' : self.total_credit,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on 

        }

class JournalDetails(Base):
    __tablename__ = 'journal_details'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    amount = Column(Integer, nullable=False)
    debit_credit = Column(String(40), nullable=False)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    journal_id = Column(Integer , ForeignKey('journal.id'))
    journal = relationship(Journal) 
    account_id = Column(Integer , ForeignKey('chart_account.id'))
    account = relationship(ChartAccount)
    tax_id = Column(Integer , ForeignKey('tax.id')) 
    tax = relationship(Tax)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'montant': self.montant,
            'debit_credit' : self.debit_credit,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on

        }


class Budget(Base):
    __tablename__ = 'budget'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    budget = Column(String(80), nullable=False)
    description = Column(String(255) , nullable=True)
    status = Column(String(20) , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    calendar_id = Column(Integer , ForeignKey('calendar.id'))
    calendar = relationship(Calendar) 
    entity_id = Column(Integer , ForeignKey('legal_entity.id'))
    entity = relationship(LegalEntity)
 

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'budget' : self.budget,
            'description' : self.description,
            'status' : self.status,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on

        }

class BudgetDetails(Base):
    __tablename__ = 'budget_details'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    amount = Column(Integer, nullable=False)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    budget_id = Column(Integer , ForeignKey('budget.id'))
    budget = relationship(Budget) 
    account_id = Column(Integer , ForeignKey('chart_account.id'))
    account = relationship(ChartAccount)
    period_id = Column(Integer , ForeignKey('calendar_period.id')) 
    period = relationship(CalendarPeriod)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'amount': self.amount,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on
        }


class CurrencyRate(Base):
    __tablename__ = 'currency_rate'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    rate = Column(Float, nullable=False)
    currency_from = Column(Integer, ForeignKey('currency.id'))
    currency_to = Column(Integer , ForeignKey('currency.id'))
    start_date = Column(Date , nullable=True)
    end_date = Column(Date , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {

            'id': self.id,
            'rate': self.rate,
            'currency_from' : self.currency_from,
            'currency_to' : self.currency_to,
            'start_date' : self.start_date,
            'end_date' : self.end_date,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on
        }


class ItemCategory(Base):
    __tablename__ = 'item_category'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    category = Column(String(80), nullable=False)
    description = Column(String(255) , nullable=True)
    status = Column(String(20) , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    entity_id = Column(Integer , ForeignKey('legal_entity.id'))
    entity = relationship(LegalEntity)
 

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'item_category' : self.category,
            'description' : self.description,
            'status' : self.status,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on

        }

class Item(Base):
    __tablename__ = 'item'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    code = Column(String(50), nullable=True)
    item = Column(String(80), nullable=True)
    description = Column(String(255), nullable=True)
    list_price = Column(Float, nullable=True)
    size = Column(String(5), nullable=True)
    size_measure = Column(String(3), nullable=True)
    weight = Column(String(3), nullable=True)
    item_class = Column(String(3), nullable=True)
    status = Column(Boolean, nullable=True)
    start_date = Column(Date , nullable=True)
    end_date = Column(Date , nullable=True)
    discontinued_date = Column(Date , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    category_id = Column(Integer , ForeignKey('item_category.id'))
    item_category = relationship(ItemCategory)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {

            'id': self.id,
            'code': self.code,
            'item' : self.item,
            'description' : self.description,
            'list_price' : self.list_price,
            'size' : self.size,
            'size_measure' : self.size_measure,
            'weight' : self.weight,
            'item_class' : self.item_class,
            'status' : self.status,
            'start_date' : self.start_date,
            'end_date' : self.end_date,
            'discontinued_date' : self.discontinued_date,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on
        }

class BusinessPartner(Base):
    __tablename__ = 'business_partner'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    code = Column(String(50), nullable=True)
    business_partner = Column(String(80), nullable=False)
    type = Column(String(20) , nullable=True)
    status = Column(String(20) , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    entity_id = Column(Integer , ForeignKey('legal_entity.id'))
    entity = relationship(LegalEntity)
 

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'code' : self.code,
            'business_partner' : self.business_partner,
            'type' : self.type,
            'status' : self.status,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on

        }


class RequestForQuote(Base):
    __tablename__ = 'rfq'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    document_id = Column(String(50) , nullable=True)
    document_date = Column(Date , nullable=True)
    status = Column(String(20) , nullable=True)
    memo = Column(String(255), nullable=True)
    total_gross = Column(Float , nullable=True)
    total_discount = Column(Float , nullable=True)
    total_tax = Column(Float , nullable=True)
    total_net = Column(Float , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    currency_id = Column(Integer , ForeignKey('currency.id'))
    currency = relationship(Currency) 
    entity_id = Column(Integer , ForeignKey('legal_entity.id'))
    entity = relationship(LegalEntity)
    period_id = Column(Integer , ForeignKey('calendar_period.id'))
    period = relationship(CalendarPeriod)
    business_partner_id = Column(Integer , ForeignKey('business_partner.id'))
    business_partner = relationship(BusinessPartner)  


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'document_id' : self.document_id,
            'document_date' : self.document_date,
            'status' : self.status,
            'memo' : self.memo,
            'total_gross' : self.total_gross,
            'total_discount' : self.total_discount,
            'total_tax' : self.total_tax,
            'total_net' : self.total_net,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on 

        }



class RequestForQuoteDetails(Base):
    __tablename__ = 'rfq_details'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=True)
    quantity = Column(Integer, nullable=True)
    total_gross = Column(Float , nullable=True)
    total_discount = Column(Float , nullable=True)
    total_tax = Column(Float , nullable=True)
    total_net = Column(Float , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    rfq_id = Column(Integer , ForeignKey('rfq.id'))
    rfq = relationship(RequestForQuote) 
    item_id = Column(Integer , ForeignKey('item.id'))
    item = relationship(Item)
    tax_id = Column(Integer , ForeignKey('tax.id')) 
    tax = relationship(Tax)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'price': self.price,
            'quantity' : self.quantity,
            'total_gross' : self.total_gross,
            'total_discount' : self.total_discount,
            'total_tax' : self.total_tax,
            'total_net' : self.total_net,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on

        }


class PurchaseOrder(Base):
    __tablename__ = 'purchase_order'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    document_id = Column(String(50) , nullable=True)
    document_date = Column(Date , nullable=True)
    document_status = Column(String(20) , nullable=True)
    document_origin_id = Column(Integer , nullable=True)
    document_origin = Column(String(20) , nullable=True)
    memo = Column(String(255), nullable=True)
    total_gross = Column(Float , nullable=True)
    total_discount = Column(Float , nullable=True)
    total_tax = Column(Float , nullable=True)
    total_net = Column(Float , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    currency_id = Column(Integer , ForeignKey('currency.id'))
    currency = relationship(Currency) 
    entity_id = Column(Integer , ForeignKey('legal_entity.id'))
    entity = relationship(LegalEntity)
    period_id = Column(Integer , ForeignKey('calendar_period.id'))
    period = relationship(CalendarPeriod)
    business_partner_id = Column(Integer , ForeignKey('business_partner.id'))
    business_partner = relationship(BusinessPartner)
    document_type_id = Column(Integer , ForeignKey('document.id'))
    document = relationship(Document)    


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'document_id' : self.document_id,
            'document_date' : self.document_date,
            'document_status' : self.document_status,
            'memo' : self.memo,
            'total_gross' : self.total_gross,
            'total_discount' : self.total_discount,
            'total_tax' : self.total_tax,
            'total_net' : self.total_net,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on 

        }


class PurchaseOrderDetails(Base):
    __tablename__ = 'purchase_order_details'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=True)
    quantity = Column(Integer, nullable=True)
    total_gross = Column(Float , nullable=True)
    total_discount = Column(Float , nullable=True)
    total_tax = Column(Float , nullable=True)
    total_net = Column(Float , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    purchase_order_id = Column(Integer , ForeignKey('purchase_order.id'))
    purchase_order = relationship(PurchaseOrder) 
    item_id = Column(Integer , ForeignKey('item.id'))
    item = relationship(Item)
    tax_id = Column(Integer , ForeignKey('tax.id')) 
    tax = relationship(Tax)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'price': self.price,
            'quantity' : self.quantity,
            'total_gross' : self.total_gross,
            'total_discount' : self.total_discount,
            'total_tax' : self.total_tax,
            'total_net' : self.total_net,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on

        }


class GoodsReceipt(Base):
    __tablename__ = 'goods_receipt'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    document_id = Column(String(50) , nullable=True)
    document_date = Column(Date , nullable=True)
    document_status = Column(String(20) , nullable=True)
    document_origin_id = Column(Integer , nullable=True)
    document_origin = Column(String(20) , nullable=True)
    memo = Column(String(255), nullable=True)
    total_gross = Column(Float , nullable=True)
    total_discount = Column(Float , nullable=True)
    total_tax = Column(Float , nullable=True)
    total_net = Column(Float , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    currency_id = Column(Integer , ForeignKey('currency.id'))
    currency = relationship(Currency) 
    entity_id = Column(Integer , ForeignKey('legal_entity.id'))
    entity = relationship(LegalEntity)
    period_id = Column(Integer , ForeignKey('calendar_period.id'))
    period = relationship(CalendarPeriod)
    business_partner_id = Column(Integer , ForeignKey('business_partner.id'))
    business_partner = relationship(BusinessPartner)
    document_type_id = Column(Integer , ForeignKey('document.id'))
    document = relationship(Document)    


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'document_id' : self.document_id,
            'document_date' : self.document_date,
            'document_status' : self.document_status,
            'memo' : self.memo,
            'total_gross' : self.total_gross,
            'total_discount' : self.total_discount,
            'total_tax' : self.total_tax,
            'total_net' : self.total_net,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on 

        }


class GoodsReceiptDetails(Base):
    __tablename__ = 'goods_receipt_details'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=True)
    quantity = Column(Integer, nullable=True)
    total_gross = Column(Float , nullable=True)
    total_discount = Column(Float , nullable=True)
    total_tax = Column(Float , nullable=True)
    total_net = Column(Float , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    warehouse_id = Column(Integer , ForeignKey('location.id')) 
    location = relationship(Location)
    goods_receipt_id = Column(Integer , ForeignKey('goods_receipt.id'))
    goods_receipt = relationship(GoodsReceipt) 
    item_id = Column(Integer , ForeignKey('item.id'))
    item = relationship(Item)
    tax_id = Column(Integer , ForeignKey('tax.id')) 
    tax = relationship(Tax)

    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'price': self.price,
            'quantity' : self.quantity,
            'total_gross' : self.total_gross,
            'total_discount' : self.total_discount,
            'total_tax' : self.total_tax,
            'total_net' : self.total_net,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on

        }


class Bill(Base):
    __tablename__ = 'bill'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    document_id = Column(String(50) , nullable=True)
    document_date = Column(Date , nullable=True)
    due_date = Column(Date , nullable=True)
    document_status = Column(String(20) , nullable=True)
    document_origin_id = Column(Integer , nullable=True)
    document_origin = Column(String(20) , nullable=True)
    memo = Column(String(255), nullable=True)
    total_gross = Column(Float , nullable=True)
    total_discount = Column(Float , nullable=True)
    total_tax = Column(Float , nullable=True)
    total_net = Column(Float , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    currency_id = Column(Integer , ForeignKey('currency.id'))
    currency = relationship(Currency) 
    entity_id = Column(Integer , ForeignKey('legal_entity.id'))
    entity = relationship(LegalEntity)
    period_id = Column(Integer , ForeignKey('calendar_period.id'))
    period = relationship(CalendarPeriod)
    business_partner_id = Column(Integer , ForeignKey('business_partner.id'))
    business_partner = relationship(BusinessPartner)
    document_type_id = Column(Integer , ForeignKey('document.id'))
    document = relationship(Document)    


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'document_id' : self.document_id,
            'document_date' : self.document_date,
            'document_status' : self.document_status,
            'memo' : self.memo,
            'total_gross' : self.total_gross,
            'total_discount' : self.total_discount,
            'total_tax' : self.total_tax,
            'total_net' : self.total_net,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on 

        }


class BillDetails(Base):
    __tablename__ = 'bill_details'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=True)
    quantity = Column(Integer, nullable=True)
    total_gross = Column(Float , nullable=True)
    total_discount = Column(Float , nullable=True)
    total_tax = Column(Float , nullable=True)
    total_net = Column(Float , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    bill_id = Column(Integer , ForeignKey('bill.id'))
    bill = relationship(Bill) 
    item_id = Column(Integer , ForeignKey('item.id'))
    item = relationship(Item)
    tax_id = Column(Integer , ForeignKey('tax.id')) 
    tax = relationship(Tax)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'price': self.price,
            'quantity' : self.quantity,
            'total_gross' : self.total_gross,
            'total_discount' : self.total_discount,
            'total_tax' : self.total_tax,
            'total_net' : self.total_net,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on

        }


class Quote(Base):
    __tablename__ = 'quote'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    document_id = Column(String(50) , nullable=True)
    document_date = Column(Date , nullable=True)
    document_status = Column(String(20) , nullable=True)
    memo = Column(String(255), nullable=True)
    total_gross = Column(Float , nullable=True)
    total_discount = Column(Float , nullable=True)
    total_tax = Column(Float , nullable=True)
    total_net = Column(Float , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    currency_id = Column(Integer , ForeignKey('currency.id'))
    currency = relationship(Currency) 
    entity_id = Column(Integer , ForeignKey('legal_entity.id'))
    entity = relationship(LegalEntity)
    period_id = Column(Integer , ForeignKey('calendar_period.id'))
    period = relationship(CalendarPeriod)
    business_partner_id = Column(Integer , ForeignKey('business_partner.id'))
    business_partner = relationship(BusinessPartner)
    document_type_id = Column(Integer , ForeignKey('document.id'))
    document = relationship(Document)    


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'document_id' : self.document_id,
            'document_date' : self.document_date,
            'document_status' : self.document_status,
            'memo' : self.memo,
            'total_gross' : self.total_gross,
            'total_discount' : self.total_discount,
            'total_tax' : self.total_tax,
            'total_net' : self.total_net,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on 

        }


class QuoteDetails(Base):
    __tablename__ = 'quote_details'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=True)
    quantity = Column(Integer, nullable=True)
    total_gross = Column(Float , nullable=True)
    total_discount = Column(Float , nullable=True)
    total_tax = Column(Float , nullable=True)
    total_net = Column(Float , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    quote_id = Column(Integer , ForeignKey('quote.id'))
    quote = relationship(Quote) 
    item_id = Column(Integer , ForeignKey('item.id'))
    item = relationship(Item)
    tax_id = Column(Integer , ForeignKey('tax.id')) 
    tax = relationship(Tax)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'price': self.price,
            'quantity' : self.quantity,
            'total_gross' : self.total_gross,
            'total_discount' : self.total_discount,
            'total_tax' : self.total_tax,
            'total_net' : self.total_net,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on

        }


class SaleOrder(Base):
    __tablename__ = 'sale_order'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    document_id = Column(String(50) , nullable=True)
    document_date = Column(Date , nullable=True)
    document_status = Column(String(20) , nullable=True)
    document_origin_id = Column(Integer , nullable=True)
    document_origin = Column(String(20) , nullable=True)
    memo = Column(String(255), nullable=True)
    total_gross = Column(Float , nullable=True)
    total_discount = Column(Float , nullable=True)
    total_tax = Column(Float , nullable=True)
    total_net = Column(Float , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    currency_id = Column(Integer , ForeignKey('currency.id'))
    currency = relationship(Currency) 
    entity_id = Column(Integer , ForeignKey('legal_entity.id'))
    entity = relationship(LegalEntity)
    period_id = Column(Integer , ForeignKey('calendar_period.id'))
    period = relationship(CalendarPeriod)
    business_partner_id = Column(Integer , ForeignKey('business_partner.id'))
    business_partner = relationship(BusinessPartner)
    document_type_id = Column(Integer , ForeignKey('document.id'))
    document = relationship(Document)    


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'document_id' : self.document_id,
            'document_date' : self.document_date,
            'document_status' : self.document_status,
            'memo' : self.memo,
            'total_gross' : self.total_gross,
            'total_discount' : self.total_discount,
            'total_tax' : self.total_tax,
            'total_net' : self.total_net,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on 

        }


class SaleOrderDetails(Base):
    __tablename__ = 'sale_order_details'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=True)
    quantity = Column(Integer, nullable=True)
    total_gross = Column(Float , nullable=True)
    total_discount = Column(Float , nullable=True)
    total_tax = Column(Float , nullable=True)
    total_net = Column(Float , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    sale_order_id = Column(Integer , ForeignKey('sale_order.id'))
    sale_order = relationship(SaleOrder) 
    item_id = Column(Integer , ForeignKey('item.id'))
    item = relationship(Item)
    tax_id = Column(Integer , ForeignKey('tax.id')) 
    tax = relationship(Tax)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'price': self.price,
            'quantity' : self.quantity,
            'total_gross' : self.total_gross,
            'total_discount' : self.total_discount,
            'total_tax' : self.total_tax,
            'total_net' : self.total_net,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on

        }


class Shipping(Base):
    __tablename__ = 'shipping'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    document_id = Column(String(50) , nullable=True)
    document_date = Column(Date , nullable=True)
    document_status = Column(String(20) , nullable=True)
    document_origin_id = Column(Integer , nullable=True)
    document_origin = Column(String(20) , nullable=True)
    memo = Column(String(255), nullable=True)
    total_gross = Column(Float , nullable=True)
    total_discount = Column(Float , nullable=True)
    total_tax = Column(Float , nullable=True)
    total_net = Column(Float , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    currency_id = Column(Integer , ForeignKey('currency.id'))
    currency = relationship(Currency) 
    entity_id = Column(Integer , ForeignKey('legal_entity.id'))
    entity = relationship(LegalEntity)
    period_id = Column(Integer , ForeignKey('calendar_period.id'))
    period = relationship(CalendarPeriod)
    business_partner_id = Column(Integer , ForeignKey('business_partner.id'))
    business_partner = relationship(BusinessPartner)
    document_type_id = Column(Integer , ForeignKey('document.id'))
    document = relationship(Document)   


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'document_id' : self.document_id,
            'document_date' : self.document_date,
            'document_status' : self.document_status,
            'memo' : self.memo,
            'total_gross' : self.total_gross,
            'total_discount' : self.total_discount,
            'total_tax' : self.total_tax,
            'total_net' : self.total_net,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on 

        }


class ShippingDetails(Base):
    __tablename__ = 'shipping_details'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=True)
    quantity = Column(Integer, nullable=True)
    total_gross = Column(Float , nullable=True)
    total_discount = Column(Float , nullable=True)
    total_tax = Column(Float , nullable=True)
    total_net = Column(Float , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    shipping_id = Column(Integer , ForeignKey('shipping.id'))
    shipping = relationship(Shipping) 
    item_id = Column(Integer , ForeignKey('item.id'))
    item = relationship(Item)
    tax_id = Column(Integer , ForeignKey('tax.id')) 
    tax = relationship(Tax)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'price': self.price,
            'quantity' : self.quantity,
            'total_gross' : self.total_gross,
            'total_discount' : self.total_discount,
            'total_tax' : self.total_tax,
            'total_net' : self.total_net,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on

        }


class Invoice(Base):
    __tablename__ = 'invoice'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    document_id = Column(String(50) , nullable=True)
    document_date = Column(Date , nullable=True)
    document_status = Column(String(20) , nullable=True)
    document_origin_id = Column(Integer , nullable=True)
    document_origin = Column(String(20) , nullable=True)
    memo = Column(String(255), nullable=True)
    total_gross = Column(Float , nullable=True)
    total_discount = Column(Float , nullable=True)
    total_tax = Column(Float , nullable=True)
    total_net = Column(Float , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    currency_id = Column(Integer , ForeignKey('currency.id'))
    currency = relationship(Currency) 
    entity_id = Column(Integer , ForeignKey('legal_entity.id'))
    entity = relationship(LegalEntity)
    period_id = Column(Integer , ForeignKey('calendar_period.id'))
    period = relationship(CalendarPeriod)
    business_partner_id = Column(Integer , ForeignKey('business_partner.id'))
    business_partner = relationship(BusinessPartner)
    document_type_id = Column(Integer , ForeignKey('document.id'))
    document = relationship(Document)    


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'document_id' : self.document_id,
            'document_date' : self.document_date,
            'document_status' : self.document_status,
            'memo' : self.memo,
            'total_gross' : self.total_gross,
            'total_discount' : self.total_discount,
            'total_tax' : self.total_tax,
            'total_net' : self.total_net,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on 

        }


class InvoiceDetails(Base):
    __tablename__ = 'invoice_details'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=True)
    quantity = Column(Integer, nullable=True)
    total_gross = Column(Float , nullable=True)
    total_discount = Column(Float , nullable=True)
    total_tax = Column(Float , nullable=True)
    total_net = Column(Float , nullable=True)
    created_by = Column(String(80), nullable=False)
    updated_by =  Column(String(80), nullable=True)
    created_on = Column(Date ,default=datetime.datetime.now)
    updated_on = Column(Date , onupdate=datetime.datetime.now)
    invoice_id = Column(Integer , ForeignKey('invoice.id'))
    invoice = relationship(Invoice) 
    item_id = Column(Integer , ForeignKey('item.id'))
    item = relationship(Item)
    tax_id = Column(Integer , ForeignKey('tax.id')) 
    tax = relationship(Tax)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'price': self.price,
            'quantity' : self.quantity,
            'total_gross' : self.total_gross,
            'total_discount' : self.total_discount,
            'total_tax' : self.total_tax,
            'total_net' : self.total_net,
            'created_by' : self.created_by,
            'updated_by' : self.updated_by,
            'created_on' : self.created_on,
            'updated_on' : self.updated_on

        }

#engine = create_engine('sqlite:///cba.db')

engine = create_engine('mysql://root@127.0.0.1:3306/cba')

Base.metadata.create_all(engine)
