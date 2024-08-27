from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from config import db
from slgalchemy.orm import validates, relationship 

class All(db.Model, SerializerMixin):
    __tablename__='alls'
    id = db.Column(db.Integer, primary_key=True)
    monster_id = db.Column(db.Integer,db.ForeignKey("monsters.id"))
    story_id = db.Column(db.Integer, db.ForeignKey("stories.id"))
    media_id = db.Column(db.Integer,db.ForeignKey("medias.id"))
    buy_id = db.Column(db.Integer,db.ForeignKey("buys.id"))
    saved_id = db.Column(db.Integer, db.ForeignKey('saveds.id'))
    saved = db.relationship("Saved", back_populates="all", cascade ="all, delete-orphan")
    monster = db.relationship("Monster", back_populates="all", cascade ="all, delete-orphan")
    stories = db.relationship("Story", back_populates="all", cascade ="all, delete-orphan")
    medias = db.relationship("Media", back_populates="all", cascade ="all, delete-orphan")
    buys = db.relationship("Buy", back_populates="all", cascade ="all, delete-orphan")


class Monster(db Model, SerializerMixin): 
    __tablename__ = 'monsters' 
    id =db.Column (db.Integer, primary_key=True) 
    name = db.Column (db.String) 
    age = db.Column (db.Integer) 
    parents = db.Column (db.String)
    siblings = db.Column(db.String)
    movies = db.Column (db.String)
    episodes = db.Column (db.String) 
    save = db.Column(db.String)

    saved = db.relationship("Saved", back_populates="monster", cascade ="all, delete-orphan")
    stories = db.relationship("Story", back_populates="monster", cascade ="all, delete-orphan")
    medias = db.relationship("Media", back_populates="monster", cascade ="all, delete-orphan")
    buys = db.relationship("Buy", back_populates="monster", cascade ="all, delete-orphan")
    serialize_rules = ('-stories.monster','-medias.monster','-saved.monster')


class Story(db.Model, SerializerMixin):
    __tablename__= 'stories' 
    id=db.Column (db.Integer, primary_key=True) 
    origin_story= db.Column(db.String) 
    L_book = db.Column (db.String)
    save = db.Column(db.String)

    monster_id = db.Column(db.Integer,db.ForeignKey("monsters.id"))
    monster = db.relationship("Monster", back_populates="stories", cascade ="all, delete-orphan")
    saved = db.relationship("Saved", back_populates="stories", cascade ="all, delete-orphan")
    serialize_rules = ('-monster.stories','-saved.monster')



class Media(db.Model, SerializerMixin):
    __tablename__= 'medias' 
    id=db.Column (db.Integer, primary_key=True)
    channels = db.Column(db.String)
    sites = db.Column(db.String)
    movies = db.Column(db.String)
    episodes = db.Column(db.String)
    save = db.Column(db.String)

    monster_id = db.Column(db.Integer,db.ForeignKey("monsters.id"))
    monster = db.relationship("Monster", back_populates="medias",cascade ="all, delete-orphan")
    saved = db.relationship("Saved", back_populates="medias", cascade ="all, delete-orphan")
    serialize_rules = ('-monster.medias','-saved.monster')

class Buy(db.Model, SerializerMixin):
    __tablename__= 'buys' 
    id=db. Column (db.Integer, primary_key=True)
    cheapest = db.Column(db.String)
    most = db.Column(db.String)
    reliable = db.Column(db.String)
    save = db.Column(db.String)

    monster_id = db.Column(db.Integer,db.ForeignKey("monsters.id"))
    monster = db.relationship("Monster", back_populates="buys", cascade ="all, delete-orphan")
    saved = db.relationship("Saved", back_populates="monster", cascade ="all, delete-orphan")
    serialize_rules = ('-monster.buys','-saved.monster')



    

class Saved(db.Model, SerializerMixin):
    __tablename__= 'saveds' 
    id=db.Column (db.Integer, primary_key=True)
    buying = db.Column(db.String)
    watching = db.Column(db.String)
    mon = db.Column(db.String)
    story = db.Column(db.String)
    users = db.relationship('User', back_populates='saveds', cascade = 'all, delete-orphan')



class Info(db.Model, SerializerMixin):
    __tablename__='infos'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='infos', cascade = 'all, delete-orphan')
    saved_id = db.Column(db.Integer, db.ForeignKey('saveds.id'))
    saved = db.relationship('Saved', back_populates='infos', cascade = 'all delete-orphan')


class User(db.Model, SerializerMixin):
    __tablename__= 'users' 
    id=db.Column (db.Integer, primary_key=True)
    username= db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String)
    fav_mon = db.Column(db.String)
    fav_mov = db.Column(db.String)
    save = db.Column(db.String)
    saveds = db.relationship("Saved", back_populates="users", cascade ="all, delete-orphan")
    serialize_rules = ()

    @validates('fav_mov')
    def check_mov(self, value):
        movies=[" Monster High: New Ghoul at School", "Monster High: Fright On", "Monster High: Why Do Ghouls Fall in Love?", "Monster High: Escape from Skull Shores", " Monster High: Ghouls Rule!", " Monster High: Friday Night Frights", ". Monster High: Scaris, City of Frights", " Monster High: 13 Wishes", "Monster High: Frights, Camera, Action!", "Monster High: Freaky Fusion", "Monster High: Haunted", " Monster High: Boo York, Boo York", "Monster High: Great Scarrier Reef"]
        for i in value:
            if i not in movies:
                raise ValueError("This isnt a monster high movie")
        return value


    @hybrid_property
    def password(self):
        return self._password
    @password.setter
    def password(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password = password_hash.decode('utf-8')
    def authenticate(self,password):
        return bcrypt.check_password_hash(self._password, password.encode('utf-8'))

    @validates('username')
    def check_username(self, key, value):
        if type(value) is str and 0<value=>10:
            return value
        else:
            raise ValueError('Not a vaild username')
