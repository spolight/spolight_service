from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

__all__ = ['Player','Match','League','Event','Competition','Team','Team_Competition','Player_TeamCompetition']

