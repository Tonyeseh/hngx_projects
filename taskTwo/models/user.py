import models
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

Base = declarative_base()

class User(Base):
    """Representation of a User"""
    __tablename__ = 'users'
    id = Column(String(60), primary_key=True)
    email = Column(String(128), nullable=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name, email=None):
        """initialises user"""
        self.name = name
        self.email = email
        self.id = str(uuid4())

    def to_dict(self):
        """returns the dictionary containing all key/value of an instance"""
        new_dict = self.__dict__.copy()
        #new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict['_sa_instance_state']
        return new_dict

    def save(self):
        """updates user in the database"""
        models.storage.new(self)
        models.storage.save()
        
    def delete(self):
        """deletes the current instance from storage"""
        models.storage.delete(self)
