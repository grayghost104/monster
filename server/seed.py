from random import randint, choice 
# from faker import Faker
from config import app, db
from models import User, Monster, Media, Buy


# if __name__ == '__main__':
# fake = Faker()
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
m1 = Monster(
    name = "Clawdeen Wolf",
    age = 15,
    parents = "Clawrk and Harriet Wolf.",
    siblings = "Clawdia, Clawd, Howleen", 
    movies = "Monster High: New Ghoul at School, Monster High: 13 Wishes, Monster High: The Movie, Monster High: Ghouls Rule, Monster High: Welcome to Monster High, Monster High: Frights, Camera, Action!, Monster High: Great Scarrier Reef, Monster High: Haunted, Monster High: Escape from Skull Shores, Monster High: Freaky Fusion, Monster High: Friday Night Frights
    episodes = "speed dating"
    )

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

e1=Media{
    movies = "Monster High: New Ghoul at School, Monster High: Fright On, Monster High: Why Do Ghouls Fall in Love?, Monster High: Escape from Skull Shores, Monster High: Ghouls Rule!, Monster High: Friday Night Frights, Monster High: Scaris, City of Frights, Monster High: 13 Wishes, Monster High: Frights, Camera, Action!, Monster High: Freaky Fusion, Monster High: Haunted, Monster High: Boo York, Boo York, Monster High: Great Scarrier Reef"
    episodes = "Jaundice Brothers, Talon Show, Fear Squad, Substitute Creature, Party Planners, Blue Lagoona, Copy Canine, The Hot Boy, Bad Scare Day, Photo Finish, Cyrano De Ghoulia, Bad Zituation, Clawditions, Freedom Fight, Totally Busted, Freakout Friday, Mad Science Fair, Shock and Awesome, The Good, the Bat, and the Fabulous, Rumor Run Wild, Fur Will Fly, Horrorscope, Idol Threat, Hatch Me If You Can, Date of the Dead, A Scare of a Dare, Parent-Creature Conference, Scream Building, Why We Fright, Fear-a-Mid Power, Beast Friends, Varsity Boos, Gloomsday, Falling Spirits, Fatal Error, Screech to the Beach, Witch Trials, Don't Cheer the Reaper, Road to Monster Mashionals, Queen of the Scammed, Frightday the 13th, HooDoo You Like?, Fear Pressure, Fear The Book, Desperate Hours, Miss Infearmation, Hyde and Shriek, Daydream of the Dead, Nefera Again, Back-to-Ghoul, Abominable Impression, Frost Friends, Hyde Your Heart, Ghostly Gossip, Hiss-teria, Phantom of the Opry, The Bermuda Love Triangle, Here Comes Treble, Dueling Personality, Neferamore, Rising From the Dead, Monster Mashionals Part 1, Monster Mashionals Part 2, Dodgeskull, Game of DeNile, Uncommon Cold, Ghosts with Dirty Face, Hickmayleeun, No Place Like Nome, Sibling Rivalry, The Nine Lives of Toralei, Unlife to Live, Abyss Adventure, Unearthed Day, Creepfast Club, Home Ick, HooDoo That VooDoo That You Do, I Know What You Did Last Fright, Honey, I Shrunk the Ghouls, HooDude VooDoo, Undo the Voodoo, Night of a Thousand Dots (Dot Dead Gorgeous), Beast Ghoulfriend, Aba-Kiss Me Deadly, Bean Scare, Done That, A Perfect Match, Hiss-toria, The Need for Speed, The Halls Have Eyes, Mauled, Scare-born Infection, Boo Year's Eve, Franken-Styled, Defending Your Lagoona, Freaky Fridate, The Ghoulest Season, Fright Dance, Scare-itage, Tough As Scales, Tree of Unlife, No Ghouls Allowed, I Scream, You Scream, Frankie's Joltin' Juice, Tortoise and The Scare, Fierce Crush, Invasion of the Ghoul Snatchers, Flowers for Slo Mo, Slo Mo, Ready, Wheeling and Able, Creature of the Year, Party Undead, Student Disembodied President, Clawbacks, Field of Screams, Angry Ghouls, The Stich-uation, Scarah-Voyant, Inscare-itance, Playing the Boos, Department of Monster Vehicles, Royal Pest Sitter, Cookie Creeper, Crime Scream Investigation, Games Ghouls Play, Monster-morphoseas, Scream Spirit, Eye of the Boo-holder, Who's the Boo Girl?, Boo Ghoul at School, Creature Creepers Adventures, Part 1: Bat Dialing Disaster, Scream Spirit, Scareful What You Wish For, Boogey Mansion, Monsters of Music, Tales from the Script, Boolittle Too Late, Jungle Boo-gie, Just Ghost to Show Ya, Master of Hiss-guise, Zombie Shake, Just One of the Ghouls, Join the Scream, In Plain Fright, Creature Creepers Adventures, Part 2: The Coin Calamity, We Are Monster High, Creepateria, I Only Have Eye for You, So You Think You Can Date, Inner Monster 1.0, Inner Monster 2.0, Graveball Grates, Happy Howlidays, Boys Fright Out, Creature Cribs, Draculocker, Stage Frightened, Casta Vote, I Casta Spell On You, Sayonara Draculaura, Lochness Lorna, Meet You in Monster Picchu, Looks Gil-ty, The Agony of D'Feet, Gloom and Bloom, Part 1, Gloom and Bloom, Part 2, Bad Tomb-mates, Freak Du Chic, Act 1, Freak Du Chic, Act 2, Freak Du Chic, Act 3, From Fear to There, Part 1, From Fear to There, Part 2, Decomposition Class"
}
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

    