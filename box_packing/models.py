from box_packing import db


# engine = create_engine('sqlite+pysqlite:///moving.db', echo=True, future=True)


class Box(db.Model):
    __tablename__ = 'boxes'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(30))
    size = db.Column('size', db.String(20))
    length = db.Column('length', db.Integer)
    width = db.Column('width', db.Integer)
    height = db.Column('height', db.Integer)
    weight_class = db.Column('weight_class', db.Integer)
    fragile = db.Column('fragile', db.Boolean, default=False)
    liquid = db.Column('liquid', db.Boolean, default=False)
    valuable = db.Column('valuable', db.Boolean, default=False)
    weather_resistant = db.Column('weather_resistant', db.Boolean, default=False)
    can_freeze = db.Column('can_freeze', db.Boolean, default=False)
    essential = db.Column('essential', db.Boolean, default=False)

    items = db.relationship('Item', back_populates='boxes')

    # def __repr__(self):
    #     return f'Box(id={self.id!r}, name={self.name!r}, size={self.size!r}'


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column('id', db.Integer, primary_key=True)
    box_id = db.Column('box_id', db.ForeignKey('boxes.id'), nullable=False)
    name = db.Column('name', db.String)
    fragile = db.Column('fragile', db.Boolean, default=False)

    boxes = db.relationship('Box', back_populates='items')

    def __repr__(self):
        return f'Item(id={self.id!r}, name={self.name!r}, box_id={self.box_id!r}, fragile={self.fragile!r}'

