import datetime
import sys 
from flask import Flask, session, render_template, request, redirect, jsonify, url_for, flash,g
from flask.ext.babel import Babel , gettext
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from cba_db import (Chart,ChartAccount,Calendar,CalendarPeriod,Territory,Tax,Bank,
Currency,CurrencyRate,LegalEntity,Journal,JournalDetails,Budget,BudgetDetails,Location,
ItemCategory,BusinessPartner,RequestForQuote,RequestForQuoteDetails,Item,
PurchaseOrder,PurchaseOrderDetails,GoodsReceipt,GoodsReceiptDetails,Bill,BillDetails,Quote,
QuoteDetails,SaleOrder,SaleOrderDetails,Shipping,ShippingDetails,Invoice,InvoiceDetails)
app = Flask(__name__)
#app.config.from_pyfile('cba_babel.cfg')
babel = Babel(app , default_locale='en', default_timezone='UTC', date_formats=None, configure_jinja=True)

Base = declarative_base()

#engine = create_engine('sqlite:///cba.db')
engine = create_engine('mysql://root@127.0.0.1:3306/cba')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
db_session = DBSession()

#reload(sys)
#sys.setdefaultencoding('iso-8859-1')

# add to you main app code
@babel.localeselector
def get_locale():
    return g.get('lang_code', app.config['BABEL_DEFAULT_LOCALE'])

#Users Functions

#Login function
@app.route('/' , methods=['GET', 'POST'])
@app.route('/login' , methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    if request.form['login']:
       session['login'] = request.form['login']
       return redirect(url_for('home'))
  else:
     return render_template('loginForm.html', session=session)

#Logout function
@app.route('/logout')
def logout():
    # Clear the db_session
    session.pop('login', None)
    # Redirect the user to the login page
    return redirect(url_for('login'))

#Users home page
@app.route('/home')
def home():
    return render_template('home.html')



#Locations

#Display all locations
@app.route('/adminstration/structure/common/locations')
def displayLocations():
    locations = db_session.query(Location).all()
    return render_template('locations.html' , locations=locations)

#Add new location
@app.route('/adminstration/structure/common/location/new/', methods=['GET', 'POST'])
def newLocation():
    countries = db_session.query(Territory).all()
    if request.method == 'POST':
        newLocation = Location(city=request.form['city'],
            street=request.form['street'],
            state_province=request.form['state_province'],
            zip_code=request.form['zip_code'],
            country=request.form['country'],
            created_by=session['login'])
        db_session.add(newLocation)
        db_session.commit()
        flash(gettext("new location added with success"))
        return redirect(url_for('displayLocations'))
    else:
        return render_template('newLocation.html' , countries=countries)

#Edit location
@app.route('/adminstration/structure/common/location/<int:location_id>/edit/', 
    methods=['GET', 'POST'])
def editLocation(location_id):
    countries = db_session.query(Territory).all()
    modifiedLocation = db_session.query(
        Location).filter_by(id=location_id).one()
    if request.method == 'POST':
        if request.form['city']:
            modifiedLocation.city = request.form['city']
        if request.form['street']:
            modifiedLocation.street = request.form['street']
        if request.form['state_province']:
            modifiedLocation.state_province = request.form['state_province']
        if request.form['country']:
            modifiedLocation.country = request.form['country']
        modifiedLocation.updated_by=session['login']
        db_session.add(modifiedLocation)
        db_session.commit()
        flash(gettext("location modified with success"))
        return redirect(url_for('displayLocations'))
    else:
        return render_template('editLocation.html', location=modifiedLocation , countries=countries)

#Delete a location
@app.route('/adminstration/structure/common/location/<int:location_id>/delete/', 
    methods=['GET', 'POST'])
def deleteLocation(location_id):
    locationToDelete = db_session.query(Location).filter_by(id=location_id).one()
    if request.method == 'POST':
        db_session.delete(locationToDelete)
        db_session.commit()
        flash("location deleted with succes")
        return redirect(url_for('displayLocations'))
    else:
        return render_template('deleteLocation.html', location=locationToDelete)


#Banks

#Display all banks
@app.route('/financial/accounting/structure/banks')
def displayBanks():
    banks = db_session.query(Bank).all()
    return render_template('banks.html' , banks=banks)

#Add new bank
@app.route('/financial/accounting/structure/bank/new/', methods=['GET', 'POST'])
def newBank():
    countries = db_session.query(Territory).all()
    if request.method == 'POST':
        newBank = Bank(code=request.form['code'] ,
            bank=request.form['bank'],
            country=request.form['country'], 
            created_by=session['login'])
        db_session.add(newBank)
        db_session.commit()
        flash(gettext("bank added with success"))
        return redirect(url_for('displayBanks'))
    else:
        return render_template('newBank.html' , countries=countries)

#Edit bank
@app.route('/financial/accounting/structure/bank/<int:bank_id>/edit/', methods=['GET', 'POST'])
def editBank(bank_id):
    editedBank = db_session.query(Bank).filter_by(id=bank_id).one()
    countries = db_session.query(Territory).all()
    if request.method == 'POST':
        if request.form['code']:
            editedBank.code = request.form['code']
        if request.form['bank']:
            editedBank.bank = request.form['bank']
        if request.form['country']:
            editedBank.country = request.form['country']
        editedBank.updated_by = session['login'] 
        db_session.add(editedBank)
        db_session.commit()
        flash(gettext("bank modified with success"))
        return redirect(url_for('displayBanks'))
    else:
        return render_template('editBank.html', bank=editedBank, countries=countries)

#Delete a bank
@app.route('/financial/accounting/structure/bank/<int:bank_id>/delete/', methods=['GET', 'POST'])
def deleteBank(bank_id):
    bankToDelete = db_session.query(Bank).filter_by(id=bank_id).one()
    if request.method == 'POST':
        db_session.delete(bankToDelete)
        db_session.commit()
        flash(gettext("bank deleted with succes"))
        return redirect(url_for('displayBanks'))
    else:
        return render_template('deleteBank.html', bank=bankToDelete)


#Charts of accounts

#Display charts of accounts
@app.route('/financial/accounting/structure/charts')
def displayChartsOfAccounts():
    charts = db_session.query(Chart).all()
    return render_template('chartOfAccounts.html' , charts=charts)

#Create a new chart of accounts
@app.route('/financial/accounting/structure/chart/new/', methods=['GET', 'POST'])
def newChartOfAccounts():
    if request.method == 'POST':
        newChartOfAccounts = Chart(code=request.form['code'], 
            chart=request.form['chart'],
            language='EN',
            description=request.form['description'],
            start_date=datetime.datetime.now,
            end_date=datetime.datetime.now,
            created_by=session['login'])
        db_session.add(newChartOfAccounts)
        db_session.commit()
        flash(gettext("charts of accounts created with success"))
        return redirect(url_for('displayChartsOfAccounts'))
    else:
        return render_template('newChartOfAccounts.html')

#Edit chart of accounts
@app.route('/financial/accounting/structure/chart/<int:chart_id>/edit/', methods=['GET', 'POST'])
def editChartOfAccounts(chart_id):
    editedChartOfAccounts = db_session.query(
        Chart).filter_by(id=chart_id).one()
    if request.method == 'POST':
        if request.form['code']:
            editedChartOfAccounts.code = request.form['code']
        if request.form['chart']:
            editedChartOfAccounts.chart = request.form['chart']
        db_session.add(editedChartOfAccounts)
        db_session.commit()
        flash(gettext("charts of accounts modified with success"))
        return redirect(url_for('displayChartsOfAccounts'))
    else:
        return render_template('editChartOfAccounts.html', chart=editedChartOfAccounts)

#Delete chart of accounts
@app.route('/financial/accounting/structure/chart/<int:chart_id>/delete/', methods=['GET', 'POST'])
def deleteChartOfAccounts(chart_id):
    chartOfAccountsToDelete = db_session.query(
        Chart).filter_by(id=chart_id).one()
    if request.method == 'POST':
        db_session.delete(chartOfAccountsToDelete)
        db_session.commit()
        flash(gettext("charts of accounts deleted with success"))
        return redirect(url_for('displayChartsOfAccounts'))
    else:
        return render_template('deleteChartOfAccounts.html', chart=chartOfAccountsToDelete)

#Accounts

#Display accounts
@app.route('/financial/accounting/structure/chart/<int:chart_id>/accounts')
def displayAccounts(chart_id):
    chart = db_session.query(Chart).filter_by(id=chart_id).one()
    accounts = db_session.query(ChartAccount).filter_by(
        chart_id=chart_id).all()
    return render_template('accounts.html', accounts=accounts, chart=chart)

#Create a new account
@app.route(
    '/financial/accounting/structure/chart/<int:chart_id>/account/new/', methods=['GET', 'POST'])
def newAccount(chart_id):
    if request.method == 'POST':
        newAccount = ChartAccount(code=request.form['code'], 
            account=request.form['account'], 
            type=request.form['type'],
            posting=request.form['posting'], 
            budgeting=request.form['budgeting'],
            status=request.form['status'], 
            level=request.form['level'],
            created_by=session['login'],
            chart_id=chart_id)
        db_session.add(newAccount) 
        db_session.commit()
        flash(gettext("account created with success"))
        return redirect(url_for('displayAccounts', chart_id=chart_id))
    else:
        return render_template('newAccount.html', chart_id=chart_id)


#Edit an account
@app.route('/financial/accounting/structure/chart/<int:chart_id>/account/<int:account_id>/edit/', methods=['GET', 'POST'])
def editAccount(chart_id, account_id):
    editedAccount = db_session.query(ChartAccount).filter_by(id=account_id).one()
    if request.method == 'POST':
        if request.form['code']:
            editedAccount.code = request.form['code']
        if request.form['account']:
            editedAccount.account = request.form['account']
        if request.form['type']:
            editedAccount.type = request.form['type']
        if request.form['posting']:
            editedAccount.posting = request.form['posting']
        if request.form['budgeting']:
            editedAccount.budgeting = request.form['budgeting']
        if request.form['status']:
            editedAccount.status = request.form['status']
        if request.form['level']:
            editedAccount.level = request.form['level']
        editedAccount.updated_by = session['login']
        db_session.add(editedAccount)
        db_session.commit()
        flash(gettext("account modified with success"))
        return redirect(url_for('displayAccounts', chart_id=chart_id))
    else:
        return render_template(
            'editAccount.html', chart_id=chart_id, account_id=account_id, account=editedAccount)

#Delete an account
@app.route('/financial/accounting/structure/charts/<int:chart_id>/account/<int:account_id>/delete/', methods=['GET', 'POST'])
def deleteAccount(chart_id,account_id):
    accountToDelete = db_session.query(ChartAccount).filter_by(id=account_id).one()
    if request.method == 'POST':
        db_session.delete(accountToDelete)
        db_session.commit()
        flash(gettext("account deleted with success"))
        return redirect(url_for('displayAccounts', chart_id=chart_id))
    else:
        return render_template('deleteAccount.html', account=accountToDelete, chart_id=chart_id)


#Currencies

#Display currencies
@app.route('/adminstration/structure/common/currencies')
def displayCurrencies():
    currencies = db_session.query(Currency).all()
    return render_template('currencies.html' , currencies=currencies)


#Edit a currency
@app.route('/adminstration/structure/common/currency/<int:currency_id>/edit/', methods=['GET', 'POST'])
def editCurrency(currency_id):
    editedCurrency = db_session.query(
        Currency).filter_by(id=currency_id).one()
    if request.method == 'POST':
        if request.form['status']:
            editedCurrency.status = request.form['status']
        if request.form['start_date']:
            editedCurrency.start_date = request.form['start_date']
        if request.form['end_date']:
            editedCurrency.end_date = request.form['end_date']
        editedCurrency.updated_by = session['login']
        db_session.add(editedCurrency)
        db_session.commit()
        flash(gettext("currency modified with success"))
        return redirect(url_for('displayCurrencies'))
    else:
        return render_template('editCurrency.html', currency=editedCurrency)



#Legal Entities

#Display all entities
@app.route('/adminstration/structure/common/legal_entities/')
def displayLegalEntities():
    entities = db_session.query(LegalEntity).all()
    return render_template('entities.html' , entities=entities)

#Add new entity
@app.route('/adminstration/structure/common/legal_entity/new/', methods=['GET', 'POST'])
def newLegalEntity():
    charts = db_session.query(Chart).all()
    currencies = db_session.query(Currency).all()
    locations = db_session.query(Location).all()
    if request.method == 'POST':
        newLegalEntity = LegalEntity(code=request.form['code'], 
            entity=request.form['entity'], 
            entity_status=True,
            national_id=request.form['national_id'],
            fiscal_id=request.form['fiscal_id'], 
            start_date=datetime.datetime.now,
            end_date=datetime.datetime.now,  
            created_by=session['login'],
            chart_id=request.form['chart_id'],
            headquarter=request.form['location'],
            currency_id=request.form['currency_id'])
        db_session.add(newLegalEntity)
        db_session.commit()
        flash(gettext("legal entity created with success"))
        return redirect(url_for('displayLegalEntities'))
    else:
        return render_template('newLegalEntity.html' , charts=charts, currencies=currencies, locations=locations)

#Edit a legal entity
@app.route('/adminstration/structure/common/legal_entity/<int:entity_id>/edit/', methods=['GET', 'POST'])
def editLegalEntity(entity_id):
    editedLegalEntity = db_session.query(
        LegalEntity).filter_by(id=entity_id).one()
    charts = db_session.query(Chart).all()
    currencies = db_session.query(Currency).all()
    locations = db_session.query(Location).all()
    if request.method == 'POST':
        if request.form['code']:
            editedLegalEntity.code = request.form['code']
        if request.form['entity']:
            editedLegalEntity.entity = request.form['entity']
        if request.form['national_id']:
            editedLegalEntity.national_id = request.form['national_id']
        if request.form['fiscal_id']:
            editedLegalEntity.fiscal_id = request.form['fiscal_id']
        if request.form['chart_id']:
            editedLegalEntity.chart_id = request.form['chart_id']
        if request.form['location']:
            editedLegalEntity.headquarter = request.form['location']
        if request.form['currency_id']:
            editedLegalEntity.currency_id = request.form['currency_id']
        editedLegalEntity.updated_by = session['login']
        db_session.add(editedLegalEntity)
        flash(gettext("legal entity modified with success"))
        db_session.commit()
        return redirect(url_for('displayLegalEntities'))
    else:
        return render_template('editLegalEntity.html', entity=editedLegalEntity, charts=charts, currencies=currencies, locations=locations)

#Delete an entity
@app.route('/adminstration/structure/common/legal_entity/<int:entity_id>/delete/', methods=['GET', 'POST'])
def deleteLegalEntity(entity_id):
    legalEntityToDelete = db_session.query(
        LegalEntity).filter_by(id=entity_id).one()
    if request.method == 'POST':
        db_session.delete(legalEntityToDelete)
        db_session.commit()
        flash(gettext("legal entity deleted with success"))
        return redirect(url_for('displayLegalEntities'))
    else:
        return render_template('deleteLegalEntity.html', entity=legalEntityToDelete)


#Calendars

#Display calendars
@app.route('/adminstration/structure/common/calendars')
def displayCalendars():
    calendars = db_session.query(Calendar).all()
    return render_template('calendars.html' , calendars=calendars)

#Create a new calendar
@app.route('/adminstration/structure/common/calendar/new/', methods=['GET', 'POST'])
def newCalendar():
    if request.method == 'POST':
        newCalendar = Calendar(calendar=request.form['calendar'], 
            status=request.form['status'],
            year=request.form['year'],
            created_by=session['login'])
        db_session.add(newCalendar)
        db_session.commit()
        flash(gettext("calendar created with success"))
        return redirect(url_for('displayCalendars'))
    else:
        return render_template('newCalendar.html')

#Edit a calendar
@app.route('/adminstration/structure/common/calendar/<int:calendar_id>/edit/', methods=['GET', 'POST'])
def editCalendar(calendar_id):
    editedCalendar = db_session.query(
        Calendar).filter_by(id=calendar_id).one()
    if request.method == 'POST':
        if request.form['calendar']:
            editedCalendar.calendar = request.form['calendar']
        if request.form['status']:
            editedCalendar.status = request.form['status']
        if request.form['year']:
            editedCalendar.year = request.form['year']
        editedCalendar.updated_by = session['login']
        db_session.add(editedCalendar)
        db_session.commit()
        flash(gettext("calendar modified with success"))
        return redirect(url_for('displayCalendars'))
    else:
        return render_template('editCalendar.html', calendar=editedCalendar)

#Delete calendar
@app.route('/adminstration/structure/common/calendar/<int:calendar_id>/delete', methods=['GET', 'POST'])
def deleteCalendar(calendar_id):
    calendarToDelete = db_session.query(
        Calendar).filter_by(id=calendar_id).one()
    if request.method == 'POST':
        db_session.delete(calendarToDelete)
        db_session.commit()
        flash(gettext("calendar deleted with success"))
        return redirect(url_for('displayCalendars'))
    else:
        return render_template('deleteCalendar.html', calendar=calendarToDelete)


#Periods

#Display periods of a specific calendar
@app.route('/adminstration/structure/common/calendar/<int:calendar_id>/periods')
def displayPeriods(calendar_id):
    calendar = db_session.query(Calendar).filter_by(id=calendar_id).one()
    periods = db_session.query(CalendarPeriod).filter_by(
        calendar_id=calendar_id).all()
    return render_template('periods.html', periods=periods, calendar=calendar)

#Create a new period
@app.route(
    '/adminstration/structure/common/calendar/<int:calendar_id>/period/new/', methods=['GET', 'POST'])
def newPeriod(calendar_id):
    if request.method == 'POST':
        newPeriod = CalendarPeriod(period=request.form['period'], 
            period_start=request.form['period_start'], 
            period_end=request.form['period_end'],
            status='C', 
            created_by=session['login'], 
            calendar_id=calendar_id)
        db_session.add(newPeriod) 
        db_session.commit()
        flash(gettext("period created with success"))
        return redirect(url_for('displayPeriods', calendar_id=calendar_id))
    else:
        return render_template('newPeriod.html', calendar_id=calendar_id)


#Edit a period
@app.route('/adminstration/structure/common/calendar/<int:calendar_id>/period/<int:period_id>/edit/', methods=['GET', 'POST'])
def editPeriod(calendar_id, period_id):
    editedPeriod = db_session.query(CalendarPeriod).filter_by(id=period_id).one()
    if request.method == 'POST':
        if request.form['period']:
            editedPeriod.period = request.form['period']
        if request.form['period_start']:
            editedPeriod.period_start = request.form['period_start']
        if request.form['period_end']:
            editedPeriod.period_end = request.form['period_end']
        if request.form['status']:
            editedPeriod.status = request.form['status']
        editedPeriod.updated_by = session['login']
        db_session.add(editedPeriod)
        db_session.commit()
        flash(gettext("period modified with success"))
        return redirect(url_for('displayPeriods', calendar_id=calendar_id))
    else:
        return render_template(
            'editPeriod.html', calendar_id=calendar_id, period_id=period_id, period=editedPeriod)

#Delete a period
@app.route('/adminstration/structure/common/calendar/<int:calendar_id>/period/<int:period_id>/delete/', methods=['GET', 'POST'])
def deletePeriod(calendar_id,period_id):
    periodToDelete = db_session.query(CalendarPeriod).filter_by(id=period_id).one()
    if request.method == 'POST':
        db_session.delete(periodToDelete)
        db_session.commit()
        flash(gettext("period deleted with success"))
        return redirect(url_for('displayPeriods', calendar_id=calendar_id))
    else:
        return render_template('deletePeriod.html', period=periodToDelete, calendar_id=calendar_id)


#Taxes

#Display taxes
@app.route('/adminstration/structure/common/taxes')
def displayTaxes():
    taxes = db_session.query(Tax).all()
    return render_template('taxes.html' , taxes=taxes)

#Create a new tax
@app.route('/adminstration/structure/common/tax/new/', methods=['GET', 'POST'])
def newTax():
    territories = db_session.query(Territory).all()
    if request.method == 'POST':        
        newTax = Tax(code=request.form['code'],
            tax=request.form['tax'],
            status=request.form['status'],
            rate=request.form['rate'],
            start_date=request.form['start_date'],
            end_date=request.form['end_date'],
            created_by=session['login'],
            territory_id=request.form['territory_id'])
        db_session.add(newTax)
        db_session.commit()
        flash(gettext("tax created with success"))
        return redirect(url_for('displayTaxes'))
    else:
        return render_template('newTax.html' , territories=territories)

#Edit a Tax
@app.route('/adminstration/structure/common/tax/<int:tax_id>/edit/', methods=['GET', 'POST'])
def editTax(tax_id):
    editedTax = db_session.query(
        Tax).filter_by(id=tax_id).one()
    territories = db_session.query(Territory).all()
    if request.method == 'POST':
        if request.form['code']:
            editedTax.code = request.form['code']
        if request.form['tax']:
            editedTax.tax = request.form['tax']
        if request.form['status']:
            editedTax.status = request.form['status']
        if request.form['rate']:
            editedTax.rate = request.form['rate']
        if request.form['start_date']:
            editedTax.start_date= request.form['start_date']
        if request.form['end_date']:
            editedTax.end_date= request.form['end_date']
        if request.form['territory_id']:
            editedTax.territory_id = request.form['territory_id']
        editedTax.updated_by = session['login']
        db_session.add(editedTax)
        db_session.commit()
        flash(gettext("tax modified with success"))
        return redirect(url_for('displayTaxes'))
    else:
        return render_template('editTax.html', tax=editedTax, territories=territories)

#Delete tax
@app.route('/adminstration/structure/common/tax/<int:tax_id>/delete/', methods=['GET', 'POST'])
def deleteTax(tax_id):
    taxToDelete = db_session.query(
        Tax).filter_by(id=tax_id).one()
    if request.method == 'POST':
        db_session.delete(taxToDelete)
        db_session.commit()
        flash(gettext("tax deleted with success"))
        return redirect(url_for('displayTaxes'))
    else:
        return render_template('deleteTax.html', tax=taxToDelete)

#Journals

#Display journals
@app.route('/financial/accounting/data/input/journals')
def displayJournals():
    journals = db_session.query(Journal).all()
    return render_template('journals.html' , journals=journals)

#Add a new journal
@app.route('/financial/accounting/data/input/journal/new/', methods=['GET', 'POST'])
def newJournal():
    entities = db_session.query(LegalEntity).all()
    periods = db_session.query(CalendarPeriod).all()
    currencies = db_session.query(Currency).all()
    if request.method == 'POST':
        newJournal = Journal(memo=request.form['memo'] , 
            source='Manual', 
            status='U',
            actual='A',
            balanced=False,
            total_debit=0.0,
            total_credit=0.0,
            created_by=session['login'],
            currency_id=request.form['currency'],
            entity_id=request.form['entity'],
            period_id=request.form['period'])
        db_session.add(newJournal)
        db_session.commit()
        flash(gettext("journal created with success"))
        return redirect(url_for('displayJournals'))
    else:
        return render_template('newJournal.html' , entities=entities , periods=periods , currencies=currencies)

#Edit a journal
@app.route('/financial/accounting/data/input/journal/<int:journal_id>/edit/', methods=['GET', 'POST'])
def editJournal(journal_id):
    editedJournal = db_session.query(
        Journal).filter_by(id=journal_id).one()
    entities = db_session.query(LegalEntity).all()
    periods = db_session.query(CalendarPeriod).all()
    currencies = db_session.query(Currency).all()
    if request.method == 'POST':
        if request.form['memo']:
            editedJournal.memo = request.form['memo']
        if request.form['currency']:
            editedJournal.currency_id = request.form['currency']
        if request.form['entity']:
            editedJournal.entity_id = request.form['entity']
        if request.form['period']:
            editedJournal.period_id = request.form['period']
        editedJournal.updated_by=session['login']
        db_session.add(editedJournal)
        db_session.commit()
        flash("journal modified with success")
        return redirect(url_for('displayJournals'))
    else:
        return render_template(
            'editJournal.html', journal=editedJournal, entities=entities , periods=periods , currencies=currencies)

#Delete a journal
@app.route('/financial/accounting/data/input/journal/<int:journal_id>/delete/', methods=['GET', 'POST'])
def deleteJournal(journal_id):
    journalToDelete = db_session.query(
        Journal).filter_by(id=journal_id).one()
    if request.method == 'POST':
        db_session.delete(journalToDelete)
        db_session.commit()
        flash("journal deleted with succes")
        return redirect(
            url_for('displayJournals'))
    else:
        return render_template(
            'deleteJournal.html', journal=journalToDelete)

#Journal details

#Display journal details
@app.route('/financial/accounting/data/input/journal/<int:journal_id>/details')
def displayJournalDetails(journal_id):
    journal = db_session.query(Journal).filter_by(id=journal_id).one()
    details = db_session.query(JournalDetails).filter_by(
        journal_id=journal_id).all()
    return render_template('journalDetails.html', details=details, journal=journal)

#Add detail to journal
@app.route(
    '/financial/accounting/data/input/journal/<int:journal_id>/details/new', methods=['GET', 'POST'])
def newJournalDetail(journal_id):
    accounts = db_session.query(ChartAccount).all()
    taxes = db_session.query(Tax).all()
    if request.method == 'POST':
        newJournalDetail = JournalDetails(amount=request.form['amount'], 
            debit_credit=request.form['debit_credit'], 
            created_by=session['login'],
            journal_id=journal_id,
            account_id=request.form['account'],
            tax_id=request.form['tax'])
        db_session.add(newJournalDetail)
        db_session.commit()
        flash("journal detail created with succes")
        return redirect(url_for('displayJournalDetails', journal_id=journal_id))
    else:
        return render_template('newJournalDetails.html', journal_id=journal_id , accounts=accounts, taxes=taxes)


#Edit journal details
@app.route(
    '/financial/accounting/data/input/journal/<int:journal_id>/details/<int:line_id>/edit', methods=['GET', 'POST'])
def editJournalDetails(journal_id, line_id):
    editedJournalDetail = db_session.query(JournalDetails).filter_by(id=line_id).one()
    accounts = db_session.query(ChartAccount).all()
    taxes = db_session.query(Tax).all()
    if request.method == 'POST':
        if request.form['amount']:
            editedJournalDetail.montant = request.form['amount']
        if request.form['debit_credit']:
            editedJournalDetail.debit_credit = request.form['debit_credit']
        if request.form['account']:
            editedJournalDetail.account_id = request.form['account']
        if request.form['tax']:
            editedJournalDetail.tax_id = request.form['tax']
        db_session.add(editedJournalDetail)
        db_session.commit()
        flash("journal detail modified with success")
        return redirect(url_for('displayJournalDetails', journal_id=journal_id))
    else:
        return render_template(
            'editJournalDetails.html', journal_id=journal_id, line_id=line_id, detail=editedJournalDetail , taxes=taxes , accounts=accounts)

#Delete journal details
@app.route('/financial/accounting/data/input/journal/<int:journal_id>/details/<int:line_id>/delete', methods=['GET', 'POST'])
def deleteJournalDetails(journal_id, line_id):
    journalDetailsToDelete = db_session.query(JournalDetails).filter_by(id=line_id).one()
    if request.method == 'POST':
        db_session.delete(journalDetailsToDelete)
        db_session.commit()
        flash("journal detail deleted with success")
        return redirect(url_for('displayJournalDetails', journal_id=journal_id))
    else:
        return render_template('deleteJournalDetails.html', detail=journalDetailsToDelete, journal_id=journal_id)



#Budgets

#Display budgets
@app.route('/financial/accounting/data/input/budgets')
def displayBudgets():
    budgets = db_session.query(Budget).all()
    return render_template('budgets.html' , budgets=budgets)

#Add a new budget
@app.route('/financial/accounting/data/input/budget/new', methods=['GET', 'POST'])
def newBudget():
    entities = db_session.query(LegalEntity).all()
    calendars = db_session.query(Calendar).all()
    if request.method == 'POST':
        newBudget = Budget(budget=request.form['budget'], 
            description=request.form['description'], 
            status='E',
            created_by=session['login'],
            calendar_id=request.form['calendar'],
            entity_id=request.form['entity'])
        db_session.add(newBudget)
        db_session.commit()
        flash("budget created with success")
        return redirect(url_for('displayBudgets'))
    else:
        return render_template('newBudget.html' , entities=entities , calendars=calendars)

#Edit a budget
@app.route('/financial/accounting/data/input/budget/<int:budget_id>/edit', methods=['GET', 'POST'])
def editBudget(budget_id):
    entities = db_session.query(LegalEntity).all()
    calendars = db_session.query(Calendar).all()
    editedBudget = db_session.query(
        Budget).filter_by(id=budget_id).one()
    if request.method == 'POST':
        if request.form['budget']:
            editedBudget.budget = request.form['budget']
        if request.form['description']:
            editedBudget.description = request.form['description']
        if request.form['calendar']:
            editedBudget.calendar_id = request.form['calendar']
        if request.form['entity']:
            editedBudget.entity_id = request.form['entity']
        editedBudget.updated_by=session['login']
        db_session.add(editedBudget)
        db_session.commit()
        flash("budget modified with success")
        return redirect(url_for('displayBudgets'))
    else:
        return render_template('editBudget.html', budget=editedBudget , entities=entities , calendars=calendars)

#Delete a budget
@app.route('/financial/accounting/data/input/budget/<int:budget_id>/delete', methods=['GET', 'POST'])
def deleteBudget(budget_id):
    budgetToDelete = db_session.query(
        Budget).filter_by(id=budget_id).one()
    if request.method == 'POST':
        db_session.delete(budgetToDelete)
        db_session.commit()
        flash("budget deleted with succes")
        return redirect(url_for('displayBudgets'))
    else:
        return render_template('deleteBudget.html', budget=budgetToDelete)


#Budget details

#Display budget details
@app.route('/financial/accounting/data/input/budget/<int:budget_id>/details')
def displayBudgetDetails(budget_id):
    budget = db_session.query(Budget).filter_by(id=budget_id).one()
    details = db_session.query(BudgetDetails).filter_by(
        budget_id=budget_id).all()
    return render_template('budgetDetails.html', details=details, budget=budget)

#Add detail to budget
@app.route(
    '/financial/accounting/data/input/budget/<int:budget_id>/details/new', methods=['GET', 'POST'])
def newBudgetDetail(budget_id):
    accounts = db_session.query(ChartAccount).all()
    periods = db_session.query(CalendarPeriod).all()
    if request.method == 'POST':
        newBudgetDetail = BudgetDetails(amount=request.form['amount'],
            created_by=session['login'],
            budget_id=budget_id,
            account_id=request.form['account'],
            period_id=request.form['period'])
        db_session.add(newBudgetDetail)
        db_session.commit()
        flash("budget detail created with succes")
        return redirect(url_for('displayBudgetDetails', budget_id=budget_id))
    else:
        return render_template('newBudgetDetails.html', budget_id=budget_id, accounts=accounts , periods=periods)


#Edit budget detail
@app.route(
    '/financial/accounting/data/input/budget/<int:budget_id>/details/<int:line_id>/edit', methods=['GET', 'POST'])
def editBudgetDetails(budget_id, line_id):
    accounts = db_session.query(ChartAccount).all()
    periods = db_session.query(CalendarPeriod).all()
    editedBudgetDetail = db_session.query(BudgetDetails).filter_by(id=line_id).one()
    if request.method == 'POST':
        if request.form['amount']:
            editedBudgetDetail.amount = request.form['amount']
        if request.form['account']:
            editedBudgetDetail.account_id = request.form['account']
        if request.form['period']:
            editedBudgetDetail.period_id = request.form['period']
        db_session.add(editedBudgetDetail)
        db_session.commit()
        flash("budget detail modified with success")
        return redirect(url_for('displayBudgetDetails', budget_id=budget_id))
    else:
        return render_template('editBudgetDetails.html', budget_id=budget_id, detail=editedBudgetDetail , accounts=accounts , periods=periods)

#Delete budget detail
@app.route('/financial/accounting/data/input/budget/<int:budget_id>/details/<int:line_id>/delete', methods=['GET', 'POST'])
def deleteBudgetDetails(budget_id, line_id):
    budgetDetailToDelete = db_session.query(BudgetDetails).filter_by(id=line_id).one()
    if request.method == 'POST':
        db_session.delete(budgetDetailsToDelete)
        db_session.commit()
        flash("budget detail deleted with success")
        return redirect(url_for('displayBudgetDetails', budget_id=budget_id))
    else:
        return render_template('deleteBudgetDetails.html', detail=budgetDetailToDelete, budget_id=budget_id)


#Rates

#Display rates
@app.route('/adminstration/structure/common/rates')
def displayRates():
    rates =db_session.query(CurrencyRate).all()
    return render_template('rates.html', rates=rates)

#Create a new rate
@app.route('/adminstration/structure/common/rate/new', methods=['GET', 'POST'])
def newRate():
    if request.method == 'POST':
        newRate = CurrencyRate(rate=request.form['rate'], 
            start_date=request.form['start_date'], 
            end_date=request.form['end_date'],
            currency_from=request.form['currency_from'],
            currency_to=request.form['currency_to'], 
            created_by=session['login'])
        db_session.add(newRate) 
        db_session.commit()
        flash("rate created with success")
        return redirect(url_for('displayRates'))
    else:
        return render_template('newRate.html')


#Edit a rate
@app.route('/adminstration/structure/common/rate/<int:rate_id>/edit',methods=['GET', 'POST'])
def editRate(rate_id):
    editedRate = db_session.query(CurrencyRate).filter_by(id=rate_id).one()
    if request.method == 'POST':
        if request.form['rate']:
            editedRate.rate = request.form['rate']
        if request.form['start_date']:
            editedRate.start_date = request.form['start_date']
        if request.form['end_date']:
            editedRate.end_date = request.form['end_date']
        if request.form['currency_from']:
            editedRate.currency_from = request.form['currency_from']
        if request.form['currency_to']:
            editedRate.currency_to = request.form['currency_to']
        editedRate.updated_by = session['login']
        db_session.add(editedRate)
        db_session.commit()
        flash("rate modified with success")
        return redirect(url_for('displayRates'))
    else:
        return render_template('editRate.html', rate=editedRate)

#Delete a rate
@app.route('/adminstration/structure/common/rate/<int:rate_id>/delete',methods=['GET', 'POST'])
def deleteRate(rate_id):
    rateToDelete = db_session.query(CurrencyRate).filter_by(id=rate_id).one()
    if request.method == 'POST':
        db_session.delete(rateToDelete)
        db_session.commit()
        flash("rate deleted with success")
        return redirect(url_for('displayRates'))
    else:
        return render_template('deleteRate.html', rate=rateToDelete)


#Items Categories

#Display items categories
@app.route('/adminstration/structure/inventory/data/input/item_category')
def displayItemCategories():
    itemCategories = db_session.query(ItemCategory).all()
    return render_template('itemsCategories.html' , item_categories=itemCategories)

#Add a new item category
@app.route('/adminstration/structure/inventory/data/input/item_category/new/', methods=['GET', 'POST'])
def newItemCategory():
    entities = db_session.query(LegalEntity).all()
    if request.method == 'POST':
        newItemCategory = ItemCategory(category=request.form['category'] , 
            description=request.form['description'], 
            status='A',
            created_by=session['login'],
            entity_id=request.form['entity'])
        db_session.add(newItemCategory)
        db_session.commit()
        flash(gettext("item category created with success"))
        return redirect(url_for('displayItemCategories'))
    else:
        return render_template('newItemCategory.html' , entities=entities)

#Edit an item category
@app.route('/adminstration/structure/inventory/data/input/item_category/<int:category_id>/edit/', methods=['GET', 'POST'])
def editItemCategory(category_id):
    editedItemCategory = db_session.query(
        ItemCategory).filter_by(id=category_id).one()
    entities = db_session.query(LegalEntity).all()
    if request.method == 'POST':
        if request.form['category']:
            editedItemCategory.category = request.form['category']
        if request.form['description']:
            editedItemCategory.description = request.form['description']
        if request.form['status']:
            editedItemCategory.status = request.form['status']
        if request.form['entity']:
            editedItemCategory.entity_id = request.form['entity']
        editedItemCategory.updated_by=session['login']
        db_session.add(editedItemCategory)
        db_session.commit()
        flash("item category modified with success")
        return redirect(url_for('displayItemCategories'))
    else:
        return render_template(
            'editItemCategory.html', item_category=editedItemCategory, entities=entities)

#Delete an item category
@app.route('/adminstration/structure/inventory/data/input/item_category/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteItemCategory(category_id):
    itemCategoryToDelete = db_session.query(
        ItemCategory).filter_by(id=category_id).one()
    if request.method == 'POST':
        db_session.delete(itemCategoryToDelete)
        db_session.commit()
        flash("item category deleted with succes")
        return redirect(
            url_for('displayItemCategories'))
    else:
        return render_template(
            'deleteItemCategory.html', category=itemCategoryToDelete)


#Items

#Display items
@app.route('/adminstration/structure/inventory/data/input/item_category/<int:category_id>/items')
def displayItems(category_id):
    category = db_session.query(ItemCategory).filter_by(id=category_id).one()
    items = db_session.query(Item).filter_by(
        category_id=category_id).all()
    return render_template('items.html', items=items, category=category)

#Create a new item
@app.route(
    '/adminstration/structure/inventory/data/input/item_category/<int:category_id>/item/new/', methods=['GET', 'POST'])
def newItem(category_id):
    if request.method == 'POST':
        newItem = Item(code=request.form['code'], 
            item=request.form['item'], 
            description=request.form['description'],
            list_price=request.form['list_price'], 
            size=request.form['size'],
            size_measure=request.form['size_measure'], 
            weight=request.form['weight'],
            item_class=request.form['item_class'],
            status=request.form['status'],
            start_date=request.form['start_date'],
            end_date=request.form['end_date'],
            discontinued_date=request.form['discontinued_date'],
            created_by=session['login'],
            category_id=category_id)
        db_session.add(newItem) 
        db_session.commit()
        flash(gettext("item created with success"))
        return redirect(url_for('displayItems', category_id=category_id))
    else:
        return render_template('newItem.html', category_id=category_id)


#Edit an item
@app.route('/adminstration/structure/inventory/data/input/item_category/<int:category_id>/item/<int:item_id>/edit/', methods=['GET', 'POST'])
def editItem(category_id, item_id):
    editedItem = db_session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        if request.form['code']:
            editedItem.code = request.form['code']
        if request.form['item']:
            editedItem.item = request.form['item']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['list_price']:
            editedItem.list_price = request.form['list_price']
        if request.form['size']:
            editedItem.size = request.form['size']
        if request.form['size_measure']:
            editedItem.size_measure = request.form['size_measure']
        if request.form['weight']:
            editedItem.weight = request.form['weight']
        if request.form['item_class']:
            editedItem.item_class = request.form['item_class']
        if request.form['start_date']:
            editedItem.start_date = request.form['start_date']
        if request.form['end_date']:
            editedItem.end_date = request.form['end_date']
        if request.form['discontinued_date']:
            editedItem.discontinued_date = request.form['discontinued_date']
        editedItem.updated_by = session['login']
        db_session.add(editedItem)
        db_session.commit()
        flash(gettext("item modified with success"))
        return redirect(url_for('displayItems', category_id=category_id))
    else:
        return render_template(
            'editItem.html', category_id=category_id, item_id=item_id, item=editedItem)

#Delete an item
@app.route('/adminstration/structure/inventory/data/input/item_category/<int:category_id>/item/<int:item_id>/delete/', methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
    itemToDelete = db_session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        db_session.delete(itemToDelete)
        db_session.commit()
        flash(gettext("item deleted with success"))
        return redirect(url_for('displayItems', category_id=category_id))
    else:
        return render_template('deleteItem.html', item=itemToDelete, category_id=category_id)


#Business partners

#Display business partners
@app.route('/adminstration/structure/common/data/input/business_partner')
def displayBusinessPartners():
    businessPartners = db_session.query(BusinessPartner).all()
    return render_template('businessPartners.html' , business_partners=businessPartners)

#Add a new business partner
@app.route('/adminstration/structure/common/data/input/business_partner/new/', methods=['GET', 'POST'])
def newBusinessPartner():
    entities = db_session.query(LegalEntity).all()
    if request.method == 'POST':
        newBusinessPartner = BusinessPartner(code=request.form['code'] , 
            business_partner=request.form['business_partner'], 
            type=request.form['type'],
            status='A',
            created_by=session['login'],
            entity_id=request.form['entity'])
        db_session.add(newBusinessPartner)
        db_session.commit()
        flash(gettext("business partner created with success"))
        return redirect(url_for('displayBusinessPartners'))
    else:
        return render_template('newBusinessPartner.html' , entities=entities)

#Edit a business partner
@app.route('/adminstration/structure/common/data/input/business_partner/<int:business_partner_id>/edit/', methods=['GET', 'POST'])
def editBusinessPartner(business_partner_id):
    editedBusinessPartner = db_session.query(
        BusinessPartner).filter_by(id=business_partner_id).one()
    entities = db_session.query(LegalEntity).all()
    if request.method == 'POST':
        if request.form['code']:
            editedBusinessPartner.code = request.form['code']
        if request.form['business_partner']:
            editedBusinessPartner.business_partner = request.form['business_partner']
        if request.form['type']:
            editedBusinessPartner.type = request.form['type']
        if request.form['status']:
            editedBusinessPartner.status = request.form['status']
        if request.form['entity']:
            editedBusinessPartner.entity_id = request.form['entity']
        editedBusinessPartner.updated_by=session['login']
        db_session.add(editedBusinessPartner)
        db_session.commit()
        flash("business partner modified with success")
        return redirect(url_for('displayBusinessPartners'))
    else:
        return render_template(
            'editBusinessPartner.html', business_partner=editedBusinessPartner, entities=entities)

#Delete a business partner
@app.route('/adminstration/structure/common/data/input/business_partner/<int:business_partner_id>/delete/', methods=['GET', 'POST'])
def deleteBusinessPartner(business_partner_id):
    businessPartnerToDelete = db_session.query(
        BusinessPartner).filter_by(id=business_partner_id).one()
    if request.method == 'POST':
        db_session.delete(businessPartnerToDelete)
        db_session.commit()
        flash("business partner deleted with succes")
        return redirect(
            url_for('displayBusinessPartners'))
    else:
        return render_template(
            'deleteBusinessPartner.html', business_partner=businessPartnerToDelete)





#Request for quote

#Display request for quotes
@app.route('/accounts/payables/data/input/rfqs')
def displayRequestForQuotes():
    rfqs = db_session.query(RequestForQuote).all()
    return render_template('requestForQuotes.html' , rfqs=rfqs)

#Add a request for quote
@app.route('/accounts/payables/data/input/rfq/new/', methods=['GET', 'POST'])
def newRequestForQuote():
    entities = db_session.query(LegalEntity).all()
    periods = db_session.query(CalendarPeriod).all()
    business_partners = db_session.query(BusinessPartner).all()
    if request.method == 'POST':
        newRequestForQuote = RequestForQuote(document_date=request.form['document_date'] ,
            status='O',
            memo=request.form['memo'], 
            created_by=session['login'],
            business_partner_id=request.form['business_partner'],
            entity_id=request.form['entity'],
            period_id=request.form['period'])
        db_session.add(newRequestForQuote)
        db_session.commit()
        flash(gettext("request for quote created with success"))
        return redirect(url_for('displayRequestForQuotes'))
    else:
        return render_template('newRequestForQuote.html' , entities=entities , periods=periods , business_partners=business_partners)

#Edit a request for quote
@app.route('/accounts/payables/data/input/rfq/<int:rfq_id>/edit/', methods=['GET', 'POST'])
def editRequestForQuote(rfq_id):
    editedRequestForQuote = db_session.query(
        RequestForQuote).filter_by(id=rfq_id).one()
    entities = db_session.query(LegalEntity).all()
    periods = db_session.query(CalendarPeriod).all()
    business_partners = db_session.query(BusinessPartner).all()
    if request.method == 'POST':
        if request.form['document_date']:
            editedRequestForQuote.document_date = request.form['document_date']
        if request.form['memo']:
            editedRequestForQuote.memo = request.form['memo']
        if request.form['business_partner']:
            editedRequestForQuote.business_partner_id = request.form['business_partner']
        if request.form['entity']:
            editedRequestForQuote.entity_id = request.form['entity']
        if request.form['period']:
            editedRequestForQuote.period_id = request.form['period']
        editedRequestForQuote.updated_by=session['login']
        db_session.add(editedRequestForQuote)
        db_session.commit()
        flash("request for quote modified with success")
        return redirect(url_for('displayRequestForQuotes'))
    else:
        return render_template(
            'editRequestForQuote.html', rfq=editedRequestForQuote, entities=entities , periods=periods , business_partners=business_partners)

#Delete a request for quote
@app.route('/accounts/payables/data/input/rfq/<int:rfq_id>/delete/', methods=['GET', 'POST'])
def deleteRequestForQuote(rfq_id):
    requestForQuoteToDelete = db_session.query(
        RequestForQuote).filter_by(id=rfq_id).one()
    if request.method == 'POST':
        db_session.delete(requestForQuoteToDelete)
        db_session.commit()
        flash("request for quote deleted with succes")
        return redirect(
            url_for('displayRequestForQuotes'))
    else:
        return render_template(
            'deleteRequestForQuote.html', rfq=requestForQuoteToDelete)

#Request for quote details

#Display request for quote details
@app.route('/accounts/payables/data/input/rfq/<int:rfq_id>/details')
def displayRequestForQuoteDetails(rfq_id):
    rfq = db_session.query(RequestForQuote).filter_by(id=rfq_id).one()
    details = db_session.query(RequestForQuoteDetails).filter_by(
        rfq_id=rfq_id).all()
    return render_template('rfqDetails.html', details=details, rfq=rfq)

#Add detail to a request for quote
@app.route(
    '/accounts/payables/data/input/rfq/<int:rfq_id>/details/new', methods=['GET', 'POST'])
def newRequestForQuoteDetails(rfq_id):
    items = db_session.query(Item).all()
    taxes = db_session.query(Tax).all()
    if request.method == 'POST':
        newRequestForQuoteDetail = RequestForQuoteDetails(price=request.form['price'], 
            quantity=request.form['quantity'],
            created_by=session['login'],
            rfq_id=rfq_id,
            item_id=request.form['item'],
            tax_id=request.form['tax'])
        db_session.add(newRequestForQuoteDetail)
        db_session.commit()
        flash("request for quote detail created with succes")
        return redirect(url_for('displayRequestForQuoteDetails', rfq_id=rfq_id))
    else:
        return render_template('newRfqDetails.html', rfq_id=rfq_id, items=items, taxes=taxes)


# Modify a request for quote details
@app.route(
    '/accounts/payables/data/input/rfq/<int:rfq_id>/details/<int:line_id>/edit', methods=['GET', 'POST'])
def editRequestForQuoteDetails(rfq_id, line_id):
    editedRequestForQuoteDetail = db_session.query(RequestForQuoteDetails).filter_by(id=line_id).one()
    items = db_session.query(Item).all()
    taxes = db_session.query(Tax).all()
    if request.method == 'POST':
        if request.form['price']:
            editedRequestForQuoteDetail.price = request.form['price']
        if request.form['quantity']:
            editedRequestForQuoteDetail.quantity = request.form['quantity']
        if request.form['item']:
            editedRequestForQuoteDetail.item_id = request.form['item']
        if request.form['tax']:
            editedRequestForQuoteDetail.tax_id = request.form['tax']
        db_session.add(editedRequestForQuoteDetail)
        db_session.commit()
        flash("request for quote detail modified with success")
        return redirect(url_for('displayRequestForQuoteDetails', rfq_id=rfq_id))
    else:
        return render_template(
            'editRfqDetails.html', rfq_id=rfq_id, line_id=line_id, detail=editedRequestForQuoteDetail , items=items, taxes=taxes)

# Delete request for quote detail
@app.route('/accounts/payables/data/input/rfq/<int:rfq_id>/details/<int:line_id>/delete', methods=['GET', 'POST'])
def deleteRequestForQuoteDetails(rfq_id, line_id):
    requestForQuoteDetailsToDelete = db_session.query(RequestForQuoteDetails).filter_by(id=line_id).one()
    if request.method == 'POST':
        db_session.delete(requestForQuoteDetailsToDelete)
        db_session.commit()
        flash("request for quote detail deleted with success")
        return redirect(url_for('displayRequestForQuoteDetails', rfq_id=rfq_id))
    else:
        return render_template('deleteRfqDetails.html', detail=requestForQuoteDetailsToDelete, rfq_id=rfq_id)


#Purchase orders

#Display purchase orders
@app.route('/accounts/payables/data/input/purchase_orders')
def displayPurchaseOrders():
    purchase_orders = db_session.query(PurchaseOrder).all()
    return render_template('purchaseOrders.html' , purchase_orders=purchase_orders)

#Add a purchase order
@app.route('/accounts/payables/data/input/purchase_order/new/', methods=['GET', 'POST'])
def newPurchaseOrder():
    entities = db_session.query(LegalEntity).all()
    periods = db_session.query(CalendarPeriod).all()
    business_partners = db_session.query(BusinessPartner).all()
    if request.method == 'POST':
        newPurchaseOrder = PurchaseOrder(document_date=request.form['document_date'],
            document_status='O',
            memo=request.form['memo'], 
            created_by=session['login'],
            business_partner_id=request.form['business_partner'],
            entity_id=request.form['entity'],
            period_id=request.form['period'])
        db_session.add(newPurchaseOrder)
        db_session.commit()
        flash(gettext("purchase order created with success"))
        return redirect(url_for('displayPurchaseOrders'))
    else:
        return render_template('newPurchaseOrder.html' , entities=entities , periods=periods , business_partners=business_partners)

#Edit a purchase order
@app.route('/accounts/payables/data/input/purchase_order/<int:po_id>/edit/', methods=['GET', 'POST'])
def editPurchaseOrder(po_id):
    editedPurchaseOrder = db_session.query(
        PurchaseOrder).filter_by(id=po_id).one()
    entities = db_session.query(LegalEntity).all()
    periods = db_session.query(CalendarPeriod).all()
    business_partners = db_session.query(BusinessPartner).all()
    if request.method == 'POST':
        if request.form['document_date']:
            editedPurchaseOrder.document_date = request.form['document_date']
        if request.form['memo']:
            editedPurchaseOrder.memo = request.form['memo']
        if request.form['business_partner']:
            editedPurchaseOrder.business_partner_id = request.form['business_partner']
        if request.form['entity']:
            editedPurchaseOrder.entity_id = request.form['entity']
        if request.form['period']:
            editedPurchaseOrder.period_id = request.form['period']
        editedPurchaseOrder.updated_by=session['login']
        db_session.add(editedPurchaseOrder)
        db_session.commit()
        flash("purchase order modified with success")
        return redirect(url_for('displayPurchaseOrders'))
    else:
        return render_template(
            'editPurchaseOrder.html', po=editedPurchaseOrder, entities=entities , periods=periods , business_partners=business_partners)

#Delete a purchase order
@app.route('/accounts/payables/data/input/purchase_order/<int:po_id>/delete/', methods=['GET', 'POST'])
def deletePurchaseOrder(po_id):
    purchaseOrderToDelete = db_session.query(
        PurchaseOrder).filter_by(id=po_id).one()
    if request.method == 'POST':
        db_session.delete(purchaseOrderToDelete)
        db_session.commit()
        flash("purchase order deleted with succes")
        return redirect(
            url_for('displayPurchaseOrders'))
    else:
        return render_template(
            'deletePurchaseOrder.html', po=purchaseOrderToDelete)

#Purchase order details

#Display purchase order details
@app.route('/accounts/payables/data/input/purchase_order/<int:po_id>/details')
def displayPurchaseOrderDetails(po_id):
    purchase_order = db_session.query(PurchaseOrder).filter_by(id=po_id).one()
    details = db_session.query(PurchaseOrderDetails).filter_by(
        purchase_order_id=po_id).all()
    return render_template('purchaseOrderDetails.html', details=details, purchase_order=purchase_order)

#Add detail to a purchase order
@app.route(
    '/accounts/payables/data/input/purchase_order/<int:po_id>/details/new', methods=['GET', 'POST'])
def newPurchaseOrderDetails(po_id):
    items = db_session.query(Item).all()
    taxes = db_session.query(Tax).all()
    if request.method == 'POST':
        newPurchaseOrderDetail = PurchaseOrderDetails(price=request.form['price'], 
            quantity=request.form['quantity'],
            created_by=session['login'],
            purchase_order_id=po_id,
            item_id=request.form['item'],
            tax_id=request.form['tax'])
        db_session.add(newPurchaseOrderDetail)
        db_session.commit()
        flash("purchase order detail created with succes")
        return redirect(url_for('displayPurchaseOrderDetails', po_id=po_id))
    else:
        return render_template('newPurchaseOrderDetails.html', po_id=po_id, items=items, taxes=taxes)


# Modify a purchase order details
@app.route(
    '/accounts/payables/data/input/purchase_order/<int:po_id>/details/<int:line_id>/edit', methods=['GET', 'POST'])
def editPurchaseOrderDetails(po_id, line_id):
    editedPurchaseOrderDetail = db_session.query(PurchaseOrderDetails).filter_by(id=line_id).one()
    items = db_session.query(Item).all()
    taxes = db_session.query(Tax).all()
    if request.method == 'POST':
        if request.form['price']:
            editedPurchaseOrderDetail.price = request.form['price']
        if request.form['quantity']:
            editedPurchaseOrderDetail.quantity = request.form['quantity']
        if request.form['item']:
            editedPurchaseOrderDetail.item_id = request.form['item']
        if request.form['tax']:
            editedPurchaseOrderDetail.tax_id = request.form['tax']
        db_session.add(editedPurchaseOrderDetail)
        db_session.commit()
        flash("purchase order detail modified with success")
        return redirect(url_for('displayPurchaseOrderDetails', po_id=po_id))
    else:
        return render_template(
            'editPurchaseOrderDetails.html', po_id=po_id, line_id=line_id, detail=editedPurchaseOrderDetail , items=items, taxes=taxes)

# Delete purchase order detail
@app.route('/accounts/payables/data/input/purchase_order/<int:po_id>/details/<int:line_id>/delete', methods=['GET', 'POST'])
def deletePurchaseOrderDetails(po_id, line_id):
    purchaseOrderDetailsToDelete = db_session.query(PurchaseOrderDetails).filter_by(id=line_id).one()
    if request.method == 'POST':
        db_session.delete(purchaseOrderDetailsToDelete)
        db_session.commit()
        flash("purchase order detail deleted with success")
        return redirect(url_for('displayPurchaseOrderDetails', po_id=po_id))
    else:
        return render_template('deletePurchaseOrderDetails.html', detail=purchaseOrderDetailsToDelete, po_id=po_id)


#Goods receipts

#Display goods receipts
@app.route('/accounts/payables/data/input/goods_receipts')
def displayGoodsReceipts():
    goods_receipts = db_session.query(GoodsReceipt).all()
    return render_template('goodsReceipts.html' , goods_receipts=goods_receipts)

#Add a goods receipt
@app.route('/accounts/payables/data/input/goods_receipt/new/', methods=['GET', 'POST'])
def newGoodsReceipt():
    entities = db_session.query(LegalEntity).all()
    periods = db_session.query(CalendarPeriod).all()
    business_partners = db_session.query(BusinessPartner).all()
    if request.method == 'POST':
        newGoodsReceipt = GoodsReceipt(document_date=request.form['document_date'] ,
            document_status='O',
            memo=request.form['memo'], 
            created_by=session['login'],
            business_partner_id=request.form['business_partner'],
            entity_id=request.form['entity'],
            period_id=request.form['period'])
        db_session.add(newGoodsReceipt)
        db_session.commit()
        flash(gettext("goods receipt created with success"))
        return redirect(url_for('displayGoodsReceipts'))
    else:
        return render_template('newGoodsReceipt.html' , entities=entities , periods=periods , business_partners=business_partners)

#Edit a goods receipts
@app.route('/accounts/payables/data/input/goods_receipt/<int:gr_id>/edit/', methods=['GET', 'POST'])
def editGoodsReceipt(gr_id):
    editedGoodsReceipt = db_session.query(
        GoodsReceipt).filter_by(id=gr_id).one()
    entities = db_session.query(LegalEntity).all()
    periods = db_session.query(CalendarPeriod).all()
    business_partners = db_session.query(BusinessPartner).all()
    if request.method == 'POST':
        if request.form['document_date']:
            editedGoodsReceipt.document_date = request.form['document_date']
        if request.form['memo']:
            editedGoodsReceipt.memo = request.form['memo']
        if request.form['business_partner']:
            editedGoodsReceipt.business_partner_id = request.form['business_partner']
        if request.form['entity']:
            editedGoodsReceipt.entity_id = request.form['entity']
        if request.form['period']:
            editedGoodsReceipt.period_id = request.form['period']
        editedGoodsReceipt.updated_by=session['login']
        db_session.add(editedGoodsReceipt)
        db_session.commit()
        flash("goods receipt modified with success")
        return redirect(url_for('displayGoodsReceipts'))
    else:
        return render_template(
            'editGoodsReceipt.html', gr=editedGoodsReceipt, entities=entities , periods=periods , business_partners=business_partners)

#Delete a goods receipts
@app.route('/accounts/payables/data/input/goods_receipt/<int:gr_id>/delete/', methods=['GET', 'POST'])
def deleteGoodsReceipt(gr_id):
    goodsReceiptToDelete = db_session.query(
        GoodsReceipt).filter_by(id=gr_id).one()
    if request.method == 'POST':
        db_session.delete(goodsReceiptToDelete)
        db_session.commit()
        flash("goods receipt deleted with succes")
        return redirect(
            url_for('displayGoodsReceipts'))
    else:
        return render_template(
            'deleteGoodsReceipt.html', gr=goodsReceiptToDelete)

#Goods receipt details

#Display goods receipt details
@app.route('/accounts/payables/data/input/goods_receipt/<int:gr_id>/details')
def displayGoodsReceiptDetails(gr_id):
    goods_receipt = db_session.query(GoodsReceipt).filter_by(id=gr_id).one()
    details = db_session.query(GoodsReceiptDetails).filter_by(
        goods_receipt_id=gr_id).all()
    return render_template('goodsReceiptDetails.html', details=details, goods_receipt=goods_receipt)

#Add detail to a goods receipt
@app.route(
    '/accounts/payables/data/input/goods_receipt/<int:gr_id>/details/new', methods=['GET', 'POST'])
def newGoodsReceiptDetails(gr_id):
    items = db_session.query(Item).all()
    taxes = db_session.query(Tax).all()
    if request.method == 'POST':
        newGoodsReceiptDetail = GoodsReceiptDetails(price=request.form['price'], 
            quantity=request.form['quantity'],
            created_by=session['login'],
            goods_receipt_id=gr_id,
            item_id=request.form['item'],
            tax_id=request.form['tax'])
        db_session.add(newGoodsReceiptDetail)
        db_session.commit()
        flash("goods receipt detail created with succes")
        return redirect(url_for('displayGoodsReceiptDetails', gr_id=gr_id))
    else:
        return render_template('newGoodsReceiptDetails.html', gr_id=gr_id, items=items, taxes=taxes)


# Modify a goods receipt details
@app.route(
    '/accounts/payables/data/input/goods_receipt/<int:gr_id>/details/<int:line_id>/edit', methods=['GET', 'POST'])
def editGoodsReceiptDetails(gr_id, line_id):
    editedGoodsReceiptDetail = db_session.query(GoodsReceiptDetails).filter_by(id=line_id).one()
    items = db_session.query(Item).all()
    taxes = db_session.query(Tax).all()
    if request.method == 'POST':
        if request.form['price']:
            editedGoodsReceiptDetail.price = request.form['price']
        if request.form['quantity']:
            editedGoodsReceiptDetail.quantity = request.form['quantity']
        if request.form['item']:
            editedGoodsReceiptDetail.item_id = request.form['item']
        if request.form['tax']:
            editedGoodsReceiptDetail.tax_id = request.form['tax']
        db_session.add(editedGoodsReceiptDetail)
        db_session.commit()
        flash("goods receipt detail modified with success")
        return redirect(url_for('displayGoodsReceiptDetails', gr_id=gr_id))
    else:
        return render_template(
            'editGoodsReceiptDetails.html', gr_id=gr_id, line_id=line_id, detail=editedGoodsReceiptDetail , items=items, taxes=taxes)

# Delete request for goods receipt
@app.route('/accounts/payables/data/input/goods_receipt/<int:gr_id>/details/<int:line_id>/delete', methods=['GET', 'POST'])
def deleteGoodsReceiptDetails(gr_id, line_id):
    goodsReceiptDetailsToDelete = db_session.query(GoodsReceiptDetails).filter_by(id=line_id).one()
    if request.method == 'POST':
        db_session.delete(goodsReceiptDetailsToDelete)
        db_session.commit()
        flash("goods receipt detail deleted with success")
        return redirect(url_for('displayGoodsReceiptDetails', gr_id=gr_id))
    else:
        return render_template('deleteGoodsReceiptDetails.html', detail=goodsReceiptDetailsToDelete, gr_id=gr_id)

#Bills

#Display bills
@app.route('/accounts/payables/data/input/bills')
def displayBills():
    bills = db_session.query(Bill).all()
    return render_template('bills.html' , bills=bills)

#Add a bill
@app.route('/accounts/payables/data/input/bill/new/', methods=['GET', 'POST'])
def newBill():
    entities = db_session.query(LegalEntity).all()
    periods = db_session.query(CalendarPeriod).all()
    business_partners = db_session.query(BusinessPartner).all()
    if request.method == 'POST':
        newBill = Bill(document_date=request.form['document_date'] ,
            document_status='O',
            memo=request.form['memo'], 
            created_by=session['login'],
            business_partner_id=request.form['business_partner'],
            entity_id=request.form['entity'],
            period_id=request.form['period'])
        db_session.add(newBill)
        db_session.commit()
        flash(gettext("bill created with success"))
        return redirect(url_for('displayBills'))
    else:
        return render_template('newBill.html' , entities=entities , periods=periods , business_partners=business_partners)

#Edit a bill
@app.route('/accounts/payables/data/input/bill/<int:bill_id>/edit/', methods=['GET', 'POST'])
def editBill(bill_id):
    editedBill = db_session.query(
        Bill).filter_by(id=bill_id).one()
    entities = db_session.query(LegalEntity).all()
    periods = db_session.query(CalendarPeriod).all()
    business_partners = db_session.query(BusinessPartner).all()
    if request.method == 'POST':
        if request.form['document_date']:
            editedBill.document_date = request.form['document_date']
        if request.form['memo']:
            editedBill.memo = request.form['memo']
        if request.form['business_partner']:
            editedBill.business_partner_id = request.form['business_partner']
        if request.form['entity']:
            editedBill.entity_id = request.form['entity']
        if request.form['period']:
            editedBill.period_id = request.form['period']
        editedBill.updated_by=session['login']
        db_session.add(editedBill)
        db_session.commit()
        flash("bill modified with success")
        return redirect(url_for('displayBills'))
    else:
        return render_template(
            'editBill.html', bill=editedBill, entities=entities , periods=periods , business_partners=business_partners)

#Delete a bill
@app.route('/accounts/payables/data/input/bill/<int:bill_id>/delete/', methods=['GET', 'POST'])
def deleteBill(bill_id):
    billToDelete = db_session.query(
        Bill).filter_by(id=bill_id).one()
    if request.method == 'POST':
        db_session.delete(billToDelete)
        db_session.commit()
        flash("bill deleted with succes")
        return redirect(
            url_for('displayBills'))
    else:
        return render_template(
            'deleteBill.html', bill=billToDelete)

#Bill details

#Display bill details
@app.route('/accounts/payables/data/input/bill/<int:bill_id>/details')
def displayBillDetails(bill_id):
    bill = db_session.query(Bill).filter_by(id=bill_id).one()
    details = db_session.query(BillDetails).filter_by(
        bill_id=bill_id).all()
    return render_template('billDetails.html', details=details, bill=bill)

#Add detail to a bill
@app.route(
    '/accounts/payables/data/input/bill/<int:bill_id>/details/new', methods=['GET', 'POST'])
def newBillDetails(bill_id):
    items = db_session.query(Item).all()
    taxes = db_session.query(Tax).all()
    if request.method == 'POST':
        newBillDetail = BillDetails(price=request.form['price'], 
            quantity=request.form['quantity'],
            created_by=session['login'],
            bill_id=bill_id,
            item_id=request.form['item'],
            tax_id=request.form['tax'])
        db_session.add(newBillDetail)
        db_session.commit()
        flash("bill detail created with succes")
        return redirect(url_for('displayBillDetails', bill_id=bill_id))
    else:
        return render_template('newBillDetails.html', bill_id=bill_id, items=items, taxes=taxes)


# Modify a bill details
@app.route(
    '/accounts/payables/data/input/bill/<int:bill_id>/details/<int:line_id>/edit', methods=['GET', 'POST'])
def editBillDetails(bill_id, line_id):
    editedBillDetail = db_session.query(BillDetails).filter_by(id=line_id).one()
    items = db_session.query(Item).all()
    taxes = db_session.query(Tax).all()
    if request.method == 'POST':
        if request.form['price']:
            editedBillDetail.price = request.form['price']
        if request.form['quantity']:
            editedBillDetail.quantity = request.form['quantity']
        if request.form['item']:
            editedBillDetail.item_id = request.form['item']
        if request.form['tax']:
            editedBillDetail.tax_id = request.form['tax']
        db_session.add(editedBillDetail)
        db_session.commit()
        flash("bill detail modified with success")
        return redirect(url_for('displayBillDetails', bill_id=bill_id))
    else:
        return render_template(
            'editBillDetails.html', bill_id=bill_id, line_id=line_id, detail=editedBillDetail , items=items, taxes=taxes)

# Delete bill details
@app.route('/accounts/payables/data/input/bill/<int:bill_id>/details/<int:line_id>/delete', methods=['GET', 'POST'])
def deleteBillDetails(bill_id, line_id):
    billDetailsToDelete = db_session.query(BillDetails).filter_by(id=line_id).one()
    if request.method == 'POST':
        db_session.delete(billDetailsToDelete)
        db_session.commit()
        flash("bill detail deleted with success")
        return redirect(url_for('displayBillDetails', bill_id=bill_id))
    else:
        return render_template('deleteBillDetails.html', detail=billDetailsToDelete, bill_id=bill_id)


#Quotes

#Display quotes
@app.route('/accounts/receivables/data/input/quotes')
def displayQuotes():
    quotes = db_session.query(Quote).all()
    return render_template('quotes.html' , quotes=quotes)

#Add a quote
@app.route('/accounts/receivables/data/input/quote/new/', methods=['GET', 'POST'])
def newQuote():
    entities = db_session.query(LegalEntity).all()
    periods = db_session.query(CalendarPeriod).all()
    business_partners = db_session.query(BusinessPartner).all()
    if request.method == 'POST':
        newQuote = Quote(document_date=request.form['document_date'] ,
            document_status='O',
            memo=request.form['memo'], 
            created_by=session['login'],
            business_partner_id=request.form['business_partner'],
            entity_id=request.form['entity'],
            period_id=request.form['period'])
        db_session.add(newQuote)
        db_session.commit()
        flash(gettext("quote created with success"))
        return redirect(url_for('displayQuotes'))
    else:
        return render_template('newQuote.html' , entities=entities , periods=periods , business_partners=business_partners)

#Edit a quote
@app.route('/accounts/receivables/data/input/quote/<int:quote_id>/edit/', methods=['GET', 'POST'])
def editQuote(quote_id):
    editedQuote = db_session.query(
        Quote).filter_by(id=quote_id).one()
    entities = db_session.query(LegalEntity).all()
    periods = db_session.query(CalendarPeriod).all()
    business_partners = db_session.query(BusinessPartner).all()
    if request.method == 'POST':
        if request.form['document_date']:
            editedQuote.document_date = request.form['document_date']
        if request.form['memo']:
            editedQuote.memo = request.form['memo']
        if request.form['business_partner']:
            editedQuote.business_partner_id = request.form['business_partner']
        if request.form['entity']:
            editedQuote.entity_id = request.form['entity']
        if request.form['period']:
            editedQuote.period_id = request.form['period']
        editedQuote.updated_by=session['login']
        db_session.add(editedQuote)
        db_session.commit()
        flash("quote modified with success")
        return redirect(url_for('displayQuotes'))
    else:
        return render_template(
            'editQuote.html', quote=editedQuote, entities=entities , periods=periods , business_partners=business_partners)

#Delete a quote
@app.route('/accounts/receivables/data/input/quote/<int:quote_id>/delete/', methods=['GET', 'POST'])
def deleteQuote(quote_id):
    quoteToDelete = db_session.query(
        Quote).filter_by(id=quote_id).one()
    if request.method == 'POST':
        db_session.delete(quoteToDelete)
        db_session.commit()
        flash("quote deleted with succes")
        return redirect(
            url_for('displayQuotes'))
    else:
        return render_template(
            'deleteQuote.html', quote=quoteToDelete)

#Quote details

#Display quote details
@app.route('/accounts/receivables/data/input/quote/<int:quote_id>/details')
def displayQuoteDetails(quote_id):
    quote = db_session.query(Quote).filter_by(id=quote_id).one()
    details = db_session.query(QuoteDetails).filter_by(
        quote_id=quote_id).all()
    return render_template('quoteDetails.html', details=details, quote=quote)

#Add detail to a quote
@app.route(
    '/accounts/receivables/data/input/quote/<int:quote_id>/details/new', methods=['GET', 'POST'])
def newQuoteDetails(quote_id):
    items = db_session.query(Item).all()
    taxes = db_session.query(Tax).all()
    if request.method == 'POST':
        newQuoteDetail = QuoteDetails(price=request.form['price'], 
            quantity=request.form['quantity'],
            created_by=session['login'],
            quote_id=quote_id,
            item_id=request.form['item'],
            tax_id=request.form['tax'])
        db_session.add(newQuoteDetail)
        db_session.commit()
        flash("quote detail created with succes")
        return redirect(url_for('displayQuoteDetails', quote_id=quote_id))
    else:
        return render_template('newQuoteDetails.html', quote_id=quote_id, items=items, taxes=taxes)


# Modify a quote details
@app.route(
    '/accounts/receivables/data/input/quote/<int:quote_id>/details/<int:line_id>/edit', methods=['GET', 'POST'])
def editQuoteDetails(quote_id, line_id):
    editedQuoteDetail = db_session.query(QuoteDetails).filter_by(id=line_id).one()
    items = db_session.query(Item).all()
    taxes = db_session.query(Tax).all()
    if request.method == 'POST':
        if request.form['price']:
            editedQuoteDetail.price = request.form['price']
        if request.form['quantity']:
            editedQuoteDetail.quantity = request.form['quantity']
        if request.form['item']:
            editedQuoteDetail.item_id = request.form['item']
        if request.form['tax']:
            editedQuoteDetail.tax_id = request.form['tax']
        db_session.add(editedQuoteDetail)
        db_session.commit()
        flash("quote detail modified with success")
        return redirect(url_for('displayQuoteDetails', quote_id=quote_id))
    else:
        return render_template(
            'editQuoteDetails.html', quote_id=quote_id, line_id=line_id, detail=editedQuoteDetail , items=items, taxes=taxes)

# Delete quote details
@app.route('/accounts/receivables/data/input/quote/<int:quote_id>/details/<int:line_id>/delete', methods=['GET', 'POST'])
def deleteQuoteDetails(quote_id, line_id):
    quoteDetailsToDelete = db_session.query(QuoteDetails).filter_by(id=line_id).one()
    if request.method == 'POST':
        db_session.delete(quoteDetailsToDelete)
        db_session.commit()
        flash("quote detail deleted with success")
        return redirect(url_for('displayQuoteDetails', quote_id=quote_id))
    else:
        return render_template('deleteQuoteDetails.html', detail=quoteDetailsToDelete, quote_id=quote_id)


#Sale orders

#Display sale orders
@app.route('/accounts/receivables/data/input/sale_orders')
def displaySaleOrders():
    sale_orders = db_session.query(SaleOrder).all()
    return render_template('saleOrders.html' , sale_orders=sale_orders)

#Add a sale order
@app.route('/accounts/receivables/data/input/sale_order/new/', methods=['GET', 'POST'])
def newSaleOrder():
    entities = db_session.query(LegalEntity).all()
    periods = db_session.query(CalendarPeriod).all()
    business_partners = db_session.query(BusinessPartner).all()
    if request.method == 'POST':
        newSaleOrder = SaleOrder(document_date=request.form['document_date'] ,
            document_status='O',
            memo=request.form['memo'], 
            created_by=session['login'],
            business_partner_id=request.form['business_partner'],
            entity_id=request.form['entity'],
            period_id=request.form['period'])
        db_session.add(newSaleOrder)
        db_session.commit()
        flash(gettext("sale order created with success"))
        return redirect(url_for('displaySaleOrders'))
    else:
        return render_template('newSaleOrder.html' , entities=entities , periods=periods , business_partners=business_partners)

#Edit a sale order
@app.route('/accounts/receivables/data/input/sale_order/<int:so_id>/edit/', methods=['GET', 'POST'])
def editSaleOrder(so_id):
    editedSaleOrder = db_session.query(
        SaleOrder).filter_by(id=so_id).one()
    entities = db_session.query(LegalEntity).all()
    periods = db_session.query(CalendarPeriod).all()
    business_partners = db_session.query(BusinessPartner).all()
    if request.method == 'POST':
        if request.form['document_date']:
            editedSaleOrder.document_date = request.form['document_date']
        if request.form['memo']:
            editedSaleOrder.memo = request.form['memo']
        if request.form['business_partner']:
            editedSaleOrder.business_partner_id = request.form['business_partner']
        if request.form['entity']:
            editedSaleOrder.entity_id = request.form['entity']
        if request.form['period']:
            editedSaleOrder.period_id = request.form['period']
        editedSaleOrder.updated_by=session['login']
        db_session.add(editedSaleOrder)
        db_session.commit()
        flash("sale order modified with success")
        return redirect(url_for('displaySaleOrders'))
    else:
        return render_template(
            'editSaleOrder.html', sale_order=editedSaleOrder, entities=entities , periods=periods , business_partners=business_partners)

#Delete a sale order
@app.route('/accounts/receivables/data/input/sale_order/<int:so_id>/delete/', methods=['GET', 'POST'])
def deleteSaleOrder(so_id):
    saleOrderToDelete = db_session.query(
        SaleOrder).filter_by(id=so_id).one()
    if request.method == 'POST':
        db_session.delete(saleOrderToDelete)
        db_session.commit()
        flash("sale order deleted with succes")
        return redirect(
            url_for('displaySaleOrders'))
    else:
        return render_template(
            'deleteSaleOrder.html', sale_order=saleOrderToDelete)

#Sale order details

#Display sale order details
@app.route('/accounts/receivables/data/input/sale_order/<int:so_id>/details')
def displaySaleOrderDetails(so_id):
    sale_order = db_session.query(SaleOrder).filter_by(id=so_id).one()
    details = db_session.query(SaleOrderDetails).filter_by(
        sale_order_id=so_id).all()
    return render_template('saleOrderDetails.html', details=details, sale_order=sale_order)

#Add detail to a sale order
@app.route(
    '/accounts/receivables/data/input/sale_order/<int:so_id>/details/new', methods=['GET', 'POST'])
def newSaleOrderDetails(so_id):
    items = db_session.query(Item).all()
    taxes = db_session.query(Tax).all()
    if request.method == 'POST':
        newSaleOrderDetail = SaleOrderDetails(price=request.form['price'], 
            quantity=request.form['quantity'],
            created_by=session['login'],
            sale_order_id=so_id,
            item_id=request.form['item'],
            tax_id=request.form['tax'])
        db_session.add(newSaleOrderDetail)
        db_session.commit()
        flash("sale order detail created with succes")
        return redirect(url_for('displaySaleOrderDetails', so_id=so_id))
    else:
        return render_template('newSaleOrderDetails.html', so_id=so_id, items=items, taxes=taxes)


# Modify a sale order details
@app.route(
    '/accounts/receivables/data/input/sale_order/<int:so_id>/details/<int:line_id>/edit', methods=['GET', 'POST'])
def editSaleOrderDetails(so_id, line_id):
    editedSaleOrderDetail = db_session.query(SaleOrderDetails).filter_by(id=line_id).one()
    items = db_session.query(Item).all()
    taxes = db_session.query(Tax).all()
    if request.method == 'POST':
        if request.form['price']:
            editedSaleOrderDetail.price = request.form['price']
        if request.form['quantity']:
            editedSaleOrderDetail.quantity = request.form['quantity']
        if request.form['item']:
            editedSaleOrderDetail.item_id = request.form['item']
        if request.form['tax']:
            editedSaleOrderDetail.tax_id = request.form['tax']
        db_session.add(editedSaleOrderDetail)
        db_session.commit()
        flash("sale order modified with success")
        return redirect(url_for('displaySaleOrderDetails', so_id=so_id))
    else:
        return render_template(
            'editSaleOrderDetails.html', so_id=so_id, line_id=line_id, detail=editedSaleOrderDetail , items=items, taxes=taxes)

# Delete sale order details
@app.route('/accounts/receivables/data/input/sale_order/<int:so_id>/details/<int:line_id>/delete', methods=['GET', 'POST'])
def deleteSaleOrderDetails(so_id, line_id):
    saleOrderDetailsToDelete = db_session.query(SaleOrderDetails).filter_by(id=line_id).one()
    if request.method == 'POST':
        db_session.delete(saleOrderDetailsToDelete)
        db_session.commit()
        flash("sale order detail deleted with success")
        return redirect(url_for('displaySaleOrderDetails', so_id=so_id))
    else:
        return render_template('deleteSaleOrderDetails.html', detail=saleOrderDetailsToDelete, so_id=so_id)

#Shippings

#Display shippings
@app.route('/accounts/receivables/data/input/shippings')
def displayShippings():
    shippings = db_session.query(Shipping).all()
    return render_template('shippings.html' , shippings=shippings)

#Add a shipping
@app.route('/accounts/receivables/data/input/shipping/new/', methods=['GET', 'POST'])
def newShipping():
    entities = db_session.query(LegalEntity).all()
    periods = db_session.query(CalendarPeriod).all()
    business_partners = db_session.query(BusinessPartner).all()
    if request.method == 'POST':
        newShipping = Shipping(document_date=request.form['document_date'] ,
            document_status='O',
            memo=request.form['memo'], 
            created_by=session['login'],
            business_partner_id=request.form['business_partner'],
            entity_id=request.form['entity'],
            period_id=request.form['period'])
        db_session.add(newShipping)
        db_session.commit()
        flash(gettext("shipping created with success"))
        return redirect(url_for('displayShippings'))
    else:
        return render_template('newShipping.html' , entities=entities , periods=periods , business_partners=business_partners)

#Edit a shipping
@app.route('/accounts/receivables/data/input/shipping/<int:sh_id>/edit/', methods=['GET', 'POST'])
def editShipping(sh_id):
    editedShipping = db_session.query(
        Shipping).filter_by(id=sh_id).one()
    entities = db_session.query(LegalEntity).all()
    periods = db_session.query(CalendarPeriod).all()
    business_partners = db_session.query(BusinessPartner).all()
    if request.method == 'POST':
        if request.form['document_date']:
            editedShipping.document_date = request.form['document_date']
        if request.form['memo']:
            editedShipping.memo = request.form['memo']
        if request.form['business_partner']:
            editedShipping.business_partner_id = request.form['business_partner']
        if request.form['entity']:
            editedShipping.entity_id = request.form['entity']
        if request.form['period']:
            editedShipping.period_id = request.form['period']
        editedShipping.updated_by=session['login']
        db_session.add(editedShipping)
        db_session.commit()
        flash("shipping modified with success")
        return redirect(url_for('displayShippings'))
    else:
        return render_template(
            'editShipping.html', shipping=editedShipping, entities=entities , periods=periods , business_partners=business_partners)

#Delete a shipping
@app.route('/accounts/receivables/data/input/shipping/<int:sh_id>/delete/', methods=['GET', 'POST'])
def deleteShipping(sh_id):
    shippingToDelete = db_session.query(
        Shipping).filter_by(id=sh_id).one()
    if request.method == 'POST':
        db_session.delete(shippingToDelete)
        db_session.commit()
        flash("shipping deleted with succes")
        return redirect(
            url_for('displayShippings'))
    else:
        return render_template(
            'deleteShipping.html', shipping=shippingToDelete)

#Shipping details

#Display shipping details
@app.route('/accounts/receivables/data/input/shipping/<int:sh_id>/details')
def displayShippingDetails(sh_id):
    shipping = db_session.query(Shipping).filter_by(id=sh_id).one()
    details = db_session.query(ShippingDetails).filter_by(
        shipping_id=sh_id).all()
    return render_template('shippingDetails.html', details=details, shipping=shipping)

#Add detail to a shipping
@app.route(
    '/accounts/receivables/data/input/shipping/<int:sh_id>/details/new', methods=['GET', 'POST'])
def newShippingDetails(sh_id):
    items = db_session.query(Item).all()
    taxes = db_session.query(Tax).all()
    if request.method == 'POST':
        newShippingDetail = ShippingDetails(price=request.form['price'], 
            quantity=request.form['quantity'],
            created_by=session['login'],
            shipping_id=sh_id,
            item_id=request.form['item'],
            tax_id=request.form['tax'])
        db_session.add(newShippingDetail)
        db_session.commit()
        flash("shipping detail created with succes")
        return redirect(url_for('displayShippingDetails', sh_id=sh_id))
    else:
        return render_template('newShippingDetails.html', sh_id=sh_id, items=items, taxes=taxes)


# Modify a shipping details
@app.route(
    '/accounts/receivables/data/input/shipping/<int:sh_id>/details/<int:line_id>/edit', methods=['GET', 'POST'])
def editShippingDetails(sh_id, line_id):
    editedShippingDetail = db_session.query(ShippingDetails).filter_by(id=line_id).one()
    items = db_session.query(Item).all()
    taxes = db_session.query(Tax).all()
    if request.method == 'POST':
        if request.form['price']:
            editedShippingDetail.price = request.form['price']
        if request.form['quantity']:
            editedShippingDetail.quantity = request.form['quantity']
        if request.form['item']:
            editedShippingDetail.item_id = request.form['item']
        if request.form['tax']:
            editedShippingDetail.tax_id = request.form['tax']
        db_session.add(editedShippingDetail)
        db_session.commit()
        flash("shipping detail modified with success")
        return redirect(url_for('displayShippingDetails', sh_id=sh_id))
    else:
        return render_template(
            'editShippingDetails.html', sh_id=sh_id, line_id=line_id, detail=editedShippingDetail , items=items, taxes=taxes)

# Delete shipping details
@app.route('/accounts/receivables/data/input/shipping/<int:sh_id>/details/<int:line_id>/delete', methods=['GET', 'POST'])
def deleteShippingDetails(sh_id, line_id):
    shippingDetailsToDelete = db_session.query(ShippingDetails).filter_by(id=line_id).one()
    if request.method == 'POST':
        db_session.delete(shippingDetailsToDelete)
        db_session.commit()
        flash("shipping detail deleted with success")
        return redirect(url_for('displayShippingDetails', sh_id=sh_id))
    else:
        return render_template('deleteShippingDetails.html', detail=shippingDetailsToDelete, sh_id=sh_id)

#Invoices

#Display invoices
@app.route('/accounts/receivables/data/input/invoices')
def displayInvoices():
    invoices = db_session.query(Invoice).all()
    return render_template('invoices.html' , invoices=invoices)

#Add a invoice
@app.route('/accounts/receivables/data/input/invoice/new/', methods=['GET', 'POST'])
def newInvoice():
    entities = db_session.query(LegalEntity).all()
    periods = db_session.query(CalendarPeriod).all()
    business_partners = db_session.query(BusinessPartner).all()
    if request.method == 'POST':
        newInvoice = Invoice(document_date=request.form['document_date'] ,
            document_status='O',
            memo=request.form['memo'], 
            created_by=session['login'],
            business_partner_id=request.form['business_partner'],
            entity_id=request.form['entity'],
            period_id=request.form['period'])
        db_session.add(newInvoice)
        db_session.commit()
        flash(gettext("invoice created with success"))
        return redirect(url_for('displayInvoices'))
    else:
        return render_template('newInvoice.html' , entities=entities , periods=periods , business_partners=business_partners)

#Edit a invoice
@app.route('/accounts/receivables/data/input/invoice/<int:invoice_id>/edit/', methods=['GET', 'POST'])
def editInvoice(invoice_id):
    editedInvoice = db_session.query(
        Invoice).filter_by(id=invoice_id).one()
    entities = db_session.query(LegalEntity).all()
    periods = db_session.query(CalendarPeriod).all()
    business_partners = db_session.query(BusinessPartner).all()
    if request.method == 'POST':
        if request.form['document_date']:
            editedInvoice.document_date = request.form['document_date']
        if request.form['memo']:
            editedInvoice.memo = request.form['memo']
        if request.form['business_partner']:
            editedInvoice.business_partner_id = request.form['business_partner']
        if request.form['entity']:
            editedInvoice.entity_id = request.form['entity']
        if request.form['period']:
            editedInvoice.period_id = request.form['period']
        editedInvoice.updated_by=session['login']
        db_session.add(editedInvoice)
        db_session.commit()
        flash("invoice modified with success")
        return redirect(url_for('displayInvoices'))
    else:
        return render_template(
            'editInvoice.html', invoice=editedInvoice, entities=entities , periods=periods , business_partners=business_partners)

#Delete a invoice
@app.route('/accounts/receivables/data/input/invoice/<int:invoice_id>/delete/', methods=['GET', 'POST'])
def deleteInvoice(invoice_id):
    invoiceToDelete = db_session.query(
        Invoice).filter_by(id=invoice_id).one()
    if request.method == 'POST':
        db_session.delete(invoiceToDelete)
        db_session.commit()
        flash("invoice deleted with succes")
        return redirect(
            url_for('displayInvoices'))
    else:
        return render_template(
            'deleteInvoice.html', invoice=invoiceToDelete)

#Invoice details

#Display invoice details
@app.route('/accounts/receivables/data/input/invoice/<int:invoice_id>/details')
def displayInvoiceDetails(invoice_id):
    invoice = db_session.query(Invoice).filter_by(id=invoice_id).one()
    details = db_session.query(InvoiceDetails).filter_by(
        invoice_id=invoice_id).all()
    return render_template('invoiceDetails.html', details=details, invoice=invoice)

#Add detail to an invoice
@app.route(
    '/accounts/receivables/data/input/invoice/<int:invoice_id>/details/new', methods=['GET', 'POST'])
def newInvoiceDetails(invoice_id):
    items = db_session.query(Item).all()
    taxes = db_session.query(Tax).all()
    if request.method == 'POST':
        newInvoiceDetail = InvoiceDetails(price=request.form['price'], 
            quantity=request.form['quantity'],
            created_by=session['login'],
            invoice_id=invoice_id,
            item_id=request.form['item'],
            tax_id=request.form['tax'])
        db_session.add(newInvoiceDetail)
        db_session.commit()
        flash("invoice detail created with succes")
        return redirect(url_for('displayInvoiceDetails', invoice_id=invoice_id))
    else:
        return render_template('newInvoiceDetails.html', invoice_id=invoice_id, items=items, taxes=taxes)


# Modify a invoice details
@app.route(
    '/accounts/receivables/data/input/invoice/<int:invoice_id>/details/<int:line_id>/edit', methods=['GET', 'POST'])
def editInvoiceDetails(invoice_id, line_id):
    editedInvoiceDetail = db_session.query(InvoiceDetails).filter_by(id=line_id).one()
    items = db_session.query(Item).all()
    taxes = db_session.query(Tax).all()
    if request.method == 'POST':
        if request.form['price']:
            editedInvoiceDetail.price = request.form['price']
        if request.form['quantity']:
            editedInvoiceDetail.quantity = request.form['quantity']
        if request.form['item']:
            editedInvoiceDetail.item_id = request.form['item']
        if request.form['tax']:
            editedInvoiceDetail.tax_id = request.form['tax']
        db_session.add(editedInvoiceDetail)
        db_session.commit()
        flash("invoice detail modified with success")
        return redirect(url_for('displayInvoiceDetails', invoice_id=invoice_id))
    else:
        return render_template(
            'editInvoiceDetails.html', invoice_id=invoice_id, line_id=line_id, detail=editedInvoiceDetail , items=items, taxes=taxes)

# Delete invoice details
@app.route('/accounts/receivables/data/input/invoice/<int:invoice_id>/details/<int:line_id>/delete', methods=['GET', 'POST'])
def deleteInvoiceDetails(invoice_id, line_id):
    invoiceDetailsToDelete = db_session.query(InvoiceDetails).filter_by(id=line_id).one()
    if request.method == 'POST':
        db_session.delete(invoiceDetailsToDelete)
        db_session.commit()
        flash("invoice detail deleted with success")
        return redirect(url_for('displayInvoiceDetails', invoice_id=invoice_id))
    else:
        return render_template('deleteInvoiceDetails.html', detail=invoiceDetailsToDelete, invoice_id=invoice_id)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
