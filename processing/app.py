import yaml, json, connexion, logging.config, logging, sys, swagger_ui_bundle, requests, sqlalchemy, pymongo, hashlib#, drop_tables
#import create_tables

from connexion import NoContent
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#drop_tables
#create_tables

BASE = declarative_base()
ENGINE = create_engine("mysql+pymysql://Jordan:Password@mysql/data") # Name of compose file
BASE.metadata.bind = ENGINE
SESSION = sessionmaker(bind=ENGINE)

def process():

    # Get data from MySQL
    session = SESSION()
    
    var = session.query(info).first()

    # Hash value
    count = hash(var)

    # Open MongoDB session
    client = pymongo.MongoClient("mongodb://host.docker.internal:27017")
    db = client["data"] # Select database
    col = db["info"]# Select table

    x = col.insert_one(count) # Insert hash into table

app = connexion.FlaskApp(__name__, specification_dir='')

if __name__ == "__main__":

    app.run(port=8100, use_reloader=False)