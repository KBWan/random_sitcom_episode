import requests
import random

# Dictionary of Top 20 sitcomes and their IMDb IDs
showids = {
    "The Simpsons":  "tt0096697",
    "Cheers": "tt0083399",
    "Seinfeld": "tt0098904",
    "I Love Lucy": "tt0043208",
    "All in the Family": "tt0066626",
    "M*A*S*H": "tt0068098",
    "The Mary Tyler Moore Show": "tt0065314",
    "The Honeymooners": "tt0042114",
    "Parks and Recreation": "tt1266020",
    "The Larry Sanders Show": "tt0103466",
    "The Dick Van Dyke Show": "tt0054533",
    "Curb Your Enthusiasm": "tt0264235",
    "Frasier": "tt0106004",
    "The And y Griffith Show": "tt0053479",
    "Arrested Development": "tt0367279",
    "The Cosby Show": "tt0086687",
    "Taxi": "tt0077089",
    "30 Rock": "tt0496424",
    "Roseanne": "tt0094540",
    "BoJack Horseman": "tt3398228",
    "Fleabag": "tt5687612",
    "South Park": "tt0121955",
    "The Office": "tt0386676",
    "Community": "tt1439629",
    "Atlanta": "tt4288182",
    "The Bob Newhart Show": "tt0068049",
    "Louie": "tt1492966",
    "Malcom in the Middle": "tt0212671",
    "It's Always Sunny in Philadelphia": "tt0472954",
    "The Office": "tt0290978",
    "Fawlty Towers": "tt0072500",
    "The Golden Girls": "tt0088526",
    "Better Things": "tt4370596",
    "Spongebob Squarepants": "tt0206512",
    "Everybody Loves Raymond": "tt0115167",
    "Sex and the City": "tt0159206",
    "Bob's Burgers": "tt1561755",
    "Friends": "tt0108778",
    "Black-ish": "tt3487356",
    "Review": "tt2141913",
    "King of the Hill": "tt0118375",
    "Brockmire": "tt5722190",
    "Brooklyn Nine-Nine": "tt2467372",
    "Veep": "tt1759761",
    "Broad City": "tt2578560",
    "The Good Place": "tt4955642",
    "Fresh Prince of Bel-Air": "tt0098800",
    "The Jeffersons": "tt0072519",
    "Barney Miller": "tt0072472",
    "NewsRadio": "tt0112095",
    "Police Squad!": "tt0083466",
    "I'm Alan Partridge": "tt0129690",
    "Scrubs": "tt0285403",
    "The Bernie Mac Show": "tt0285341",
    "The Odd Couple": "tt0063374",
    "Murphy Brown": "tt0094514",
    "You’re the Worst": "tt3228420",
    "It’s Garry Shandling’s Show": "tt0090459",
    "Spaced": "tt0187664",
    "Good Times": "tt0070991",
    "Catastrophe": "tt4374208",
    "The Thick of It": "tt0459159",
    "Designing Women": "tt0090418",
    "What We Do in the Shadows": "tt7908628",
    "Phineas and Ferb": "tt0852863",
    "Get Smart": "tt0058805",
    "The Jack Benny Program": "tt0042116",
    "Maude": "tt0067185",
    "Flight of the Conchords": "tt0863046",
    "The Phil Silvers Show": "tt0047763",
    "Rick and Morty": "tt2861424",
    "The Comeback": "tt0434672",
    "Absolutely Fabulous": "tt0105929",
    "Futurama": "tt0149460",
    "Blackadder": "tt0084988",
    "New Girl": "tt1826940",
    "One Day at a Time": "tt5339440",
    "Peep Show": "tt0387764",
    "WKRP in Cincinnati": "tt0077097",
    "Sanford and Son": "tt0068128",
    "Will & Grace": "tt0157246",
    "How I Met Your Mother": "tt0460649",
    "Letterkenny": "tt4647692",
    "Modern Family": "tt1442437",
    "The George Burns and Gracie Allen Show": "tt0042111",
    "Living Single": "tt0106056",
    "Soap": "tt0075584",
    "Party Down": "tt1073507",
    "A Different World": "tt0092339",
    "The Big Bang Theory": "tt0898266",
    "Buffalo Bill": "tt0084992",
    "Daria": "tt0118298",
    "Big Mouth": "tt6524350",
    "Insecure": "tt5024912",
    "Baskets": "tt3468798",
    "Bluey": "tt7678620",
    "Night Court": "tt0086770",
    "Derry Girls": "tt7120662",
    "Frank’s Place": "tt0092354",
    "Schitt’s Creek": "tt3526078"
}

#verifying dict ids match api
shows = list(showids.keys())
#for show in shows:
#    x = requests.get(f"https://api.imdbapi.dev/titles/{showids[show]}").json();
#    showids[show] = x['id'];
#    print(show + " | " + x['primaryTitle'])
#   



#Function gets random episode from the top 20 sitcoms
#Determines random 5 minute segment of the episode to watch
#Returns episode data
def get_random_episode():

    random_show = random.choice(shows)

    random_show_id = showids[random_show]
    
    eps = requests.get(f'https://api.imdbapi.dev/titles/{random_show_id}/episodes').json()

    random_episode = random.choice(eps['episodes'])
    runtime = random_episode['runtimeSeconds']

    if runtime < 300:
        watch_period = "0:00 - 5:00"
    else:
        start = random.randint(0, runtime - 300)
        end = start + 300
        watch_period = f"{start // 60}:{start % 60:02d} - {end // 60}:{end % 60:02d}"
    response_data = {
        "show": random_show,
        "episode_title": random_episode['title'],
        "season": random_episode['season'],
        "episode_number": random_episode['episodeNumber'],
        "watch_period": watch_period,
        "rating": random_episode['rating']['aggregateRating'],
        "air_date": random_episode['releaseDate'],
        "description": random_episode['plot'],
        "image": random_episode['primaryImage']['url']
    }
    return response_data

print(get_random_episode())