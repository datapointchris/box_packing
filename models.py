from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Box(Base):
    __tablename__ = 'boxes'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(30))
    size = Column('size', String(10))
    length = Column('length', Integer)
    width = Column('width', Integer)
    height = Column('height', Integer)
    weight_class = Column('weight_class', Integer)
    fragile = Column('fragile', Boolean, default=False)
    liquid = Column('liquid', Boolean, default=False)
    valuable = Column('valuable', Boolean, default=False)
    weather_resistant = Column('weather_resistant', Boolean, default=False)

    items = relationship('Items', back_populates='boxes')

    def __repr__(self):
        return f'Box(id={self.id!r}, name={self.name!r}, size={self.size!r}'


class Item(Base):
    __tablename__ = 'items'

    id = Column('id', Integer, primary_key=True)
    box_id = Column('box_id', ForeignKey('boxes.id'), nullable=False)
    name = Column('name', String)
    fragile = Column('fragile', Boolean, default=False)

    boxes = relationship('Boxes', back_populates='items')

    def __repr__(self):
        return f'Item(id={self.id!r}, name={self.name!r}, box_id={self.box_id!r}'
