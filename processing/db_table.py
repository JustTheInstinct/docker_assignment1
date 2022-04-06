from tkinter import Variable
from xmlrpc.client import Boolean
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime
from base import BASE

class db_table(BASE):
    __tablename__ = "values"

    id = Column(Integer, primary_key=True)
    info = Column(String, nullable=False)

    def __init__(self, info):
        self.item = info

    def to_dict(self):
        # Sends items to dictionary
        dict = {}
        dict['info'] = self.info

        return dict
