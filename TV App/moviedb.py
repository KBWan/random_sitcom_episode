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
    "The Andy Griffith Show": "tt0053479",
    "Arrested Development": "tt0367279",
    "The Cosby Show": "tt0086687",
    "Taxi": "tt0077089",
    "30 Rock": "tt0496424",
    "Roseanne": "tt0094540",
    "BoJack Horseman": "tt3398228"
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