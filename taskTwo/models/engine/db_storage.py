import models
from dotenv import load_dotenv
from models.user import Base, User
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

load_dotenv()

class DBStorage:
    """interacts with POSTGRES database"""
    __engine = None
    __session = None

    def __init__(self) -> None:
        """initialise a DBStorage object"""
        DB_USER = getenv('DB_USER')
        DB_PWD = getenv('DB_PWD')
        DB_HOST = getenv('DB_HOST')
        DB_NAME = getenv('DB_NAME')
        DATABASE_URL = getenv('DATABASE_URL')

        #self.__engine = create_engine('postgresql+pyscopg2://{}:{}@{}/{}'.format(DB_USER, DB_PWD, DB_HOST, DB_NAME))
        self.__engine = create_engine(DATABASE_URL)
        Base.metadata.drop_all(self.__engine)

    def all(self):
        new_dict = {}
        try:
            objs = self.__session.query(User).all()
        except:
            self.reload()
            objs = self.__session.query(User).all()
        for obj in objs:
            key = obj.id
            new_dict[key] = obj
        return new_dict
    
    def new(self, obj):
        """add obj to the current database session"""
        try:
            self.__session.add(obj)
        except:
            self.reload()
            self.__session.add(obj)

    def save(self):
        """commit all changes of the cirrect database seesion"""
        try:
            self.__session.commit()
        except:
            self.reload()
            self.__session.commit()

    def delete(self, obj):
        """delete from the current database session obj"""
        try:
            self.__session.delete(obj)
        except:
            self.reload()
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def get(self, id):
        """returns the object based on its ID"""
        all_obj = models.storage.all()
        for obj in all_obj.values():
            if obj.id == id:
                return obj
            
        return None
