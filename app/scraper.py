import json
import requests
from bs4 import BeautifulSoup

class Location:
    def __init__(self):
         self.city = ""
         self.country = ""
         self.street = ""
         self.email = ""
         self.name = ""
         self.telephone = ""
         self.zip = ""

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
                    sort_keys=True, indent=4)

class Event:
    def __init__(self):
        self.name = ""
        self.id = ""
        self.duplicate_id  = ""
        self.source = ""
        self.title = ""
        self.description = ""
        self.location = ""
        self.start_date_time = ""
        self.end_date_time = ""
        self.organizer = ""
        self.pricing = ""
        self.url = ""
        self.categories = ""

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
                    sort_keys=True, indent=4)

def Run():
    # do the scraping
    events = []

    default_location = Location()
    default_location.name = "Makerspace"
    default_location.telephone = "07131 88795533"
    default_location.email = "makerspace@experimenta.science"
    default_location.street = "Experimentaplatz 1"
    default_location.zip = "74072"
    default_location.city = "Heilbronn"
    default_location.country = "Germany"


    r = requests.get('https://makerspace.experimenta.science/workshops/')
    if r.status_code != 200:
        raise RuntimeError("Failed to fetch page")

    root = BeautifulSoup(r.content, features="html.parser")
    post = root.find("div", { "class": "wp-post" })
    list_items = post.find_all("a", { "class": "list-group-item" })

    for item in list_items:
        title = item.find("h5")

        date = item.find_all("div" , { "class": "col-12" })[1].find_all("div")[0]
        start = item.find_all("div" , { "class": "col-12" })[1].find_all("div")[1]

        e = Event()
        e.name = title.text
        e.start_date_time = date.text + " " + start.text
        e.location = default_location
    
        events.append(e)

    return events