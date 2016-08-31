from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref

from spolight.model import Base
from spolight.model.League import *
class Competition(Base):
    __tablename__='competition'

    id = Column(Integer, primary_key=True)
    league_id = Column(Integer, ForeignKey(League.id))
    season=Column(String(100))
    st_date=Column(DateTime)
    en_date=Column(DateTime)

    def __init__(self,league_id,season,st_date,en_date):
        self.league_id=league_id
        self.season=season
        self.st_date=st_date
        self.en_date=en_date

    def __repr__(self):
        return "<Competition('%r','%r','%r','%r')>"%(self.league_id,self.season,self.st_date,self.en_date)

