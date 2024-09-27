from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_bcrypt import Bcrypt
# from dotenv import load_dotenv
import os

# Local imports
# load_dotenv()
# Instantiate app, set attributes
app = Flask(__name__,
    static_url_path='',
    static_folder='../client/build',
    template_folder='../client/build'
)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your_monster_high_user:p4Gg8Zd5PDPGyE1vALYljJo5G5cRjLOJ@dpg-crpidrdsvqrc738rmpdg-a.oregon-postgres.render.com/your_monster_high'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Define metadata, instantiate db
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
      "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "pk": "pk_%(table_name)s"
})
db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)
db.init_app(app)
app.secret_key= ('\xcf]i\xae\n\xcf\x8d\xd74_X\x8e"\x17\xa9\x05')
# app.secret_key = os.getenv('SECRET_KEY')
# Instantiate REST API
api = Api(app)
bcrypt = Bcrypt(app)
CORS(app)
