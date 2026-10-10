import json
from pathlib import Path
from models.trip_models import Attraction

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ATTRACTIONS_FILE = PROJECT_ROOT / "data" / "attractions.json"

def load_attractions():
    
    with ATTRACTIONS_FILE.open("r", encoding="utf-8") as file:
        attractions_data = json.load(file)
    
    attractions = [] #list for Attraction objs
    
    #converts dictionaries into Attraction objs
    for attraction in attractions_data:
        attractions.append(Attraction(**attraction)
        )
    return attractions
    