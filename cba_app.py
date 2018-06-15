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


from cba_db import (MoviesList)
from json import dumps


UPLOAD_FOLDER = '/home/varun/code/movi_app/static/img/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
babel = Babel(app , default_locale='en', default_timezone='UTC', date_formats=None, configure_jinja=True)

Base = declarative_base()


engine = create_engine('mysql://root:root@127.0.0.1:3306/testdb', echo=True)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
db_session = DBSession()

# add to you main app code
@babel.localeselector
def get_locale():
    return g.get('lang_code', app.config['BABEL_DEFAULT_LOCALE'])

#@app.route('/' , methods=['GET', 'POST'])
@app.route('/')
def displayMovies():
    moviesList = db_session.query(MoviesList).limit(2000).all()
    return render_template('viewMovies.html' , movies_list=moviesList)

#Add a new movi
@app.route('/new_movies/', methods=['GET', 'POST'])
def newRestaurant():
    entities = db_session.query(MoviesList).filter_by(movieID = 1).all()
    if request.method == 'POST':
        newMovies = MoviesList( 
            movieTitle=request.form['movie_title'],
            movieDesc=request.form['movie_desc'],
            movieReleaseDate=request.form['movie_release_date'],
            movieRuntime=request.form['movie_runtime'],
            movieCertificate=request.form['movie_certificate'],
            movieRating=request.form['movie_rating']
           )
        db_session.add(newMovies)
        db_session.commit()
        flash(gettext("Movi insert with success"))
        return redirect(url_for('displayMovies'))
    else:
        return render_template('newMovies.html')


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='127.0.0.9', port=8000)
