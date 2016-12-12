import datetime

import flask_sqlalchemy


db = flask_sqlalchemy.SQLAlchemy()


class BaseModel(object):
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def rollback(self):
        db.session.rollback()


class UserRequest(db.Model, BaseModel):
    __tablename__ = 'user_request'

    id = db.Column(db.Integer, primary_key=True)
    user_ip = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, user_ip):
        self.user_ip = user_ip

    def __repr__(self):
        return f'<UserRequest {self.user_ip}>'
