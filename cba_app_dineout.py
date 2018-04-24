import datetime
import os
import sys 
import hashlib
from flask import Flask, session, render_template, request, redirect, jsonify, url_for, flash,g
from flask import Flask,jsonify,json
from flask_babel import Babel , gettext
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.utils import secure_filename



#from cba_db import (RestaurantList)
from cba_db_restaurant import (RestaurantList,City,Locality,Area,BookingList,DinerList,OrderList,OfferList)
from json import dumps


UPLOAD_FOLDER = '/home/varun/code/python/cba_python_mysql'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

#app.config.from_pyfile('cba_babel.cfg')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
babel = Babel(app , default_locale='en', default_timezone='UTC', date_formats=None, configure_jinja=True)

Base = declarative_base()

#engine = create_engine('sqlite:///cba.db')
engine = create_engine('mysql://root@127.0.0.1:3306/cba', echo=True)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
db_session = DBSession()

# add to you main app code
@babel.localeselector
def get_locale():
    return g.get('lang_code', app.config['BABEL_DEFAULT_LOCALE'])


#Login function
@app.route('/' , methods=['GET', 'POST'])
@app.route('/login' , methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    if request.form['login']:
       hash_object = hashlib.md5(request.form['secret'].encode())
       password = hash_object.hexdigest()
       try:
           dinerList= db_session.query(DinerList).filter_by(d_email =request.form['login'],d_password=password).one()
           if password == dinerList.d_password:
                session['user_id'] = dinerList.d_id
                return redirect(url_for('home'))
           else:
                error ="Please check login details"
                return render_template('/dineout/loginForm.html', message=error)    
       except NoResultFound:
                error ="Please check login details"
                return render_template('/dineout/loginForm.html', message=error)
  else:
     return render_template('/dineout/loginForm.html', message=session)

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
    return render_template('home_dineout.html')

#Add a new restaurant
@app.route('/adminstration/structure/new_restaurant/', methods=['GET', 'POST'])
def newRestaurant():
    entities = db_session.query(RestaurantList).filter_by(area_id = 8).all()
    city = db_session.query(City).filter_by(status=1).order_by(City.name).all()
    if request.method == 'POST':
        newRestaurant = RestaurantList(profile_name=request.form['profile_name'], 
            address=request.form['address'], 
            pincode=request.form['pincode'],
            phone=request.form['phone'],
            area_id=request.form['area_id'],
            locality_id=request.form['locality_id'],
            city_id=request.form['city_id'],
            status=request.form['status']
           )


        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  
        db_session.add(newRestaurant)
        db_session.commit()
        flash(gettext("item restaurant created with success"))
        return redirect(url_for('displayRestaurant'))
    else:
        return render_template('/dineout/newRestaurant.html' , entities=entities,city=city)



#Display restaurant
@app.route('/adminstration/structure/view_restaurant')
def displayRestaurant():
    restaurantList = db_session.query(RestaurantList).filter_by(area_id = 8).limit(2000).all()
    return render_template('/dineout/viewRestaurant.html' , restaurant_list=restaurantList)

#Edit restaurant
@app.route('/adminstration/structure/edit_restaurant/<int:r_id>/edit/', methods=['GET', 'POST'])
def editRestaurant(r_id):
    editedRestaurant = db_session.query(
        RestaurantList).filter_by(r_id=r_id).one()
    entities = db_session.query(RestaurantList).all()
    if request.method == 'POST':
        if request.form['profile_name']:
            editedRestaurant.profile_name = request.form['profile_name']
        if request.form['address']:
            editedRestaurant.address = request.form['address']
        if request.form['pincode']:
            editedRestaurant.pincode = request.form['pincode']
        if request.form['phone']:
            editedRestaurant.phone = request.form['phone']
        if request.form['status']:
            editedRestaurant.status = request.form['status']
        if request.form['city_name']:
            editedRestaurant.city_name = request.form['city_name']
        if request.form['state_name']:
            editedRestaurant.state_name = request.form['state_name']
        if request.form['locality_name']:
            editedRestaurant.locality_name = request.form['locality_name']
        if request.form['area_name']:
            editedRestaurant.area_name = request.form['area_name']
        editedRestaurant.updated_by=session['login']
        db_session.add(editedRestaurant)
        db_session.commit()
        flash("restaurant modified with success")
        return redirect(url_for('displayRestaurant'))
    else:
        return render_template(
            '/dineout/editRestaurant.html', view_restaurant=editedRestaurant, entities=entities)

#Delete restaurant
@app.route('/adminstration/structure/item_category/<int:r_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(r_id):
    itemCategoryToDelete = db_session.query(
        RestaurantList).filter_by(r_id=r_id).one()
    if request.method == 'POST':
        db_session.delete(itemCategoryToDelete)
        db_session.commit()
        flash("item category deleted with succes")
        return redirect(
            url_for('displayRestaurant'))
    else:
        return render_template(
            '/dineout/deleteRestaurant.html', category=itemCategoryToDelete)


#Display Area
@app.route('/adminstration/structure/get_area', methods=['GET', 'POST'])
def getArea():
    if request.method == 'POST':
        city_id= request.form['city_id']
        cityList = db_session.query(Area).filter_by(parent_id = city_id).filter_by(status = 1).all()
        return render_template(
            '/dineout/select_box.html', city_list=cityList)

#Display Locality
@app.route('/adminstration/structure/get_locality', methods=['GET', 'POST'])
def getLocality():
    if request.method == 'POST':
        parent_id= request.form['area_id']
        areaList = db_session.query(Locality).filter_by(parent_id = parent_id).filter_by(status = 1).all()
        return render_template(
            '/dineout/select_box_locality.html', city_list=areaList)


#Get Restaurant
@app.route('/adminstration/structure/get_restaurant', methods=['GET', 'POST'])
def getRestaurant():
    if request.method == 'POST':
        city_id= request.form['city_id']
        restaurantList = db_session.query(RestaurantList).filter_by(city_id = city_id).filter_by(status = 1).all()
        return render_template(
            '/dineout/select_box_restaurant.html', restaurant_list=restaurantList)



#Display bookings
@app.route('/adminstration/structure/view_bookings')
def displayBookings():
    bookingList = db_session.query(BookingList).filter(BookingList.dining_dt_time > '2017-01-01 00:00:00', BookingList.dining_dt_time < '2017-01-10 23:59:59').limit(2000).all()
    return render_template('/dineout/viewBookings.html' , booking_list=bookingList)


#Display Diners
@app.route('/adminstration/structure/view_diners')
def displayDiners():
    dinerList= db_session.query(DinerList).filter_by(is_do_plus_member=1).order_by(DinerList.d_id.desc()).limit(2000).all()
    return render_template('/dineout/viewDiners.html',diner_list=dinerList)
    

#Add a new Diner
@app.route('/adminstration/structure/new_Diner/', methods=['GET', 'POST'])
def newDiner():
    entities = db_session.query(DinerList).filter_by(is_verified=1).first()
    city = db_session.query(City).filter_by(status=1).order_by(City.name).all()

    if request.method == 'POST':
        newDiner = DinerList(d_first_name=request.form['d_first_name'], 
                        d_last_name=request.form['d_last_name'], 
                        d_email=request.form['d_email'],
                        d_phone=request.form['d_phone'],
                        d_city_id=request.form['d_city_id'],
                        is_verified=request.form['is_verified'],
                        is_do_plus_member=request.form['is_do_plus_member']
        )
        db_session.add(newDiner)
        db_session.commit()
        flash(gettext("item Diner created with success"))
        return redirect(url_for('displayDiners'))
    else:
        return render_template('/dineout/newDiner.html' , entities=entities,city=city)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


#Diner History
@app.route('/adminstration/structure/diner_history')
def dinerHistory():
    dinerList= db_session.query(DinerList).filter_by(is_do_plus_member=1).order_by(DinerList.d_id.desc()).limit(2000).all()
    return render_template('/dineout/viewDiners.html',diner_list=dinerList)
   
#Order History
@app.route('/adminstration/structure/order_history')
def orderHistory():
    orderList= db_session.query(OrderList).order_by(OrderList.id.desc()).limit(2000).all()
    return render_template('/dineout/viewOrders.html',order_list=orderList)
   

#Add a new booking
@app.route('/adminstration/structure/new_booking/', methods=['GET', 'POST'])
def newBooking():
    city = db_session.query(City).filter_by(status=1).order_by(City.name).all()
    if request.method == 'POST':
        newBooking = BookingList(diner_phone=request.form['diner_phone'], 
            diner_name=request.form['diner_name'], 
            diner_email=request.form['diner_email'],
            restaurant_id=request.form['restaurant_id'],
            offer_id=request.form['offer_id'],
            cnt_covers_males=request.form['male'],
            booking_status='NW',
            cnt_covers=request.form['female']+request.form['male']
           )

        db_session.add(newBooking)
        db_session.commit()
        flash(gettext("item restaurant created with success"))
        return redirect(url_for('displayBookings'))
    else:
        return render_template('/dineout/newBooking.html' ,city=city)

#Offer List
@app.route('/adminstration/structure/get_offer', methods=['GET', 'POST'])
def getOffer():
    if request.method == 'POST':
        restaurant_id= request.form['restaurant_id']
        offerList = db_session.query(OfferList).filter_by(restaurant_id = restaurant_id).filter_by(is_active = 1).all()
        return render_template(
            '/dineout/select_box.html', offer_list=offerList,display=1)

#Check Diner Phone No
@app.route('/adminstration/structure/get_diner_exist', methods=['GET', 'POST'])
def getDinerExist():
    if request.method == 'POST':
        d_phone= request.form['diner_phone']
        dinerList = db_session.query(DinerList).filter_by(d_phone = d_phone).filter_by(is_verified = 1).all()
        return jsonify([i.serialize for i in dinerList])

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
