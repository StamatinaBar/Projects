from db import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80), unique=True)

    def __init__(self,username,password):
        self.username=username
        self.password=password


    @classmethod
    def get_by_username(cls,username):
        row=cls.query.filter_by(username=username).first()
        return row


    @classmethod
    def get_by_id(cls,_id):
        row = cls.query.filter_by(id=_id).first()
        return row


    def insert(self):
        db.session.add(self)
        db.session.commit()

