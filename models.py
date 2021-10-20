from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey

engine = create_engine('sqlite+pysqlite:///:memory:', echo=True, future=True)
metadata = MetaData()

boxes_table = Table(
    'boxes',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('size', String(10)),
    Column('length', Integer),
    Column('width', Integer),
    Column('height', Integer),
    Column('weight_class', Integer),
    Column('fragile', Boolean),
    Column('liquid', Boolean),
    Column('valuable', Boolean),
    Column('weather_resistant', Boolean)
)

items_table = Table(
    'items',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('box_id', ForeignKey('boxes.id'), nullable=False),
    Column('name', String),
    Column('fragile', Boolean)
)

