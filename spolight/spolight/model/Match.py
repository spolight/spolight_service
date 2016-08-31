from sqlalchemy import Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship, backref

from spolight.model import Base

class Match(Base):
	__tablename__='match'
	id=Column(Integer,primary_key=True)
	date=Column(DateTime)
	status=Column(String(10))
	home=Column(String(100))
	away=Column(String(100))
	h_score=Column(Integer)
	a_score=Column(Integer)

	def __init__(self,date,status,home,away,h_score,a_score):
		self.date = date
		self.status = status
		self.home = home
		self.away = away
		self.h_score = h_score
		self.a_score = a_score
	def __repr__(self):
		return "<Match('%r','%r','%r','%r','%r','%r')>"%(self.date,self.status,self.home,self.away,self.h_score,self.a_score)
