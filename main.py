from models.trip_models import TripPreferences, BudgetBreakdown
from data.attraction_loader import load_attractions
trip = TripPreferences(
    destination="Tokyo",
    duration_days=4,
    total_budget=1500.0,
    interests=["food", "culture"],
    pace="relaxed"
)

print(trip.budget_breakdown) #Expected Output: None

budget = BudgetBreakdown(
    accomodation=600.00,
    food=300.00,
    activities=200.0
)

trip.budget_breakdown = budget

print(trip.destination) #Expected Output: Tokyo
print(trip.interests) #Expected Output:['food', 'culture']
print(trip.budget_breakdown.food) #Expected Output: 300.0

#loads Attraction objs
attractions = load_attractions()

print("Number of attractions: ", len(attractions))
for attraction in attractions:
    print(attraction.name)

