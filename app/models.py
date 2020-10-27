import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, request, url_for
from flask_login import UserMixin, AnonymousUserMixin
from . import db, login_manager
from sqlalchemy import desc



class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

class User(UserMixin, db.Model):

    """ Nesta classe estam defenidos os utilizadores do BO"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    id_hubspot=db.Column(db.Integer, unique=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id')) # nao esta em uso
    password_hash = db.Column(db.String(128))
    

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """esta funcao recebe o objecto user(que está na base de dados) e compara a pass"""
        return check_password_hash(self.password_hash, password)



    @property
    def pin(self):
        raise AttributeError('password is not a readable attribute')

    @pin.setter
    def pin(self, pin):
        self.pin_hash = generate_password_hash(pin)

    def verify_pin(self, password):
        """esta funcao recebe o objecto user(que está na base de dados) e compara a pass"""
        return check_password_hash(self.pin_hash, password)



    def generate_auth_token(self, expiration):
        s = Serializer(current_app.config['SECRET_KEY'],expires_in=expiration)
        return s.dumps({'id': self.id}).decode('utf-8')

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        if data.get('confirm') != self.id:
            return True
        self.confirmed = True
        db.session.add(self)
        return True
    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])




    def to_json(self):
        """esta funcao recebe um objecto to tipo user -> devolve em formato json o dados do utilizador """
        json_user = {
            'url': url_for('api.get_user', id=self.id),
            'username': self.username

        }
        return json_user






    def __repr__(self):
        return '<User %r>' % self.username

class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return True

    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer(), primary_key=True)
    id_zomato = db.Column(db.Integer())
    id_hubspot= db.Column(db.Integer())
    url=db.Column(db.String(128))
    addTime = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    name=db.Column(db.String(128))
    address=db.Column(db.String(128))
    city=db.Column(db.String(128))
    latitude=db.Column(db.String(128))
    longitude=db.Column(db.String(128))
    locality=db.Column(db.String(128))
    zipcode=db.Column(db.String(128))
    price_range=db.Column(db.String(128))
    all_reviews_count=db.Column(db.String(128))
    average_cost_for_two=db.Column(db.String(128))
    phone_numbers=db.Column(db.String(128))
    cuisines=db.Column(db.String(128))
    average_cost_for_two=db.Column(db.String(128))

    def __repr__(self):
        return '<Restaurant %r>' % self.restaurant


