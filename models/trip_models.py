from dataclasses import dataclass

@dataclass
class TripPreferences:
    destination: str
    duration_days: int
    budget: float
    interests: list[str]
    pace: str

@dataclass
class Attraction: 
    name: str
    category: str
    area: str
    estimated_cost: float
    duration_hours: float

@dataclass
class PlannedActivity:
    attraction: Attraction
    start_time: str
    duration_hours: float
    
@dataclass
class DayPlan:
    day_number: int
    activities: list[str]
    
@dataclass
class Itinerary:
    destination: str
    days: list[str]
    