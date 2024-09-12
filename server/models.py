from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy
from config import db, metadata, bcrypt
from sqlalchemy.orm import relationship,validates 



class Monster(db.Model, SerializerMixin): 
    __tablename__ = 'monsters' 
    id = db.Column (db.Integer, primary_key=True) 
    name = db.Column (db.String) 
    age = db.Column (db.Integer) 
    parents = db.Column (db.String)
    movies = db.Column (db.String)
    img = db.Column (db.String)
    friends = db.Column (db.String)
    enemies = db.Column (db.String)
    medias = db.relationship("Media", back_populates="monster")
    buys = db.relationship("Buy", back_populates="monster")
    stories = db.relationship("Story", back_populates="monster")
    serialize_rules = ('-medias.monster','-users.monsters')

class Story(db.Model, SerializerMixin):
    __tablename__= 'stories' 
    id=db.Column (db.Integer, primary_key=True)
    mon_name = db.Column(db.String) 
    origin_story= db.Column(db.String) 
    L_book = db.Column (db.String)
    monster_id = db.Column(db.Integer,db.ForeignKey("monsters.id"))
    monster = db.relationship("Monster", back_populates="stories")
    serialize_rules = ('-monster.stories',)


class Media(db.Model, SerializerMixin):
    __tablename__= 'medias' 
    id=db.Column (db.Integer, primary_key=True)
    movies = db.Column(db.String)
    episodes = db.Column(db.String)
    monster_id = db.Column(db.Integer,db.ForeignKey("monsters.id"))
    monster = db.relationship("Monster", back_populates="medias")
    # users = db.relationship('User', secondary="smeds", back_populates='medias')
    # smeds = db.relationship("SMed", back_populates="media")
    serialize_rules = ('-monster.medias',)

class Buy(db.Model, SerializerMixin):
    __tablename__= 'buys' 
    id=db. Column (db.Integer, primary_key=True)
    dolls = db.Column(db.String)
    monster_id = db.Column(db.Integer,db.ForeignKey("monsters.id"))
    monster = db.relationship("Monster", back_populates="buys")
    # users = db.relationship('User', secondary='sbus', back_populates='buys')
    # sbus = db.relationship("SBu", back_populates="buys")
    serialize_rules = ('-monster.buys',)


class User(db.Model, SerializerMixin):
    __tablename__= 'users' 
    id=db.Column (db.Integer, primary_key=True)
    username= db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String)
    fav_mon = db.Column(db.String)
    fav_mov = db.Column(db.String)
    # buys = db.relationship("Buy", secondary='sbus', back_populates="users")
    # monsters = db.relationship("Monster", secondary='smons', back_populates='users')
    # medias = db.relationship("Media", secondary="smeds", back_populates="users")
    # smons = db.relationship("SMon", back_populates="user")
    # smeds = db.relationship("SMed", back_populates="user")
    # sbus = db.relationship("SBu", back_populates="user")
    # serialize_rules = ('-monsters.users')

    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash,password.encode('utf-8'))

    @validates('password')
    def check_pass(self,key,value):
        if 0>=value>=8:
            return value
        else:
            raise ValueError("Make your password longer")

    @validates('fav_mon') 
    def check_mon(self, key, value):
        char=["Abbey Bominable", "Clawdeen Wolf", "Cleo de Nile", "Deuce Gorgon", "Draculaura", "Frankie Stein", "Ghoulia Yelps", "Lagoona Blue","Jinafire Long", "Robecca Steam","Heath Burns","Invisi Billy"]
            # "Abbey Bominable", "Clawdeen Wolf", "Cleo de Nile", "Deuce Gorgon", "Draculaura", "Frankie Stein", "Ghoulia Yelps", "Lagoona Blue", "Crystal", "Cy Clops", "Dayna Treasura Jones", "Dee O'Gee", "Don Ofdadead", "Finnegan Wake", "Gigi Gran", "Gilda Goldstag", "Gillington Webber", "Gob", "Gooliope Jellington", "Gory Fangtell", "Heath Burns", "Herbert East", "Holt Hyde", "Hoodude Voodoo", "Howleen Wolf", "Invisi Billy", "Iris Clops, Jackie Lope", "Jackson Jekyll", "Jane Boolittle", "Jinafire Long", "Johnny Spirit", "Kipling", "Kieran Valentine", "Lothar", "Manny Taur", "Meowlody", "Moanica D'Kay", "Neighthan Rot", "Operetta", "Purrsephone", "Raythe", "Robecca Steam", "Rochelle Goyle", "Romulus", "Scarah Screams", "Silvi Timberwolf", "Simon Clops", "Sirena Von Boo", "Skelita Calaveras", "kelly", "Sloman Mortavitch", "Spectra Vondergeist", "Spelldon Cauldronello", "Thornton", "Toralei Stripe", "Twyla Boogeyman", "Venus McFlytrap", "Woolee", "Wydowna Spider", "Astranova", "Batsy Claro", "Djinni Grant", "Elle Eedee", "Fawn", "Finn", "Garrott du Roque", "Haylee", "Honey Swamp", "Isi Dawndancer", "Kala Mer'ri", "Kiyomi Haunterly", "Kjersti Trollsøn", "Lorna McNessie", "Luna Mothews", "Marisol Coxi", "Mouscedes King", "Peri and Pearl Serpentine", "Porter Geiss", "Posea Reef", "River Styxx", "Rocco", "Sansquatch", "Seth Ptolemy", "Thad", "Thorna Thornwillow", "Treesa Thornwillow", "Vandala Doubloons", "Viperine Gorgon", "C.A. Cupid", "Casta Fierce", "Clawdia Wolf," "Elissabat", "Euna", "Nefera de Nile", "Victor Frankenstein", "Alivia Stein", "Ebbie Blue", "Fangelica VanBat", "Kelpie Blue"]
        if value not in char:
            raise ValueError("This monster doesnt go to monster high")
        else:
            return value
    @validates('fav_mov')
    def check_mov(self, key, value):
        movies=["Monster High New Ghoul at School", "Monster High Fright On", "Monster High Why Do Ghouls Fall in Love?", "Monster High Escape from Skull Shores", "Monster High Ghouls Rule!", "Monster High Friday Night Frights", "Monster High Scaris City of Frights", "Monster High 13 Wishes", "Monster High Frights Camera Action!", "Monster High Freaky Fusion", "Monster High Haunted", "Monster High Boo York Boo York", "Monster High Great Scarrier Reef"]
        if value not in movies:
            raise ValueError("This isnt a monster high movie")
        else:
            return value

    # @validates('username')
    # def check_username(self, value):
    #     if type(value) is str:
    #         return value
    #     else:
    #         raise ValueError('Not a vaild username')









# class SSto(db.Model, SerializerMixin):
#     __tablename__='sstos'
#     id = db.Column(db.Integer, primary_key=True)
#     saved_id = db.Column(db.Integer, db.ForeignKey('saveds.id'))
#     saved = db.relationship("Saved", back_populates="sstos")
#     story_id = db.Column(db.Integer, db.ForeignKey("stories.id"))
#     stories = db.relationship("Story", back_populates="sstos")

# class SMon(db.Model, SerializerMixin):
#     __tablename__='smons'
#     monster_id = db.Column('monster_id', db.Integer, db.ForeignKey("monsters.id"), primary_key=True)
#     user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
#     monster = db.relationship("Monster", back_populates="smons")
#     user = db.relationship("User", back_populates="smons")


# class SMed(db.Model, SerializerMixin):
#     __tablename__='smeds'
#     user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
#     media_id = db.Column('media_id', db.Integer,db.ForeignKey("medias.id"), primary_key=True)
#     user = db.relationship("User", back_populates="smeds")
#     media = db.relationship("Media", back_populates="smeds")


# class SBu(db.Model, SerializerMixin):
#     __tablename__='sbus'
#     user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
#     buy_id = db.Column('buy_id', db.Integer,db.ForeignKey("buys.id"), primary_key=True)
#     user = db.relationship("User", back_populates="sbus")
#     buys = db.relationship("Buy", back_populates="sbus")