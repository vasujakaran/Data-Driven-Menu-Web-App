'''@package models
'''


from sqlalchemy import Column, ForeignKey, Integer, String
from . import database_setup



# Class
class Restaurant(database_setup.Base):
    '''
    The description of a restaurant.
    A restaurant is an entity that consists of n menuitems.

    Ideally, there should be another model called outlet.
    A restaurant should have many outlets.
    And outlets should have menu items.

    Must also have a relation (FK) to another table called cusines.
    '''
    # Table
    __tablename__ = 'restaurant'

    # Mapper
    'Primary Key'
    id = Column(Integer, primary_key=True)

    'Name of the establishment'
    name = Column(String(80), nullable=False)

    'Address of the establishment'
    address = Column(String(250), nullable=False)

    # this property is from Restaurant
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
        }



