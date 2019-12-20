#!/usr/bin/python3
"""This is the state class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade='all, delete')

    @property
    def cities(self):
        """Getter attritube
        Return:
        list of City instances with state_id equals 
        to the current State.id
        """
        cities = []
        obj_dict = storage.all(City)
        keys = obj_dict.keys()

        for key in keys:
            if self.id in keys:
                cities.append(obj_dict[key])
        
        return cities
