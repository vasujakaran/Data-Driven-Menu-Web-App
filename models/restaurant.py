from sqlalchemy import Column, ForeignKey, Integer, String
from . import database_setup


# Class
class Restaurant(database_setup.Base):
    # Table
    __tablename__ = 'restaurant'
    # Mapper
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    address = Column(String(250), nullable=False)

    # this property is from Restaurant
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
        }



