from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref

from spolight.model import Base

class Team(Base):
	__tablename__='team'

	id = Column(Integer, primary_key=True)
	name = Column(String(100))
	founded=Column(String(100))
	coach=Column(String(100))

	# many to many: Team <->Competition
	competitions = relationship('Competition',secondary='Team_Competition',backref='team')

	def __init__(self,name,founded,coach):
		self.name=name
		self.founded=founded
		self.coach=coach
	def __repr__(self):
		return "<Team('%r','%r','%r')>"%(self.name,self.founded,self.coach)

