from sqlalchemy import Column, Integer, String ,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship,backref


engine = create_engine('sqlite:///music.db')

Base = declarative_base()

class Artist(Base):
    __tablename__ ='artists'

    id = Column(Integer() , primary_key=True)
    name = Column(String())
    gender = Column(String())
    




    def __repr__(self):
        pass
 
 
 
 
    
class Album(Base):
    __tablename__='albums'


    id = Column(Integer() ,primary_key=True)
    name = Column(String())
    number_of_songs = Column(Integer)
    songs = relationship('Song', back_populates='album')
    


    
    

 
    def __repr__(self):
        return f'album(id={self.id},' + \
            f'name={self.name},'+\
            f'song_id={self.song_id})'




class Song(Base):
    __tablename__= 'songs'

    id = Column(Integer() , primary_key=True)
    name = Column(String())
    year_realesed = Column(Integer())

    artist_id = Column(Integer, ForeignKey('artists.id'))
    artist = relationship('Artist', back_populates='songs')
    
    album_id = Column(Integer, ForeignKey('albums.id'))
    album = relationship('Album', back_populates='songs')


    
    def __repr_(self):
        return f"song{self.id}:"\
          +f"{self.name},"\
          +f'artist_id={self.artist_id}'
            


