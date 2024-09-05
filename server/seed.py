from random import randint, choice 
# from faker import Faker
from config import app, db
from models import User, Monster, Media, Buy
import itertools
from flask import Flask, render_template, request, jsonify
import requests 
from bs4 import BeautifulSoup 



# if __name__ == '__main__':
# fake = Faker()
main = User(username="gray_ghost", password_hash= "kittenlove", fav_mon= "Lagoona Blue", fav_mov="Monster High Why Do Ghouls Fall in Love?")
main2 = User(username="isis", password_hash= "evan", fav_mon= "Draculaura", fav_mov="Monster High Why Do Ghouls Fall in Love?")
# def create_users():
#     for _ in range(10):
#         user= User(
#             username = fake.name(), 
#             password = fake.word(), 
# "Abbey Bominable", "Clawdeen Wolf", "Cleo de Nile", "Deuce Gorgon", "Draculaura", "Frankie Stein", "Ghoulia Yelps", "Lagoona Blue","Jinafire Long", "Robecca Steam","Heath Burns","Invisi Billy"
#             fav_mon = choice(["Abbey Bominable", "Clawdeen Wolf", "Cleo de Nile", "Deuce Gorgon", "Draculaura", "Frankie Stein", "Ghoulia Yelps", "Lagoona Blue", "Amanita Nightshade", "Andy Beast", "Ari Hauntington", "Avea Trotter", "Bonesy", "Bonita Femur", "Bram Devein", "Bridgett Rolle", "Brocko", "Catrine DeMew", "Catty Noir", "Clawd Wolf", "Crystal", "Cy Clops", "Dayna Treasura Jones", "Dee O'Gee", "Don Ofdadead", "Finnegan Wake", "Gigi Gran", "Gilda Goldstag", "Gillington Webber", "Gob", "Gooliope Jellington", "Gory Fangtell", "Heath Burns", "Herbert East", "Holt Hyde", "Hoodude Voodoo", "Howleen Wolf", "Invisi Billy", "Iris Clops, Jackie Lope", "Jackson Jekyll", "Jane Boolittle", "Jinafire Long", "Johnny Spirit", "Kipling", "Kieran Valentine", "Lothar", "Manny Taur", "Meowlody", "Moanica D'Kay", "Neighthan Rot", "Operetta", "Purrsephone", "Raythe", "Robecca Steam", "Rochelle Goyle", "Romulus", "Scarah Screams", "Silvi Timberwolf", "Simon Clops", "Sirena Von Boo", "Skelita Calaveras", "kelly", "Sloman Mortavitch", "Spectra Vondergeist", "Spelldon Cauldronello", "Thornton", "Toralei Stripe", "Twyla Boogeyman", "Venus McFlytrap", "Woolee", "Wydowna Spider", "Astranova", "Batsy Claro", "Djinni Grant", "Elle Eedee", "Fawn", "Finn", "Garrott du Roque", "Gary", "Haylee", "Honey Swamp", "Isi Dawndancer", "Kala Mer'ri", "Kiyomi Haunterly", "Kjersti Trollsøn", "Lorna McNessie", "Luna Mothews", "Marisol Coxi", "Mouscedes King", "Peri and Pearl Serpentine", "Porter Geiss", "Posea Reef", "River Styxx", "Rocco", "Sansquatch", "Seth Ptolemy", "Thad", "Thorna Thornwillow", "Treesa Thornwillow", "Vandala Doubloons", "Viperine Gorgon", "C.A. Cupid", "Casta Fierce", "Clawdia Wolf," "Elissabat", "Euna", "Nefera de Nile", "Victor Frankenstein", "Alivia Stein", "Ebbie Blue", "Fangelica VanBat", "Kelpie Blue"])
#             fav_mov = choice(["Monster High: New Ghoul at School", "Monster High: Fright On", "Monster High: Why Do Ghouls Fall in Love?", "Monster High: Escape from Skull Shores", "Monster High: Ghouls Rule!", "Monster High: Friday Night Frights", "Monster High: Scaris, City of Frights", "Monster High: 13 Wishes", "Monster High: Frights, Camera, Action!", "Monster High: Freaky Fusion", "Monster High: Haunted", "Monster High: Boo York, Boo York", "Monster High: Great Scarrier Reef"])
#         )
#     db.session.add(user)
m1 = Monster(
    name = "Jinafire Long",
    age = 1500,
    parents = "Japanese human and Chinese dragons",
    movies = ""
    )
m2 = Monster(
    name= "Abbey Bominable",
    age = 16,
    parents = "Tundra Bominable and the Abominable Snowman",
    movies = ""
    )
m3 = Monster(
    name = "Clawdeen Wolf",
    age = 15,
    parents = "Clawrk and Harriet Wolf.",
    movies = "" 
    # ["Monster High New Ghoul at School", "Monster High Fright On", "Monster High Why Do Ghouls Fall in Love?", "Monster High Escape from Skull Shores", "Monster High Ghouls Rule!", "Monster High Friday Night Frights", "Monster High Scaris City of Frights", "Monster High 13 Wishes", "Monster High Frights Camera Action!", "Monster High Freaky Fusion", "Monster High Haunted", "Monster High Boo York Boo York", "Monster High Great Scarrier Reef"]
    )
m4 = Monster(
    name = "Robecca Steam",
    age = 116,
    parents = "Hexiciah Steam",
    movies = "" 
    # ["Monster High New Ghoul at School", "Monster High Fright On", "Monster High Why Do Ghouls Fall in Love?", "Monster High Escape from Skull Shores", "Monster High Ghouls Rule!", "Monster High Friday Night Frights", "Monster High Scaris City of Frights", "Monster High 13 Wishes", "Monster High Frights Camera Action!", "Monster High Freaky Fusion", "Monster High Haunted", "Monster High Boo York Boo York", "Monster High Great Scarrier Reef"]
    )
m5 = Monster(
    name = "Cleo de Nile",
    age = 5842,
    parents = "Mummy",
    movies = "" 
    # ["Monster High New Ghoul at School", "Monster High Fright On", "Monster High Why Do Ghouls Fall in Love?", "Monster High Escape from Skull Shores", "Monster High Ghouls Rule!", "Monster High Friday Night Frights", "Monster High Scaris City of Frights", "Monster High 13 Wishes", "Monster High Frights Camera Action!", "Monster High Freaky Fusion", "Monster High Haunted", "Monster High Boo York Boo York", "Monster High Great Scarrier Reef"]
    )
m6 = Monster(
    name = "Deuce Gorgon",
    age = 15,
    parents = "Medusa",
    movies = "" 
    # ["Monster High New Ghoul at School", "Monster High Fright On", "Monster High Why Do Ghouls Fall in Love?", "Monster High Escape from Skull Shores", "Monster High Ghouls Rule!", "Monster High Friday Night Frights", "Monster High Scaris City of Frights", "Monster High 13 Wishes", "Monster High Frights Camera Action!", "Monster High Freaky Fusion", "Monster High Haunted", "Monster High Boo York Boo York", "Monster High Great Scarrier Reef"]
    )
m7 = Monster(
    name = "Draculaura",
    age = 1600,
    parents = "Dracula",
    movies = "" 
    # ["Monster High New Ghoul at School", "Monster High Fright On", "Monster High Why Do Ghouls Fall in Love?", "Monster High Escape from Skull Shores", "Monster High Ghouls Rule!", "Monster High Friday Night Frights", "Monster High Scaris City of Frights", "Monster High 13 Wishes", "Monster High Frights Camera Action!", "Monster High Freaky Fusion", "Monster High Haunted", "Monster High Boo York Boo York", "Monster High Great Scarrier Reef"]
    )
m8 = Monster(
    name = "Frankie Stein",
    age = 15,
    parents = "Viktor and Viveka Stein",
    movies = "" 
    # ["Monster High New Ghoul at School", "Monster High Fright On", "Monster High Why Do Ghouls Fall in Love?", "Monster High Escape from Skull Shores", "Monster High Ghouls Rule!", "Monster High Friday Night Frights", "Monster High Scaris City of Frights", "Monster High 13 Wishes", "Monster High Frights Camera Action!", "Monster High Freaky Fusion", "Monster High Haunted", "Monster High Boo York Boo York", "Monster High Great Scarrier Reef"]
    )
m9 = Monster(
    name = "Ghoulia Yelps",
    age =  16,
    parents = "Hairy and Hellen Yelps",
    movies = "" 
    # ["Monster High New Ghoul at School", "Monster High Fright On", "Monster High Why Do Ghouls Fall in Love?", "Monster High Escape from Skull Shores", "Monster High Ghouls Rule!", "Monster High Friday Night Frights", "Monster High Scaris City of Frights", "Monster High 13 Wishes", "Monster High Frights Camera Action!", "Monster High Freaky Fusion", "Monster High Haunted", "Monster High Boo York Boo York", "Monster High Great Scarrier Reef"]
    )
m10 = Monster(
    name = "Lagoona Blue",
    age = 16,
    parents = "Wade Blue and Angel Fisher",
    movies = "" 
    # ["Monster High New Ghoul at School", "Monster High Fright On", "Monster High Why Do Ghouls Fall in Love?", "Monster High Escape from Skull Shores", "Monster High Ghouls Rule!", "Monster High Friday Night Frights", "Monster High Scaris City of Frights", "Monster High 13 Wishes", "Monster High Frights Camera Action!", "Monster High Freaky Fusion", "Monster High Haunted", "Monster High Boo York Boo York", "Monster High Great Scarrier Reef"]
    )
m11 = Monster(
    name = "Heath Burns",
    age = 15,
    parents = "Greek fire elemental mother and Korean hearth fire demi-god",
    movies = "" 
    # ["Monster High New Ghoul at School", "Monster High Fright On", "Monster High Why Do Ghouls Fall in Love?", "Monster High Escape from Skull Shores", "Monster High Ghouls Rule!", "Monster High Friday Night Frights", "Monster High Scaris City of Frights", "Monster High 13 Wishes", "Monster High Frights Camera Action!", "Monster High Freaky Fusion", "Monster High Haunted", "Monster High Boo York Boo York", "Monster High Great Scarrier Reef"]
    )
m12 = Monster(
    name = "Invisil Billy",
    age = 15,
    parents = "Invisible Man",
    movies = "" 
    # ["Monster High New Ghoul at School", "Monster High Fright On", "Monster High Why Do Ghouls Fall in Love?", "Monster High Escape from Skull Shores", "Monster High Ghouls Rule!", "Monster High Friday Night Frights", "Monster High Scaris City of Frights", "Monster High 13 Wishes", "Monster High Frights Camera Action!", "Monster High Freaky Fusion", "Monster High Haunted", "Monster High Boo York Boo York", "Monster High Great Scarrier Reef"]
    )
def news():
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=monster+high+dolls+g1&_sacat=0&_odkw=monster+high+dolls&_osacat=0'
    response = requests.get(url)
    if response.status_code == 200:
        soup= BeautifulSoup(response.text, "html.parser")
        ebay = []
        d1 = soup.find('li', id="item5a1575ea09")
        d2 = soup.find('li', id="item36e246057f")
        d3 = soup.find('li', id="item2b5908a6f9")
        d4 = soup.find('li', id="item2b62d9c3a3")
        d5 = soup.find('li', id="item26def8c1df")
        d6 = soup.find('li', id="item472fe7ed45")
        ebay.append(d1)
        ebay.append(d2)
        ebay.append(d3)
        ebay.append(d4)
        ebay.append(d5)
        ebay.append(d6)
        for i in itertools.zip_longest(ebay, fillvalue=""):
            print(type(i))
            buy = Buy(
                dolls = str(i)
            )
            db.session.add(buy)
def create_media():
    movie = ["Monster High New Ghoul at School", "Monster High Fright On", "Monster High Why Do Ghouls Fall in Love?", "Monster High Escape from Skull Shores", "Monster High Ghouls Rule!", "Monster High Friday Night Frights", "Monster High Scaris City of Frights", "Monster High 13 Wishes", "Monster High Frights Camera Action!", "Monster High Freaky Fusion", "Monster High Haunted", "Monster High Boo York Boo York", "Monster High Great Scarrier Reef"]
    episode = ["Jaundice Brothers", "Talon Show", "Fear Squad", "Substitute Creature", "Party Planners", "Blue Lagoona", "Copy Canine", "The Hot Boy", "Bad Scare Day", "Photo Finish", "Cyrano De Ghoulia", "Bad Zituation", "Clawditions", "Freedom Fight", "Totally Busted", "Freakout Friday", "Mad Science Fair", "Shock and Awesome", "The Good, the Bat, and the Fabulous", "Rumor Run Wild", "Fur Will Fly", "Horrorscope", "Idol Threat", "Hatch Me If You Can", "Date of the Dead", "A Scare of a Dare", "Parent-Creature Conference", "Scream Building", "Why We Fright", "Fear-a-Mid Power", "Beast Friends", "Varsity Boos", "Gloomsday", "Falling Spirits", "Fatal Error", "Screech to the Beach", "Witch Trials", "Don't Cheer the Reaper", "Road to Monster Mashionals", "Queen of the Scammed", "Frightday the 13th", "HooDoo You Like?", "Fear Pressure", "Fear The Book", "Desperate Hours", "Miss Infearmation", "Hyde and Shriek", "Daydream of the Dead", "Nefera Again", "Back-to-Ghoul", "Abominable Impression", "Frost Friends", "Hyde Your Heart", "Ghostly Gossip", "Hiss-teria", "Phantom of the Opry", "The Bermuda Love Triangle", "Here Comes Treble", "Dueling Personality", "Neferamore", "Rising From the Dead", "Monster Mashionals Part 1", "Monster Mashionals Part 2", "Dodgeskull", "Game of DeNile", "Uncommon Cold", "Ghosts with Dirty Face", "Hickmayleeun", "No Place Like Nome", "Sibling Rivalry", "The Nine Lives of Toralei", "Unlife to Live", "Abyss Adventure", "Unearthed Day", "Creepfast Club", "Home Ick", "HooDoo That VooDoo That You Do", "I Know What You Did Last Fright", "Honey", "I Shrunk the Ghouls", "HooDude VooDoo", "Undo the Voodoo", "Night of a Thousand Dots (Dot Dead Gorgeous)", "Beast Ghoulfriend", "Aba-Kiss Me Deadly", "Bean Scare", "Done That", "A Perfect Match", "Hiss-toria", "The Need for Speed", "The Halls Have Eyes", "Mauled", "Scare-born Infection", "Boo Year's Eve", "Franken-Styled", "Defending Your Lagoona", "Freaky Fridate", "The Ghoulest Season", "Fright Dance", "Scare-itage", "Tough As Scales", "Tree of Unlife", "No Ghouls Allowed", "I Scream", "You Scream", "Frankie's Joltin' Juice", "Tortoise and The Scare", "Fierce Crush", "Invasion of the Ghoul Snatchers", "Flowers for Slo Mo", "Slo Mo", "Ready", "Wheeling and Able", "Creature of the Year", "Party Undead", "Student Disembodied President", "Clawbacks", "Field of Screams", "Angry Ghouls", "The Stich-uation", "Scarah-Voyant", "Inscare-itance", "Playing the Boos", "Department of Monster Vehicles", "Royal Pest Sitter", "Cookie Creeper", "Crime Scream Investigation", "Games Ghouls Play", "Monster-morphoseas", "Scream Spirit", "Eye of the Boo-holder", "Who's the Boo Girl?", "Boo Ghoul at School", "Creature Creepers Adventures", "Part 1: Bat Dialing Disaster", "Scream Spirit", "Scareful What You Wish For", "Boogey Mansion", "Monsters of Music", "Tales from the Script", "Boolittle Too Late", "Jungle Boo-gie", "Just Ghost to Show Ya", "Master of Hiss-guise", "Zombie Shake", "Just One of the Ghouls", "Join the Scream", "In Plain Fright", "Creature Creepers Adventures", "Part 2: The Coin Calamity", "We Are Monster High", "Creepateria", "I Only Have Eye for You", "So You Think You Can Date", "Inner Monster 1.0", "Inner Monster 2.0", "Graveball Grates", "Happy Howlidays", "Boys Fright Out", "Creature Cribs", "Draculocker", "Stage Frightened", "Casta Vote", "I Casta Spell On You", "Sayonara Draculaura", "Lochness Lorna", "Meet You in Monster Picchu", "Looks Gil-ty", "The Agony of D'Feet", "Gloom and Bloom, Part 1", "Gloom and Bloom, Part 2", "Bad Tomb-mates", "Freak Du Chic, Act 1", "Freak Du Chic, Act 2", "Freak Du Chic, Act 3", "From Fear to There, Part 1", "From Fear to There, Part 2", "Decomposition Class"]
    for i,e in itertools.zip_longest(movie,episode, fillvalue=""):
        media = Media(
            movies = i, 
            episodes = e
        )
        db.session.add(media)
if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")
        db.session.query(Monster).delete()
        db.session.query(Media).delete()
        db.session.query(Buy).delete()
        db.session.query(User).delete()
        db.session.add_all([m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,main, main2])
        create_media()
        news()
        db.session.commit()
        print("Deleting Customers")

        # create_users()

    