from sched import scheduler
import yaml, json, connexion, logging.config, logging, sys, swagger_ui_bundle, requests, sqlalchemy, pymongo, hashlib#, drop_tables
#import create_tables

from connexion import NoContent
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from apscheduler.schedulers.background import BackgroundScheduler

#drop_tables
#create_tables

#Environments
with open('app+conf.yaml', 'r') as conf:
    app_config = yaml.safe_load(conf.read())

mysql_e = app_config["mysql"]
mongo_e = app_config["mongodb"]

BASE = declarative_base()
ENGINE = create_engine("mysql+pymysql://Jordan:Password@mysql/data") # Name of compose file
BASE.metadata.bind = ENGINE
SESSION = sessionmaker(bind=ENGINE)

MONGO_CLIENT = pymongo.MongoClient("mongodb://host.docker.internal:27017")

def populate():
    mysql_data = get_mysql()
    to_mongo(mysql_data)

def get_mysql():
    # Get data from MySQL
    session = SESSION()
    result = []

    # Query info
    query = session.query(data.info).all()

    # Gather and append
    for each in query:
        dictionary = {'info': each[0]}
        result.append(dictionary)
    
    session.close()
    return result

def to_mongo(mysql_data):
    db = MONGO_CLIENT[mongo_e['data']]
    table = db[mongo_e['info']]

    # For each item in info table, hash item, then insert
    for each in mysql_data:
        into = hash(each)
        query = {'info': str(into)}
        table.update_one(query)

def scheduler():
    sch = BackgroundScheduler(daemon=True)

    sch.add_job(populate,'interval',seconds=5)

app = connexion.FlaskApp(__name__, specification_dir='')

if __name__ == "__main__":
    scheduler()
    app.run(port=8100, use_reloader=False)