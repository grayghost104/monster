from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy
from config import db, metadata
from sqlalchemy.orm import relationship,validates 


class SMon(db.Model, SerializerMixin):
    __tablename__='smons'
    id = db.Column(db.Integer, primary_key=True)
    monster_id = db.Column(db.Integer,db.ForeignKey("monsters.id"))
    monster = db.relationship("Monster", back_populates="smons")
    users = db.relationship('User', back_populates='smons')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class SMed(db.Model, SerializerMixin):
    __tablename__='smeds'
    id = db.Column(db.Integer, primary_key=True)
    users = db.relationship('User', back_populates='smeds')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    media_id = db.Column(db.Integer,db.ForeignKey("medias.id"))
    medias = db.relationship("Media", back_populates="smeds")

class SBu(db.Model, SerializerMixin):
    __tablename__='sbus'
    id = db.Column(db.Integer, primary_key=True)
    users = db.relationship('User', back_populates='sbus')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    buy_id = db.Column(db.Integer,db.ForeignKey("buys.id"))
    buys = db.relationship("Buy", back_populates="sbus")


class Monster(db.Model, SerializerMixin): 
    __tablename__ = 'monsters' 
    id = db.Column (db.Integer, primary_key=True) 
    name = db.Column (db.String) 
    age = db.Column (db.Integer) 
    parents = db.Column (db.String)
    siblings = db.Column(db.String)
    movies = db.Column (db.String)
    episodes = db.Column (db.String)
    smons = db.relationship("SMon", back_populates="monster", cascade = "all, delete-orphan")
    # stories = db.relationship("Story", back_populates="monster", cascade ="all, delete-orphan")
    medias = db.relationship("Media", back_populates="monster", cascade ="all, delete-orphan")
    buys = db.relationship("Buy", back_populates="monster", cascade ="all, delete-orphan")
    serialize_rules = ('-medias.monster','-smons.monster')


class Media(db.Model, SerializerMixin):
    __tablename__= 'medias' 
    id=db.Column (db.Integer, primary_key=True)
    movies = db.Column(db.String)
    episodes = db.Column(db.String)
    monster_id = db.Column(db.Integer,db.ForeignKey("monsters.id"))
    monster = db.relationship("Monster", back_populates="medias")
    smeds = db.relationship("SMed", back_populates="medias")
    serialize_rules = ('-monster.medias',)

class Buy(db.Model, SerializerMixin):
    __tablename__= 'buys' 
    id=db. Column (db.Integer, primary_key=True)
    cheapest = db.Column(db.String)
    most = db.Column(db.String)
    reliable = db.Column(db.String)
    monster_id = db.Column(db.Integer,db.ForeignKey("monsters.id"))
    monster = db.relationship("Monster", back_populates="buys")
    sbus = db.relationship("SBu", back_populates="buys")
    serialize_rules = ('-monster.buys',)


class User(db.Model, SerializerMixin):
    __tablename__= 'users' 
    id=db.Column (db.Integer, primary_key=True)
    username= db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String)
    fav_mon = db.Column(db.String)
    fav_mov = db.Column(db.String)
    smons = db.relationship("SMon", back_populates="users")
    smeds = db.relationship("SMed", back_populates="users")
    sbus = db.relationship("SBu", back_populates="users")
    serialize_rules = ()

    @validates('fav_mon') 
    def check_mon(self, key, value):
        char=["Abbey Bominable", "Clawdeen Wolf", "Cleo de Nile", "Deuce Gorgon", "Draculaura", "Frankie Stein", "Ghoulia Yelps", "Lagoona Blue", "Amanita Nightshade", "Andy Beast", "Ari Hauntington", "Avea Trotter", "Bonesy", "Bonita Femur", "Bram Devein", "Bridgett Rolle", "Brocko", "Catrine DeMew", "Catty Noir", "Clawd Wolf", "Crystal", "Cy Clops", "Dayna Treasura Jones", "Dee O'Gee", "Don Ofdadead", "Finnegan Wake", "Gigi Gran", "Gilda Goldstag", "Gillington Webber", "Gob", "Gooliope Jellington", "Gory Fangtell", "Heath Burns", "Herbert East", "Holt Hyde", "Hoodude Voodoo", "Howleen Wolf", "Invisi Billy", "Iris Clops, Jackie Lope", "Jackson Jekyll", "Jane Boolittle", "Jinafire Long", "Johnny Spirit", "Kipling", "Kieran Valentine", "Lothar", "Manny Taur", "Meowlody", "Moanica D'Kay", "Neighthan Rot", "Operetta", "Purrsephone", "Raythe", "Robecca Steam", "Rochelle Goyle", "Romulus", "Scarah Screams", "Silvi Timberwolf", "Simon Clops", "Sirena Von Boo", "Skelita Calaveras", "kelly", "Sloman Mortavitch", "Spectra Vondergeist", "Spelldon Cauldronello", "Thornton", "Toralei Stripe", "Twyla Boogeyman", "Venus McFlytrap", "Woolee", "Wydowna Spider", "Astranova", "Batsy Claro", "Djinni Grant", "Elle Eedee", "Fawn", "Finn", "Garrott du Roque", "Gary", "Haylee", "Honey Swamp", "Isi Dawndancer", "Kala Mer'ri", "Kiyomi Haunterly", "Kjersti Trollsøn", "Lorna McNessie", "Luna Mothews", "Marisol Coxi", "Mouscedes King", "Peri and Pearl Serpentine", "Porter Geiss", "Posea Reef", "River Styxx", "Rocco", "Sansquatch", "Seth Ptolemy", "Thad", "Thorna Thornwillow", "Treesa Thornwillow", "Vandala Doubloons", "Viperine Gorgon", "C.A. Cupid", "Casta Fierce", "Clawdia Wolf," "Elissabat", "Euna", "Nefera de Nile", "Victor Frankenstein", "Alivia Stein", "Ebbie Blue", "Fangelica VanBat", "Kelpie Blue"]
        if value not in char:
            raise ValueError("This monster doesnt go to monster high")
        else:
            return value
    @validates('fav_mov')
    def check_mov(self, key, value):
        movies=["Monster High: New Ghoul at School", "Monster High: Fright On", "Monster High: Why Do Ghouls Fall in Love?", "Monster High: Escape from Skull Shores", "Monster High: Ghouls Rule!", "Monster High: Friday Night Frights", "Monster High: Scaris, City of Frights", "Monster High: 13 Wishes", "Monster High: Frights, Camera, Action!", "Monster High: Freaky Fusion", "Monster High: Haunted", "Monster High: Boo York, Boo York", "Monster High: Great Scarrier Reef"]
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
# class Story(db.Model, SerializerMixin):
#     __tablename__= 'stories' 
#     id=db.Column (db.Integer, primary_key=True) 
#     origin_story= db.Column(db.String) 
#     L_book = db.Column (db.String)
#     monster_id = db.Column(db.Integer,db.ForeignKey("monsters.id"))
#     monster = db.relationship("Monster", back_populates="stories")
#     users = db.relationship('User', back_populates='stories')
#     saved = db.relationship("Saved", back_populates="stories")
#     serialize_rules = ('-monster.stories',)