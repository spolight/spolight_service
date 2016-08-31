from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref

from spolight.model import Base

class Player(Base):
	__tablename__ = 'player'

	id = Column(Integer, primary_key=True)
	name = Column(String(100))
	birth = Column(DateTime)
	country = Column(String(100))
	foot = Column(Integer)
	weight = Column(Integer)
	height = Column(Integer)
	position = Column(Integer)
	# many to many : Player <-> Team_Competition
	team_competition=relationship('Team_Competition', secondary='Player_TeamCompetition', backref='player')

	def __init__(self,name,birth,country,foot,weight,height,position):
		self.name=name
		self.birth=birth
		self.country=country
		self.foot = foot
		self.weight = weight
		self.height=height
		self.position=position

	def __repr__(self):
		return "<Player('%r','%r','%r','%r','%r','%r','%r')>"%(self.name,self.brith,self.country,self.foot,self.weight,self.height,self.position)


