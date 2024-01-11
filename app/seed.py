from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Artist,Album,Song


if __name__ == '__main__':
    
    engine = create_engine('sqlite:///music.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Song).delete()
    session.query(Album).delete()
    session.query(Artist).delete()

    fake = Faker()

    #add songs
    artists=[]
    for i in range(4):
       artist = Artist(
           name=fake.name(),
           gender=fake.gender(),
        )
       session.add(artist)
       artists.append(artist)
    session.commit()



    songs=[]
    for i in range(4):
       song=Song(
          name=fake.name(),
          year_realesed=fake.year_realesed(),
        
        )
       session.add(song)
       session.append(song)
    session.commit()  
    

    


    albmus=[]
    for i in range(4):
       album=Album(
          name=fake.name(),
          numbe_of_songs=fake.number_of_songs(),

       )
       session.add(album)
       session.append(album)
    session.commit()   


    



