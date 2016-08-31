from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship, backref
from spolight.model.Player import *
from spolight.model.Team_Competition import *
from spolight.model import Base

class Player_TeamCompetition(Base):
    __tablename__ = 'player_teamcomp'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer,ForeignKey(Player.id))
    teamcomp_id = Column(Integer,ForeignKey(Team_Competition.id))
    goal = Column(Integer)
    asis = Column(Integer)
    foul = Column(Integer)
    transdate = Column(Date)
    value = Column(Float)

    def __init__(self,team_id,teamcomp_id,goal,asis,foul,transdate,value):
        self.player_id = player_id
        self.teamcomp_id = teamcomp_id
        self.goal = goal
        self.asis = asis
        self.foul = foul
        self.transdate = transdate
        self.value = value

    def __repr__(self):
        return "<Player_TeamComp('%r',%r','%r','%r','%r','%r','%r')>"%(self.player_id,self.teamcomp_id,self.goal,self.asis,self.foul,self.transdate,self.value)
