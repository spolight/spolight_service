from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref
from spolight.model.Team import *
from spolight.model.Competition import *
from spolight.model import Base

class Team_Competition(Base):
    __tablename__ = 'team_competition'
    id = Column(Integer,primary_key=True)
    team_id = Column(Integer,ForeignKey(Team.id))
    competition_id = Column(Integer,ForeignKey(Competition.id))
    win = Column(Integer)
    draw = Column(Integer)
    lose = Column(Integer)
    point = Column(Integer)

    def __init__(self, team_id, competition_id, win, draw, lose, point) :
        self.team_id = team_id
        self.competition_id = competition_id
        self.win = win
        self.draw = draw
        self.lose = lose
        self.point = point

    def __repr__(self):
        return "<Team_Competition('%r','%r','%r','%r','%r','%r')>"%(self.team_id,self.competition_id,self.win,self.draw,self.lose,self.point)
