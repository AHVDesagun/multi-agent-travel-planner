from models.trip_models import TripPreferences, BudgetBreakdown
from data.attraction_loader import load_attractions
from agents.trip_interpreter import TripInterpreter

trip1 = TripPreferences(
    destination="Tokyo",
    duration_days=4,
    total_budget=1500.0,
    interests=["food", "culture"],
    pace="relaxed"
)

print(trip1.budget_breakdown) #Expected Output: None

budget = BudgetBreakdown(
    accomodation=600.00,
    food=300.00,
    activities=200.0
)

trip1.budget_breakdown = budget

print(trip1.destination) #Expected Output: Tokyo
print(trip1.interests) #Expected Output:['food', 'culture']
print(trip1.budget_breakdown.food) #Expected Output: 300.0

#loads Attraction objs
attractions = load_attractions()

print("Number of attractions: ", len(attractions))
for attraction in attractions:
    print(attraction.name)

trip2 = TripPreferences(
    destination="Tokyo",
    duration_days=4,
    total_budget=1500.0,
    interests=["food", "CULTURE"],
    pace="busy"
)

trip_interpreter = TripInterpreter()

print("BEFORE: ", trip2.interests)
trip_interpreter.interpret(trip2)
print("AFTER: ", trip2.interests)

trip3 = TripPreferences(
    destination="Tokyo",
    duration_days=0,
    total_budget=1500.0,
    interests=["food", "culture"],
    pace="relaxed"
)
try:
    trip_interpreter.interpret(trip3)
except ValueError:
    print("Error detected")
