from dataclasses import dataclass

@dataclass
class BudgetBreakdown:
    accomodation: float | None = None
    food: float | None = None
    transportation: float | None = None
    activities: float | None = None

@dataclass
class TripPreferences:
    destination: str
    duration_days: int
    total_budget: float
    interests: list[str]
    pace: str
    budget_breakdown: BudgetBreakdown | None = None

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
    