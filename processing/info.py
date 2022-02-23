from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from base import BASE

class Info(BASE):
    __tablename__ = "info"

    #id = Column(Integer, primary_key=True)
    info = Column(String(100), primary_key=True, nullable=False)

    def __init__(self, info, username, comment, rating, created_date, trace_id):
        self.review_id = info

    def to_dict(self):
        # Sends items to dictionary
        dict = {}
        dict['info'] = self.info

        return dict