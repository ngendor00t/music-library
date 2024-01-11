from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///music.db')
    Session = sessionmaker(bind=engine)
    session = Session()


    import ipdb; ipdb.set_trace()
