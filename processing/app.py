from sched import scheduler
import yaml, json, connexion, logging.config, logging, sys, swagger_ui_bundle, requests, sqlalchemy, pymongo, os, sqlite3, logging#, drop_tables
#import create_tables

from db_table import db_table

from connexion import NoContent
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from apscheduler.schedulers.background import BackgroundScheduler

#drop_tables
#create_tables

#Environments
with open('app_conf.yaml', 'r') as conf:
    app_config = yaml.safe_load(conf.read())

logger = logging.getLogger('basicLogger')
logger.setLevel(logging.DEBUG)

mysql_e = app_config["mysql"]
mongo_e = app_config["mongodb"]

if not os.path.isfile('data.sqlite'):
    connection = sqlite3.connect('data.sqlite')
    c = connection.cursor()

    c.execute("""
                CREATE TABLE values
                (
                id INTEGER PRIMARY KEY ASC NOT NULL,
                info VARCHAR NOT NULL
                )
            """)

    connection.commit()
    connection.close()

BASE = declarative_base()
ENGINE = create_engine("mysql+pymysql://root:Passw0rd@mysql:33061/values") # Name of compose file
BASE.metadata.bind = ENGINE
SESSION = sessionmaker(bind=ENGINE)

MONGO_CLIENT = pymongo.MongoClient("mongodb://mongodb:27017/")

def populate():
    mysql_data = get_mysql()
    to_mongo(mysql_data)

def get_mysql():
    # Get data from MySQL
    session = SESSION()
    result = []

    # Query info
    query = session.query(db_table.info).all()

    # Gather and append
    for each in query:
        dictionary = {'info': each[0]}
        result.append(dictionary)
    
    session.close()
    return result

def to_mongo(mysql_data):
    db = MONGO_CLIENT['data']
    table = db['info']

    logger.info(MONGO_CLIENT.list_database_names())
    rep = table.find()
    print(rep)

    # For each item in info table, hash item, then insert
    for each in mysql_data:
        into = hash(str(each))
        query = {'info': str(into)}
        
        table.insert_one(query)

def scheduler():
    sch = BackgroundScheduler(daemon=True)

    sch.add_job(populate,'interval',seconds=5)

app = connexion.FlaskApp(__name__, specification_dir='')

if __name__ == "__main__":
    scheduler()
    populate()
    app.run(port=8100, use_reloader=False)