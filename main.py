from models.trip_models import TripPreferences

trip = TripPreferences(
    destination="Tokyo",
    duration_days=4,
    budget=800.0,
    interests=["food", "culture"],
    pace="relaxed"
)

print(trip.destination) #Expected Output: Tokyo
print(trip.interests) #Expected Output:['food', 'culture']