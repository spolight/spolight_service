from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref

from spolight.model import Base

class League(Base):
	__tablename__='league'
	id=Column(Integer,primary_key=True)
	l_type=Column(String(30))
	title=Column(String(100))
	country=Column(String(100))

	def __init__(self,l_type,title,country):
		self.l_type=l_type
		self.title=title
		self.country=country
	def __repr__(self):
		return "<League('%r','%r','%r')>"%(self.l_type,self.title,self.country)
