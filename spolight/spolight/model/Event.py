from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref

from spolight.model import Base
from spolight.model.Player import *
from spolight.model.Match import *

class Event(Base):
	__tablename__='event'
	id=Column(Integer,primary_key=True)
	e_type = Column(String(30))
	time = Column(DateTime)
	player_id=Column(Integer, ForeignKey(Player.id))
	match_id = Column(Integer, ForeignKey(Match.id))

	def __init__(self,e_type,time,player_id):
		self.e_type = e_type
		self.time = time
		self.player_id = player_id
		self.match_id = match_id
	def __repr__(self):
		return "<Event('%r','%r','%r','%r')>"%(self.e_type,self.time,self.player_id,self.match_id)


