from db import db

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(80), unique=True)
    capital = db.Column(db.String(80), unique=True)


    def __init__(self,country,capital):
        self.country=country
        self.capital=capital

    def json(self):
        return {"country": self.country,"capital": self.capital}

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_name(cls,name):
        row = cls.query.filter_by(country=name).first()
        return row