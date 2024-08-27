from random import randint, choice as rc
from faker import Faker
from app import app
from models import db

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
def create_users():
    for _ in range(10):
        user= User(
            username = fake.name(), 
            _password_hash = fake.word(), 
            fav_mon = choice(["Abbey Bominable", "Clawdeen Wolf", "Cleo de Nile", "Deuce Gorgon", "Draculaura", "Frankie Stein", "Ghoulia Yelps", "Lagoona Blue"])
        )



"Amanita Nightshade", "Andy Beast", "Ari Hauntington", "Avea Trotter", "Bonesy", "Bonita Femur", "Bram Devein", "Bridgett Rolle", "Brocko", Catrine DeMew, Catty Noir, Clawd Wolf, Crystal, Cy Clops, Dayna Treasura Jones, "Dee O'Gee", Don Ofdadead, Finnegan Wake, Gigi Gran,Gilda Goldstag, Gillington Webber, Gob, Gooliope Jellington
	Gory Fangtell
	Heath Burns
	Henry Hunchback
	Herbert East
	Holt Hyde	Hoodude Voodoo, 	Howleen Wolf	Invisi Billy, Iris Clops
	Jackie Lope
	Jackson Jekyll, Jane Boolittle, Jinafire Long, Johnny Spirit, Kipling
Kieran Valentine, 	Lothar
Manny Taur
Meowlody
	Moanica D'Kay
Neighthan Rot
	Operetta
	The Perfect Guy
	Purrsephone
	Quill Talyntino
	Raythe, 	Robecca Steam
	Rochelle Goyle
Romulus
	Rose and Blanche Van Sangre
	Scarah Screams
Silvi Timberwolf
	Simon Clops
	Sirena Von Boo
	Skelita Calaveras
	kelly, 	Sloman Mortavitch
	Spectra Vondergeist
Spelldon Cauldronello
	Teala
	Thornton
	Three Headed Freddie
Toralei Stripe
	Twyla Boogeyman
	Venus McFlytrap
	Woolee, 	Wydowna Spider

	Astranova
	Batsy Claro
	Bekka Madden
	Billy Phaidin
	Brett Redding
	Candace Carver
	Chad
	Clair
	Djinni Grant, Elle Eedee
	Fawn
	Finn, Garrott du Roque
Gary
Goons
Haylee
Honey Swamp
Isi Dawndancer
Kala Mer'ri
	Kiyomi Haunterly
	Kjersti Trollsøn
	Lilith Van Hellscream
	Lorna McNessie
	Luna Mothews
	Marisol Coxi
	Melody Carver
	Mouscedes King
	Peri and Pearl Serpentine
	Porter Geiss, Posea Reef, River Styxx, Rocco, Sansquatch, Seth Ptolemy, Thad, Thorna Thornwillow, Treesa Thornwillow, Vandala Doubloons, Viperine Gorgon, C.A. Cupid, Casta Fierce, Clawdia Wolf, Elissabat, Euna, Nefera de Nile, Victor Frankenstein, Alivia Stein, Ebbie Blue, Fangelica VanBat, Kelpie Blue
