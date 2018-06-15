import os
import sys
import datetime 
from sqlalchemy import Column,ForeignKey,Integer,String,Date,Float,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class MoviesList(Base):
    __tablename__ = 'movie'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    movieID = Column(Integer, primary_key=True)
    movieTitle = Column(String(80), nullable=False)
    movieDesc = Column(String(255) , nullable=True)
    movieReleaseDate = Column(Date ,default=datetime.datetime.now)
    movieRuntime = Column(Integer ,nullable=True)
    movieCertificate = Column(String(255) , nullable=True)
    movieRating = Column(Integer ,nullable=True)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'movieID': self.movieID,
            'movieTitle' : self.movieTitle,
            'movieDesc'      : self.movieDesc,
            'movieReleaseDate'      : self.movieReleaseDate,
            'movieRuntime'        : self.movieRuntime,
            'movieCertificate'    : self.movieCertificate,
            'movieRating'   : self.movieRating
        }


engine = create_engine('mysql://root:root@127.0.0.1/testdb')      

Base.metadata.create_all(engine)
