from app import db
from datetime import datetime

class customer(db.Model):
    custID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(32), nullable=False)
    address = db.Column(db.String(128), nullable=False)
    suburb = db.Column(db.String(64), nullable=False)
    orders = db.relationship('order', backref='orderingCust', lazy='dynamic')

    def __repr__(self):
        return '<Customer {}>'.format(self.name)

class driver(db.Model):
    driverID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    vehicle = db.Column(db.String(64), nullable=False)
    orders = db.relationship('order', backref='placedWithDriver', lazy='dynamic')

    def __repr__(self):
        return '<Driver {}>'.format(self.name)

class order(db.Model):
    orderID = db.Column(db.Integer, primary_key=True)
    custID = db.Column(db.Integer, db.ForeignKey(customer.custID), nullable=False)
    driverID = db.Column(db.Integer, db.ForeignKey(driver.driverID))
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ready = db.Column(db.Boolean, nullable=False, default=0)
    total = db.Column(db.Integer, nullable=False, default=0)
    quantities = db.relationship('quantity', backref='quantityAdded', lazy='dynamic')

    def __repr__(self):
        return '<Order {}>'.format(self.orderID)

class item(db.Model):
    itemID = db.Column(db.Integer, primary_key=True)
    decsription = db.Column(db.String(128), nullable=False)
    cost = db.Column(db.Integer, nullable=False, default=0)
    items = db.relationship('quantity', backref='itemAdded', lazy='dynamic')

    def __repr__(self):
        return '<Item {}>'.format(self.decsription)

class quantity(db.Model):
    itemID = db.Column(db.Integer, db.ForeignKey(item.itemID), primary_key=True)
    orderID = db.Column(db.Integer, db.ForeignKey(order.orderID), primary_key=True)
    quantity = db.Column(db.Integer)

    def __repr__(self):
        return '<Quantity {}>'.format(self.name)