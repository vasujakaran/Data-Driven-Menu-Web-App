from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .restaurant import Restaurant
from . import database_setup

# Class
class MenuItem(database_setup.Base):
    # Table
    __tablename__ = 'menu_item'
    # Mapper
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    # this property is from MenuItem
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'course': self.course
        }


