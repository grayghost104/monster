from random import randint, choice 
# from faker import Faker
from config import app, db
from models import User, Monster, Media, Buy


# if __name__ == '__main__':
# fake = Faker()



m1 = Monster(
    name = "Clawdeen Wolf",
    age = 17,
    parents = "Your mom",
    siblings = "Cladwolf", 
    movies = "monster high",
    episodes = "speed dating"
    )
m2 = Monster(
    name= "Abbey Bominable",
    age = 19,
    parents = "scary snowman",
    siblings = "icles",
    movies = "frosty the snowman",
    episodes = "heth burns"
    )
main = User(username="gray_ghost", password= "kittenlove", fav_mon= "Lagoona Blue", fav_mov="Monster High: Why Do Ghouls Fall in Love?")
main2 = User(username="isis", password= "evan", fav_mon= "Draculaura", fav_mov="Monster High: Why Do Ghouls Fall in Love?")
# def create_users():
#     for _ in range(10):
#         user= User(
#             username = fake.name(), 
#             password = fake.word(), 
#             fav_mon = choice(["Abbey Bominable", "Clawdeen Wolf", "Cleo de Nile", "Deuce Gorgon", "Draculaura", "Frankie Stein", "Ghoulia Yelps", "Lagoona Blue", "Amanita Nightshade", "Andy Beast", "Ari Hauntington", "Avea Trotter", "Bonesy", "Bonita Femur", "Bram Devein", "Bridgett Rolle", "Brocko", "Catrine DeMew", "Catty Noir", "Clawd Wolf", "Crystal", "Cy Clops", "Dayna Treasura Jones", "Dee O'Gee", "Don Ofdadead", "Finnegan Wake", "Gigi Gran", "Gilda Goldstag", "Gillington Webber", "Gob", "Gooliope Jellington", "Gory Fangtell", "Heath Burns", "Herbert East", "Holt Hyde", "Hoodude Voodoo", "Howleen Wolf", "Invisi Billy", "Iris Clops, Jackie Lope", "Jackson Jekyll", "Jane Boolittle", "Jinafire Long", "Johnny Spirit", "Kipling", "Kieran Valentine", "Lothar", "Manny Taur", "Meowlody", "Moanica D'Kay", "Neighthan Rot", "Operetta", "Purrsephone", "Raythe", "Robecca Steam", "Rochelle Goyle", "Romulus", "Scarah Screams", "Silvi Timberwolf", "Simon Clops", "Sirena Von Boo", "Skelita Calaveras", "kelly", "Sloman Mortavitch", "Spectra Vondergeist", "Spelldon Cauldronello", "Thornton", "Toralei Stripe", "Twyla Boogeyman", "Venus McFlytrap", "Woolee", "Wydowna Spider", "Astranova", "Batsy Claro", "Djinni Grant", "Elle Eedee", "Fawn", "Finn", "Garrott du Roque", "Gary", "Haylee", "Honey Swamp", "Isi Dawndancer", "Kala Mer'ri", "Kiyomi Haunterly", "Kjersti Trollsøn", "Lorna McNessie", "Luna Mothews", "Marisol Coxi", "Mouscedes King", "Peri and Pearl Serpentine", "Porter Geiss", "Posea Reef", "River Styxx", "Rocco", "Sansquatch", "Seth Ptolemy", "Thad", "Thorna Thornwillow", "Treesa Thornwillow", "Vandala Doubloons", "Viperine Gorgon", "C.A. Cupid", "Casta Fierce", "Clawdia Wolf," "Elissabat", "Euna", "Nefera de Nile", "Victor Frankenstein", "Alivia Stein", "Ebbie Blue", "Fangelica VanBat", "Kelpie Blue"])
#             fav_mov = choice(["Monster High: New Ghoul at School", "Monster High: Fright On", "Monster High: Why Do Ghouls Fall in Love?", "Monster High: Escape from Skull Shores", "Monster High: Ghouls Rule!", "Monster High: Friday Night Frights", "Monster High: Scaris, City of Frights", "Monster High: 13 Wishes", "Monster High: Frights, Camera, Action!", "Monster High: Freaky Fusion", "Monster High: Haunted", "Monster High: Boo York, Boo York", "Monster High: Great Scarrier Reef"])
#         )
#     db.session.add(user)
if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")
        print("Deleting Customers")
        db.session.query(Monster).delete()
        db.session.query(Media).delete()
        db.session.query(Buy).delete()
        db.session.query(User).delete()
        db.session.add_all([m1,m2, main, main2])
        db.session.commit()
        # create_users()

    