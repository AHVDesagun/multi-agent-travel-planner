from models.trip_models import TripPreferences, BudgetBreakdown
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

