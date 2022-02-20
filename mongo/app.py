import yaml, json, connexion, logging.config, logging, sys, swagger_ui_bundle, requests, sqlalchemy, pymongo, hashlib#, drop_tables
#import create_tables

from connexion import NoContent
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#drop_tables
#create_tables

with open('app_conf.yaml', 'r') as f:
    app_config = yaml.safe_load(f.read())

BASE = declarative_base()
ENGINE = create_engine("mysql+pymysql://admin:potato@localhost/data")
BASE.metadata.bind = ENGINE
SESSION = sessionmaker(bind=ENGINE)

def process():

    # Get data from MySQL
    session = SESSION()
    
    var = session.query(info).first()

    count = hash(var)

    # Open MongoDB session
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["data"]
    col = db["info"]

    x = col.insert_one(count)

app = connexion.FlaskApp(__name__, specification_dir='')

if __name__ == "__main__":

    app.run(port=8100, use_reloader=False)