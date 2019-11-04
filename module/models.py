from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'moms'
    mid = Column(String(12), primary_key = True)
    name = Column(String(3), unique = False)
    birthday = Column(Integer, unique = False)
    lucky = Column(Integer, unique = False)


    def __init__(self, mid = None, name = None, birthday = None, lucky = None):
        self.mid = mid    
        self.name = name
        self.birthday = birthday
        self.lucky = lucky
   

    def __repr__(self):
        return '<User %r>' % (self.mid)


