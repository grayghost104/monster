from random import randint, choice 
from config import app, db
from models import User, Monster, Media, Buy, Story
import itertools
from flask import Flask, render_template, request, jsonify
import requests 
from bs4 import BeautifulSoup 
import json

main = User(username="gray_ghost", password_hash= "kittenlove", fav_mon= "Lagoona Blue", fav_mov="Monster High Why Do Ghouls Fall in Love?")
main2 = User(username="isis", password_hash= "evan", fav_mon= "Draculaura", fav_mov="Monster High Why Do Ghouls Fall in Love?")

movies_str = json.dumps([
    "Monster High New Ghoul at School",
    "Monster High Fright On",
    "Monster High Why Do Ghouls Fall in Love?",
    "Monster High Escape from Skull Shores",
    "Monster High Ghouls Rule!",
    "Monster High Friday Night Frights",
    "Monster High Scaris City of Frights",
    "Monster High 13 Wishes",
    "Monster High Frights Camera Action!",
    "Monster High Freaky Fusion",
    "Monster High Haunted",
    "Monster High Boo York Boo York",
    "Monster High Great Scarrier Reef"])
Jina_str = json.dumps(['Clawdeen Wolf', 'Skelita Calaveras', 'Catrine DeMew', 'Robecca Steam', 'Heath Burns', 'Marisol Coxi'])
m1 = Monster(
    name = "Jinafire Long",
    age = 1500,
    parents = "Japanese human and Chinese dragons",
    movies = movies_str,
    friends = Jina_str,
    img = "https://i.ebayimg.com/images/g/4jgAAOSwcJxl-Huo/s-l1200.jpg",
    enemies = ""
    )
Abb_str = json.dumps(["Frankie Stein", "Lagoona Blue", "Marisol Coxi", "Headless Headmistress Bloodgood", "Draculaura", "Clawdeen Wolf", "Heath Burns" , "Ricky", "Ghoulia Yelps","Cleo de Nile", "Clawd Wolf", "Howleen Wolf", "C.A. Cupid", "Catty Noir"])
Ey_str = json.dumps(["Toralei Stripe", "Purresphone", "Meowlody", "C.A. Cupid", "Manny Taur", "Andy Beast", "Bartleby Farnum", "Lilith Van Hellscream", "New Salem Sheriff", "Moanatella Ghostier","Kieran Valentine"])
m2 = Monster(
    name= "Abbey Bominable",
    age = 16,
    parents = "Tundra Bominable and the Abominable Snowman",
    movies= movies_str,
    img = "https://m.media-amazon.com/images/I/614awBAhPVL.jpg",
    friends = Abb_str,
    enemies = Ey_str
    )
Claw_str = json.dumps(["Draculaura", "Frankie Stein", "Ghoulia Yelps", "Abbey Bominable", "Lagoona Blue", "Deuce Gorgon", "Cleo de Nile", "Spectra Vondergiest", "Jackson Jekyll", "Holt Hyde", "Melody Carver", "Toralei Stripe"])
Deen_str = json.dumps(["Cleo de Nile (Fashion Nemesis; Formerly)", "Nefera de Nile", "Manny Taur"])
m3 = Monster(
    name = "Clawdeen Wolf",
    age = 15,
    parents = "Clawrk and Harriet Wolf.",
    movies = movies_str,
    img = "https://i.ebayimg.com/images/g/Z6UAAOSw0e9U1o34/s-l1200.jpg",
    friends = Claw_str,
    enemies = Deen_str
    )
Rob_str = json.dumps(["Venus McFlytrap", "Rochelle Goyle", "Frankie Stein", "Draculaura", "Elissabat", "Finnegan Wake", "Operetta", "Ghoulia Yelps", "Cy Clops "])
Ec_str = json.dumps(["Lord Stoker", "Creature 4.0" ])
m4 = Monster(
    name = "Robecca Steam",
    age = 116,
    parents = "Hexiciah Steam",
    movies = movies_str,
    img = "https://m.media-amazon.com/images/I/81PA-XqAMzL._AC_UF894,1000_QL80_.jpg",
    friends = Rob_str,
    enemies = Ec_str
   )
CL_str = json.dumps(["Ghoulia Yelps", "Deuce Gorgon", "Draculaura", "Clawdeen Wolf", "Frankie Stein", "Lagoona Blue ", "Heath Burns", "Abbey Bominable", "Clawd Wolf", "Spectra Vondergeist", "Melody Carver", "Catty Noir", "Avea Trotter", "Bonita Femur", "Neighthan Rot", "Sirena Von Boo", "Jinafire Long", "Twyla Boogeyman"])
Eo_str = json.dumps(["Toralei Stripe", "Purrsephone", "Meowlody", "Nefera de Nile (Arch-Nemesis)", "Gory Fangtell", "Andy Beast", "Bartleby Farnum", "Kieran Valentine", "Lilith Van Hellscream", "Lilith's goons ", "Gary", "Rocco", "Djinni Grant", "Amanita Nightshade", "Neighthan Rot","Creature 4.0","Stoker","Moanatella Ghostier"] )
m5 = Monster(
    name = "Cleo de Nile",
    age = 5842,
    parents = "Mummy",
    movies = movies_str,
    img = "https://m.media-amazon.com/images/I/71N74VNOibL._AC_UF894,1000_QL80_.jpg",
    friends = CL_str,
    enemies = Eo_str
    )
De_str = json.dumps(["Heath Burns", "Clawd Wolf", "Jackson Jekyll"])
m6 = Monster(
    name = "Deuce Gorgon",
    age = 15,
    parents = "Medusa",
    movies = movies_str,
    img = "https://m.media-amazon.com/images/I/61EYMnDPb2L.jpg",
    friends = De_str,
    enemies = "" 
    )
Dr_str = json.dumps(["Clawdeen Wolf", "Frankie Stein", "Lagoona Blue", "Cleo de Nile", "Ghoulia Yelps", "Heath Burns", "Deuce Gorgon", "Clawd Wolf", "Abbey Bominable", "Spectra Vondergiest", "Howleen Wolf", "Twyla Boogeyman", "Elissabat", "Jackson Jekyll", "Holt Hyde", "Melody Carver", "Operetta", "Hoodude Voodoo", "Catty Noir", "Seth Ptolemy", "Gigi Grant", "Madison Fear", "Clawdia Wolf ", "Viperine Gorgon", "Honey Swamp ", "Hexiciah Steam", "Robecca Steam", "Venus McFlytrap", "Rochelle Goyle", "Gillington Webber", "Avea Trotter", "Bonita Femur", "Neighthan Rot", "Sirena Von Boo", "Victor Frankenstein", "Kiyomi Haunterly", "River Styxx", "Porter Geiss", "Vandala Doubloons", "Sloman Mortavitch", "Astranova", "Elle Eedee", "Luna Mothews", "Mouscedes King", "Kala Merri", "Posea Reef"])
Acu_str = json.dumps(["Cleo de Nile", "Nefera de Nile", "Toralei Stripe", "Purrsephone", "Meowlody", "Kieran Valentine", "Gary", "Rocco", "Bartleby Farnum", "Andy Beast", "Lilith Van Hellscream", "Liliths goons", "Moanatella Ghostier", "Djinni Grant", "Amanita Nightshade", "Gory Fangtell", "Lord Stoker", "Creature 4.0", "Principal Revenant", "Kala Mer'ri"])
m7 = Monster(
    name = "Draculaura",
    age = 1600,
    parents = "Dracula",
    movies =  movies_str,
    img = "https://i.ebayimg.com/images/g/RiUAAOSwiR5lW5ZG/s-l1600.jpg",
    friends = Dr_str, 
    enemies = Acu_str
    )
Fran_str = json.dumps(["Draculaura", "Clawdeen Wolf", "Lagoona Blue", "Cleo de Nile", "Ghoulia Yelps", "Abbey Bominable","Heath Burns", "Deuce Gorgon","Jackson Jekyll", "Holt Hyde", "Melody Carver", "Brett Redding", "Operetta", "Hoodude Voodoo ", "Scarah Screams", "Spectra Vondergeist", "Venus McFlytrap", "Rochelle Goyle", "Gillington Webber", "Sloman Mortavitch", "Headmistress Bloodgood", "Toarlei Stripe", "Catty Noir", "Hexiciah Steam", "Robecca Steam", "Avea Trotter", "Bonita Femur", "Sirena Von Boo", "Neighthan Rot", "Kala Mer'ri"])
Kie_str = json.dumps(["Cleo de Nile", "Toralei Stripe", "Purresphone", "Meowlody","Manny Taur","Nefera de Nile","Bartleby Farnum","Lilith Van Hellscream", "Lilith's goons","Andy Beast","Dijnni Grant","Creature 4.0","Kala Mer'ri"])
m8 = Monster(
    name = "Frankie Stein",
    age = 15,
    parents = "Viktor and Viveka Stein",
    movies =  movies_str,
    img = "https://creations.mattel.com/cdn/shop/files/fps9qdk0xof4hz8joei2_ee5b6115-16fd-4a78-9d95-7dbf27e98d32.jpg?v=1718925454",
    friends = Fran_str, 
    enemies = Kie_str
    )
Ghou_str = json.dumps(["Cleo de Nile", "Clawdeen Wolf", "Draculaura", "Frankie Stein", "Clawd Wolf", "Deuce Gorgon", "Sloman Mortavitch", "Abbey Bominable", "Lagoona Blue","Kjersti Trollsøn","Don Ofdadead","Jackson Jekyll", "Holt Hyde","Robecca Steam","Victor Frankenstein","Rochelle Goyle","Gigi Grant","Catty Noir"])
Lia_str = json.dumps(["Cleo de Nile", "Toralei Stripe", "Purrsephone", "Meowlody","Amanita Nightshade","Nefera de Nile","Manny Taur","Kieran Valentine","Bartleby Farnum","Andy Beast","Rocco","Gary","Lilith Van Hellscream","Lilith's goons","Djinni Grant","Stoker","Creature 4.0","Principal Revenant"])
m9 = Monster(
    name = "Ghoulia Yelps",
    age =  16,
    parents = "Hairy and Hellen Yelps",
    movies =  movies_str,
    img = "https://m.media-amazon.com/images/I/714BR88IRzL._AC_UF894,1000_QL80_.jpg",
    friends = Ghou_str,
    enemies = Lia_str
    )
Lago_str = json.dumps(["Gillington Webber","Sirena Von Boo","Kala Mer'ri","Cleo de Nile","Frankie Stein","Clawdeen Wolf","Draculaura","Spectra Vondergeist","Abbey Bominable","Ghoulia Yelps","Lorna McNessie","Venus McFlytrap","Kala Mer'ri"])
Ona_str = json.dumps(["Toralei Stripe", "Purrsephone", "Meowlody", "Kieran Valentine", "Bartleby Farnum", "Andy Beast","Kala Mer'ri","Amanita Nightshade"])
m10 = Monster(
    name = "Lagoona Blue",
    age = 16,
    parents = "Wade Blue and Angel Fisher",
    movies =  movies_str,
    img = "https://i5.walmartimages.com/seo/Monster-High-Lagoona-Blue-Doll-Collectible-Reproduction-in-Original-Look-with-Diary-Doll-Stand_ca33767a-ae05-4a98-9d91-40e104d88de9.12b4bb645febd33d46f30b97243a9e7c.jpeg",
    friends = Lago_str,
    enemies = Ona_str
    )
Hea_str = json.dumps([" Clawd Wolf", "Deuce Gorgon", "Manny Taur", "Slo Mo","Ghoulia Yelps"])
m11 = Monster(
    name = "Heath Burns",
    age = 15,
    parents = "Greek fire elemental mother and Korean hearth fire demi-god",
    movies =  movies_str,
    img = "https://3.bp.blogspot.com/-CDvaP2hJnr0/VuqMpfiZMeI/AAAAAAAAh6c/gRUyuR-dYEkALNllaI9RXvWmztM9zgAWw/s800/Classroom-Abbey-Heath-2-pack-1-Heath.jpg",
    friends = Hea_str,
    enemies = "" 
    )
m12 = Monster(
    name = "Invisi Billy",
    age = 15,
    parents = "Invisible Man",
    movies =  movies_str,
    img = "https://down-br.img.susercontent.com/file/br-11134201-23010-ma8i06rpvfmv96",
    friends = "Scarah Screams",
    enemies = "" 
    )

s1=Story(
    mon_name='Jinafire Long',
    origin_story= '''In China, the depiction of the dragon (traditional:龍;simplified:龙) can be found in artifacts from the Shang and Zhou dynasties, with examples dating back to the 16th century BC. Archaeologist Zhōu Chong-Fa believes that the Chinese word for dragon is an onomatopoeia of the sound thunder makes. The Chinese name for dragon is pronounced "lóng" in Mandarin Chinese or "lùhng" in Cantonese. Sometime after the 9th century AD, Japan adopted the Chinese dragon through the spread of Buddhism. ''', 
    L_book = '''There are five distinguishable dragons in the Monster High universe: Jinafire Long and Sylphia Flapper, who are sapient dragons, and Smokey, the Facebook dragon, and the pool dragon, who are pet dragons. There is also a dragon included in the Create-A-Monster lineup. It is known that most dragon characters have the ability to breath fire unlike in both Asian and European myths of dragons. According to Ghoulfriends Forever, European dragons are inherently scale- and tailless, but they have a deep desire to own a lair. The Deep End is also connected to a lair within the catacombs where a dragon resides that regulates the pool's temperature.'''
)
s2=Story(
    mon_name='Abbey Bominable',
    origin_story= '''The Yeti, often referred to as the "Abominable Snowman," is a legendary creature from Himalayan folklore. This mythical being is said to inhabit the remote, snow-covered regions of the mountains, particularly in Nepal and Tibet.Described as a large, ape-like creature, the Yeti has eluded adventurers and cryptozoology enthusiasts. Reports of footprints, sightings and local stories contribute to the beast's mystique and speculation in popular culture.''', 
    L_book= '''In G1 Monster High, the first hominid to be introduced properly was Abbey Bominable. Like yetis in myths, Abbey used to live in a colder area, and she even has ice powers that only yetis have, while her cousin Marisol Coxi, a sasquatch, has no ice powers. Abbey and Marisol's family relation confirms that yetis and sasquatches can be related. Sasquatches live in warmer areas, as shown where Marisol lives.'''
) 
s3=Story(
    mon_name='Clawdeen Wolf',
    origin_story= '''Werewolf, in European folklore, a man who turns into a wolf at night and devours animals, people, or corpses but returns to human form by day. Some werewolves change shape at will; others, in whom the condition is hereditary or acquired by having been bitten by a werewolf, change shape involuntarily, under the influence of a full moon. If he is wounded in wolf form, the wounds will show in his human form and may lead to his detection. Belief in werewolves is found throughout the world. The psychiatric condition in which a person believes he is a wolf is called lycanthropy. In countries in which wolves are not common, the monster may assume the form of another dangerous animal, such as the bear, tiger, or hyena. In French folklore, the werewolf is called loup-garou. France was particularly afflicted with reports of them in the 16th century, and there were many notable convictions and executions of loups-garous. As a subject for 20th-century horror films, the werewolf tradition is second only to the vampire tradition in popularity. Werewolves are believed to turn into vampires after death.''', 
    L_book= ''' Clawdeen has a Brooklyn accent. Her middle name is Lucia. In the books, her human identity nickname is the human spelling Claudine, without Wolf's family name at the end.'''
)
s4=Story(
    mon_name='Robecca Stream',
    origin_story= '''There are total of five robots in Monster High: Otto Maton, Robecca Steam, Captain Penny, Scareantino and Elle Eedee. Both Hexiciah Steam and Sid Borg have robotic components, but are cyborgs. Otto and Elle function by electricity. Robecca, Dracubecca, Captain Penny and Hexiciah are steam-powered. Scareantino is a clockwork-type robot. The only thing known about Sid is that he functions with the aid of pistons, so he's neither clockwork nor runs on electricity. Robots also have free will and can express emotion.''', 
    L_book= '''A robot is a type of simulacrum with a few definitions of its own. Robots are usually made of metal, but organic components fall within the definition too. One thing that clearly sets robots apart from other simulacrums is that they have an internal system explaining their working rather than owing their selves to magic or divine approval. Related to this is that a robot does not have to be sapient or even sentient to be a robot, unlike other kinds of simulacrums. If the internal system exists, it doesn't have to possess the awareness to be a robot, although that raises the question of what separates robots from other kinds of machines. Usually, this border relies on the complexity of tasks the machine is capable of and how close its form is to an organic design.'''
)
s5=Story(
    mon_name='Cleo de Nile',
    origin_story ='''Sure, there had been literary works about living mummies before cinema embraced the concept (including a short story by that wacky nutty-funster, Conan Doyle), but the creature as we know it was based on the real-life Curse of the Pharaohs. Prolific author Nina Wilcox Putnam and story editor Richard Schayer wrote a nine-page treatment for a Universal film about historical occultist Alessandro Cagliostro, which was handed over to John L. Balderston for an Egyptian makeover. Though Balderston is best known for his contributions to Dracula and Frankenstein, he covered the opening of Tut’s tomb for the aforementioned New York World. His experience informed his writing and gave us 1932’s The Mummy, the film that spawned a thousand TP-covered terrors. Much like the jinx that plagued Carter and his associates, the archaeological expedition of the film awakened a supernatural force from history. However, that supernatural force comes in the form of Imhotep (played by the uncanny Boris Karloff), the formerly mummified Egyptian high priest. While death does indeed come to those who disturb ancient powers, the titular Mummy seeks his reincarnated lover, not revenge. Despite being the progenitor of the modern mummy myth, The Mummy bears little resemblance to the films that followed. Perhaps most jarring to a modern viewer is that the Mummy only appears in his iconic wrappings at the very beginning of the picture: after a prologue of sorts, the Mummy spends the film disguised as a modern (yet desiccated) Egyptian. Unlike subsequent shamblers, this Mummy is rather articulate and doesn’t brutishly strangle folks. ''',
    L_book= '''The Monster High mummies are Mr. Mummy and the De Nile family, consisting of at least of Cleo de Nile, Nefera de Nile, and their father Ramses de Nile. Referred to in the Dawn of the Dance diaries and on Facebook is the girls' uncle Tut, and the Monster High book series make mention of an aunt named Nefertiti, while the Ghoulfriends books refer to an aunt named Neferia.The De Nile residence in the USA. Cleo de Nile is roughly 5,842 years old and her sister Nefera roughly 5,845 years. This means that in the Monster High universe, Ancient Egypt and its mummification practices kicked off well before they did in the real world. The De Niles are a royal family which lost its throne due to betrayal by people the family trusted.[1] This presumably led to the family being mummified and entombed for nearly 6,000 years, from which Cleo emerged with a severe case of fear of the dark. There is a small suggestion that the De Niles weren't constantly entombed and occasionally traveled abroad, but this is not confirmed. At some point in the third millenium CE, Cleo's father had the family leave their tomb and relocate to the Boonited States of Scaremerica, where the family's daughters came to attend Monster High. As far as Cleo and Nefera are concerned, neither of them wear much bandages as they have flawless skin (Nefera's birth-scar excluded). This is roughly in line with Imhotep from Universal's The Mummy, but also many other mummies in fiction, who all rely more on magic to preserve them than actual preservation techniques. Given the De Niles affinity with magic, this is not unlikely. However, the girls do need to wear some wrappings at all times or else they will disappear into dust.[4] This too is a classic mummy trait. They also both have a glass-breaking scream, though it's not known whether that is a mummy skill or is theirs for another reason.
Both Cleo and Nefera have a weak spot for reptiles, which in both their cases is inspired by Ancient Egyptians' use of the Egyptian cobra as symbol of royalty. Specifically, the trait originated with Cleo, whose affinity with snakes is inspired by the real-life Cleopatra's association with snakes following her choice to use one as means of honorable suicide. At least Cleo can command snakes to do her bidding, though she makes a point out of not ever using her powers on her gorgon boyfriend, Deuce Gorgon. Cleo's and Deuce's relationship is also a play on the real-life Cleopatra's association with snakes. In the books, Cleo received her pet cobra, Hissette, from Deuce, who obtained her from his mother as her first grey hair. In the diary continuity, Hissette came with a shipment from the De Niles' Egyptian home. In the webisodes, the De Niles have a pond containing crocodiles in front of their house. In addition to snakes, Nefera likes bugs, and has a pet scarab named Azura. In Ancient Egypt, scarabs were associated with the sun gods Khepri and Ra due to the way they rolled a ball forth too and seemingly created themselves from dead matter as well. Nefera is also a bit of a cat enthusiast, another animal sacred to the Ancient Egyptians, which is why she is friends of sorts with the werecats Toralei Stripe, Purrsephone, and Meowlody. In the books, there are seven cats in the De Nile household: Chisisi, Bastet, Akins, Ebonee, Ufa, Usi, and Miu-Miu.
Cleo's and Nefera's father originally carried the implication of being either Imhotep or Kharis due to the association of the main characters with the Universal Horror line-up. The name in the books aside, too many details about the girls' father has since surfaced for him to be either. Ramses de Nile is a stern man who believes in his family's superiority over commoners and insists they behave worthy of their heritage. This doesn't mean Mr. De Nile is an unpleasant person: he specifically does not allow any in his family to treat the servants badly and is very supportive of his daughters' career choices. However, he does expect both his daughters to work hard to be worthy of his support and does not want them to lose their sense of decorum in public. In the books, he is an antique dealer, while Cleo's student file reveals that he is the chairman of the MH construction committee and oversees all new building plans.
Cleo de Nile is strongly based on the real-life Cleopatra. Aside from the snake theme, Cleo's student file mentions she excels in Dead Languages. The real-life Cleopatra was the only one in her family to ever bother to learn another language than Ancient Greek, and she mastered some ten languages if not more. In contrast, Nefera doesn't appear to be modeled after a particular pharaoh but to be a mixture. Nefera's name, emphasized beauty and blue hair in a high tail evoke Nefertiti, a queen of Ancient Egypt of whom a bust remains. The bust is considered to represent an ideal of beauty and has Nefertiti wearing a high blue crown. The similarities end with the appearance though. Nefera's profile states that she believes she does not have to learn other languages as long as she has servants who can translate for her - a sentiment prominent in the real-life Cleopatra's family.
As per nineteenth century mummy fiction customs, the De Niles possess a large collection of enchanted items which they can use for a variety of goals. Especially Cleo is prone to resort to using them, though she has come to understand that the items' usage is not a free deal. Most of the De Niles' items are cursed and come with a nasty payback if used too much.[8] These paybacks have included: the disappearance of Cleo's hair, the unleashing of frog and gnat infestations - Ancient Egyptian plagues mentioned in The Exodus, and a pizza slice brought to life. Each idol has a name which holds a pun on the name of a real-life pharaoh: the Statue of Notalotincommon is a play on the name of Tutankhamun, while the Amulet of Knuck'n'nothin' is a play on the name of Akhenaten.
In their everyday life, the De Niles are assisted by servants resembling Anubis, the protector god of the dead in Ancient Egypt. These servants are presumably ushabtis, Ancient Egyptian statues buried with the dead to follow them into the afterlife and serve them.
A running theme in the De Nile family is, of course, the Nile. In Ancient Egypt, the Nile was a sacred river because only near it was life in Egypt possible. The rest of the land was too dry and warm for anyone to survive. As a result, the Nile Delta, where Egypt is at its most beautiful and comfortable, is how the Ancient Egyptians envisioned the afterlife kingdom to look like. Aside from the family name, the Nile theme is what Nefera's beauty is designed around, which is described as "timeless like the blue of the eternal Nile." Since moving to the USA, Cleo has become a rain enthusiast due to water and thus rain being scarce in Egypt.
While Cleo's fondness for geometry is probably a simple reference to Ancient Egyptian pyramids, the idea may go a little further. One of the main adults of the franchise, Mr. Mummy, is a math teacher and has studied at the Alexandria Institute of Technology M.S., Euclidian Geometry. This references Euclid, who is also known by the title "Father of Geometry". Euclid did much to further the understanding of geometry and was partially able to do so due to the intellectual environment created in Alexandria by the Ptolemaic dynasty, of which the real-life Cleopatra was a member.
Cleo and Nefera have a habit of holding their arms in a two-dimensional pose, which mimics the figures in Ancient Egyptian art and hieroglyphs. Mr. Mummy does not have this habit, though admittedly he has not appeared much yet. Also, both girls occasionally hold their arms crossed over their chest in the so-called 'Osiris position'.[10][11] This is counter to real-life Ancient Egyptian tradition that only allowed the male ruler to be depicted or mummified in that position. Female rulers had to do with a 'semi-Osiris position', which saw only their left arm folded over their chest.
It isn't clear whether in the Monster High universe mummies still possess their organs, which were often removed and stored in jars during the mummification process in the real world. If Cleo does not have her brain anymore, which was in real-life often destroyed because the Ancient Egyptians didn't think it had a purpose, her friendship with Ghoulia could be a play on that, since both mummies and zombies are associated with brains. Also in relation to Monster High mummy anatomy, there is a medical situation called mummingitis that supposedly only affects mummies. It is a pun on meningitis, but presumably is a completely different disease. It's a dream of Ghoulia's to one day find a cure for it''',
)
s6=Story(
    mon_name='Deuce Gorgon',
    origin_story= '''Gorgons are monstrous beings originating from Ancient Greek mythology. Gorgons have snake hair. The Gorgons were three monsters in Greek mythology, daughters of Echidna and Typhon, the mother and father of all monsters, respectively. Their names were Stheno, Euryale, and the most famous of them, Medusa. In some interpretations, Medusa was born human and was later turned into a gorgon by the goddess Athena, after what happened between Medusa and Poseidon. The defining ability of a gorgon is that their stare turns those who look at them to stone. In original Greek mythology, gorgons were precisely and exclusively female, as in, female creatures. In Monster High, they can also be male.''', 
    L_book= '''The Monster High gorgons are Deuce Gorgon, his mother Medusa, his aunts Stheno and Euryale and his cousin Viperine Gorgon. Medusa was born a normie, it was the goddess Athena who changed her into the beautiful and passionate monster she is today. It's not mentioned if the incident with the god Poseidon happened in the Monster High canon. All known gorgons live on or visit Petros Island in Greece.[1] "Petros" is Ancient Greek for "rock" or "stone". Deuce has been turned to stone three times by his own reflection: in "Freakout Friday", "Escape from Skull Shores" and "Great Scarrier Reef". In "Fright On!" there is also something called 'Gorgon Powder', it can turn someone into stone, and reverse the effects of someone turned into stone.'''
)
s7=Story(
    mon_name='Draculaura',
    origin_story='''Creatures with vampiric characteristics have appeared at least as far back as ancient Greece, where stories were told of creatures that attacked people in their sleep and drained their bodily fluids. Tales of walking corpses that drank the blood of the living and spread plague flourished in medieval Europe in times of disease, and people lacking a modern understanding of infectious disease came to believe that those who became vampires preyed first upon their own families. Research from the 20th and 21st centuries has posited that characteristics associated with vampires can be traced back to certain diseases such as porphyria, which makes one sensitive to sunlight; tuberculosis, which causes wasting; pellagra, a disease that thins the skin; and rabies, which causes biting and general sensitivities that could lead to repulsion by light or garlic. Vampire myths were especially popular in eastern Europe, and the word vampire most likely originates from that region. Digging up the bodies of suspected vampires was practiced in many cultures throughout Europe, and it is thought that the natural characteristics of decomposition—such as receding gums and the appearance of growing hair and fingernails—reinforced the belief that corpses were in fact continuing some manner of life after death. Also possibly contributing to this belief was the pronouncement of death for people who were not dead. Because of the constraints of medical diagnosis at the time, people who were very ill, or sometimes even very drunk, and in a coma or in shock were thought dead and later “miraculously” recovered—sometimes too late to prevent their burial. Belief in vampires led to such rituals as staking corpses through the heart before they were buried. In some cultures the dead were buried facedown to prevent them from finding their way out of their graves.''', 
    L_book='''The Monster High vampires drink blood, but they can take iron supplements to avoid having to. So far, it is unexplained where and how blood for consumption is acquired. The main vampire of the franchise, Draculaura, deviates a little from the above description. Despite being of appropriate age, she has yet to acquire the ability to turn into a bat[5] and the fact she still can't does affect her sense of confidence.[6][7] fans originally believed that this inability could be linked to her status as a vegetarian. She notes in her 'Basic' diary that her being a vegetarian is linked to various other un-vampiric aspects of her life and that this is in response to an event in her past, as she states that she's "never going back to the way [she] used to be". Her father strongly disagrees with her refusal to act more like a vampire, but he doesn't force her to change. It was later revealed in Frights, Camera, Action!, that she could not turn into a bat because she had yet to accomplish a significant good deed. She got her vampire powers by the end of the film by returning Elissabat to her rightful place as the vampire queen. Draculaura was born human but was turned into a vampire by Dracula, and he adopted her as Draculaura's birth parents are deceased.
As per traditional West European vampire lore, all Monster High vampires are aristocratic and wealthy. This is in part because they make others work for them, either by manipulation or force. Werewolves used to be their slaves in earlier days, and the manipulatable zombies are still an easily tapped resource.[2] The vampire Valentine differs a little in his choice of servants as he employs three clouds, who also do seem to be more autonomous in their position relative to their 'master'. Werewolves as servants as well as opponents of vampires is a trope established in West European vampire fiction by 1991's World of Darkness, whereas vampires controlling the weak-of-mind dates back to Dracula.
Vampires also display a high sense of vanity and always try to look their best. Due to this they are always dressed in fashionable clothing. Kieran Valentine is a sub-species of vampire, being an emotional vampire, he holds a lot of powers over the matters of emotions.
It's only implied that vampires can reproduce in generation 1. Like in folklore, vampires have to be invited in to a house or public places like a school. Despite an abundant pool of available vampires as potential parents, only Draculaura appears to have a parent that exists outside of Monster High fiction: Dracula. Originally, the character was to be called Ula D, but this was changed to Draculaura, with Ula D, becoming her nickname. Draculaura could be a simple play on the name Dracula, but it might also be a reference to the human protagonist of Carmilla, whose name is Laura. The only other vampire character with a name that is a reference is Bram Devein, whose given name recalls Bram Stoker, the writer of Dracula.
As for Dracula in Monster High, Draculaura notes in her 'School's Out' diary that her father "was already a vampire back when togas were first considered fashionable". Togas are believed to have become part of Roman culture at around 600 BC, which would make him at least 2600 years old. She also notes that the vampire usually thought of as her father was actually a con monster who once rented their castle in Transylvania and went around pretending to be Dracula himself. It isn't quite clear what Draculaura means by this, as there are many "Draculas" (the usual Dracula, Orlok, or Alucard, for instance) who could be the fake she writes about. Since the subject of the fake Dracula comes up in an age-related matter, it seems the section refers to a Vlad III-interpretation of Dracula, who was born in 1431 and would thus be younger than Draculaura herself, but this can't be taken for certain. Perhaps unintended, the matter of the fake Dracula also brings up doubt about the Monster High canonicity of many other Dracula-related vampires, primarily the Sisters.
Draculaura is known to have cousins living in Transylvania, where she lived until she and Dracula had to flee the region in the 17th century. For her to have cousins, Dracula is to have siblings. There are no canonically confirmed siblings to Dracula in any significant medium, but Monster High may interpret the Sisters as siblings of Dracula.
In the Universal version of Dracula, which is most influential to Monster High, Dracula has a daughter and possibly a son. Neither of these exist in the Monster High universe, in which Draculaura is an only child. She also does not appear to have been designed with the aforementioned daughter, Marya Zaleska, in mind. Both enjoy painting, but this is only a minor detail of Draculaura's character and appears a coincidence sooner than anything more significant.
The vampire sisters Rose and Blanche Van Sangre are identified as Romani[8] vampires. The Romani people have a history of being associated with vampires in East Europe, where vampirism was seen as something to befall deviating individuals, which Romani were automatically considered to be. In West Europe, it is Dracula that established the association, as his bodyguards on his way back to Transylvania are identified as Romani. They are human though and not confirmed to know they are working for a vampire, though the themes of xenophobia in the novel do aim for an interpretation of 'fellow evil beings'. Rose and Blanche Van Sangre play into this association.
The Vampire Queen, also known as the Queen of the Vampires, is the queen and ruler of all of her kind. The current holder of the title is Elissabat, who resides in Castle Dracool. The next Vampire Queen can only be found with the Vampire's Heart that glows when the true Queen touches it. Prior to "Frights, Camera, Action!", there had not been a Vampire Queen for 400 years. A Vampire Queen wears a special magenta colored crown that resembles a bat. During their coronation, the crown glows with a golden light.'''
)
s8=Story(
    mon_name='Frankie Stein',
    origin_story= '''An important theme in religion and people's worldviews throughout history are the stories of how everything and, in particular, humans came to be. These stories have had and have a profound effect on the way humans looked and look at themselves. Most religions feature one or more primary gods who either have always been or at one point came forth from some pre-existence chaos. These gods, in turn, created everything else. A common theme in creation myths is that the gods created humans from non-living material, often mud, clay, or wood. Humans of many cultures viewed themselves as inherently artificial beings to the gods, who were inherently natural beings. This idea also played a large role in human acceptance that the gods were their superiors and should be obeyed and appeased. Depending on the details of the religion, the idea of artificiality was also used to explain and justify a hierarchy among humans, such as that the upper class, (wo)men or relevant race/nationality consisted of humans made from better materials, formed with greater care, or created first. Also, depending on the religion was the tolerance for humans taking the role as creators of other creatures. For instance, the golems of Jewish mythology were not always appreciated, and the homunculi were largely seen by the Islamic and Christian religions as a product of magic and, therefore, of evil.''', 
    L_book= '''The Monster High simulacrums are Frankie Stein, her parents, Watzit, Hoodude Voodoo, gingerbread boy, Robecca Steam and Captain Penny. It is likely, though not confirmed that the De Nile servants may be simulacrums, and the same goes for the Tiki. Rochelle Goyle comes from a two parents-home, but nothing else is known about her parents, other than the fact that female gargoyles lay eggs. How Roux, Garrot, and Rockseena came into being is unknown and thus their status as simulacrums is uncertain. However, it can be assumed that living gargoyles are simply present due to it being mentioned that female gargoyles lay eggs. Though uncertain if it can be classified as a gargoyle one of the gargoyle statues was brought to life by Abbey in "Fright On!". As a goo monster, Gooliope was created as experiment #816 in batch #8708, in an unnamed lab by a scientist that signs as R.S. The scientist thought that a lab wasn't the right place to raise a baby, considering that as an experiment, she would be constantly tested on. So Gooliope was left as a baby in a jar at a traveling circus. Adopted by the ringmaster and his wife, she started to grow and grow until she outgrew the jar and was eventually put inside the circus tent, where she grew both in size and in age, cared for by the circus crew. Since then, she has helped on shows and participated in some herself, but is also on a mission to find her heritage since she doesn't know much about it. Eventually, she came across Monster High on one of the circus stops and became a student while the circus is on break.'''
)
s9=Story(
    mon_name='Ghoulia Yelps',
    origin_story= '''Zombies is the name for animated corpses. Zombies are dead humans or undead monsters who are brought back to life through means of vodoun or Voodoo and witchcraft like a priestess of voodoo magic in ancient times sometimes a witch doctor during the ritual in order to do their bidding like in the old movie in black and white, Night of the Living Dead. They are trapped in the same body forever.''', 
    L_book= ''' Zombies are slouching slow-moving undead that tend to gather in hoards and block the school hallways in their numbers. They are a tongue-in-cheek generation gap depiction of youth through the lens of older generations. They speak "zombie", a way of speech which does not make use of the lips and tongue and thus consists of groans and moans. This is understood by most other monsters, and for whom do not, zombies carry translators. Neighthan Rot, a half-zombie, uses full articulation in speech. Unlike Neighthan, zombies do not show visual signs of decay - their unlifeliness is depicted through their pale skin and numbed faces. Zombies are treated with little respect as they lack the ability to respond quickly and are, though highest in number in monster species at Monster High, supposed to emanate a social minority. They are shoved around and forced to serve anyone who does so, such as serving under vampires, a role werewolves have protested and successfully freed themselves of. Despite this, zombies are fully capable to advocate for themselves.'''
)
s10=Story(
    mon_name='Lagoona Blue',
    origin_story= '''Water Monsters are a broad range of monsters that live in water. There are two types of water monsters: freshwater monsters and saltwater monsters. Freshwater monsters live in lakes and rivers and saltwater monsters live in the ocean. Freshwater and saltwater monsters are usually prejudiced against each other.''', 
    L_book= '''In Monster High, there are two major kinds of water monsters, freshwater monsters, and saltwater monsters. There is prejudice against each other, but not much is known on why they don't like each other, but saltwater monsters, according to Gil's parents, are uncivilized and mean-spirited. Other monster species, such as Merfolk, Sirens or some Nymphs are more specific types of water monsters.'''
)
s11=Story(
    mon_name='Heath Burns',
    origin_story = ''' psychic ability allowing a person to create and control fire with the mind. As with other parapsychological phenomena, there is no conclusive evidence in support of the actual existence of pyrokinesis. Many alleged cases are hoaxes; the result of trickery''',
    L_book = '''For the most part, Monster High sticks to the classical elements. Most prominent is the fire elemental Heath Burns, who also has a sister in the books named Harmony and a half-fire elemental cousin named Holt Hyde. Then there's also the water elemental Sue Nami, one of the staff members at Monster High. In her Ghoul Sports notebook, Spectra mentions going up against an air elemental in tennis and losing badly. The only elemental outside of the classical elemental system is C.A. Cupid, who is most likely a bone elemental.'''
)
s12=Story(
    mon_name='Invisi Billy',
    origin_story= '''Invisibles are a type of monster that are or can turn their body fully transparent with the occasional expansion to their clothes as well. They are based off of the invisible man, a classic horror movie monster.''', 
    L_book= ''' In Monster High there are four well known invisibles, one being Mr. Where the drama teacher at Monster High. Invisibles in the Monster High franchise, have only been shown to be male so it's unknown if there are female invisibles or not. Invisi Bill was the next major invisible, his ability to turn invisible is more prominent than when ever Mr. Where shows off his invisibility, but still has been shown to do so too. Invisi Billy also once used his powers to help Rochelle Goyle for a dancing performance. He later starts to date Scarah Screams. In one issue of the Monster High comics they even switch bodies but then are swapped back by the end of the issue. Multiple other issues of the comics mention their relationship, and "13 Wishes" also confirms that they are dating. As an invisible boy, Billy Phaidin has a resemblance to Invisi Billy. However, the two are nothing alike in build, clothing, or manifestation of their invisibility, which makes it clear that they are not the same character.'''
)


def news():
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=monster+high+dolls+g1&_sacat=0&_odkw=monster+high+dolls&_osacat=0'
    response = requests.get(url)
    if response.status_code == 200:
        soup= BeautifulSoup(response.text, "html.parser")
        ebay = []
        d1 = soup.find('li', id="item5a1575ea09")
        l1 = d1.find("a", class_='s-item__link').get('href')
        d2 = soup.find('li', id="item36e246057f")
        l2 = d2.find("a", class_='s-item__link').get('href')
        d3 = soup.find('li', id="item2b5908a6f9")
        l3 = d3.find("a", class_='s-item__link').get('href')
        d4 = soup.find('li', id="item2b62d9c3a3")
        l4 = d4.find("a", class_='s-item__link').get('href')
        d5 = soup.find('li', id="item26def8c1df")
        l5 = d5.find("a", class_='s-item__link').get('href')

        ebay.append(l1)
        ebay.append(l2)
        ebay.append(l3)
        ebay.append(l4)
        ebay.append(l5)
        print(ebay)
      
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
        db.session.add_all([m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,main,main2,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12])
        create_media()
        news()
        db.session.commit()
        print("Deleting Customers")
    