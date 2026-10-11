from models.trip_models import TripPreferences

class TripInterpreter:
    
    def interpret(self, trip_preferences:TripPreferences) -> TripPreferences:
        
        #validate destination
        trip_preferences.destination = trip_preferences.destination.strip()
        if trip_preferences.destination == "":
            raise ValueError("Invalid destination: Destination must not be empty.")
        
        #validate duration_days
        if trip_preferences.duration_days <= 0:
            raise ValueError("Invalid duration: Duration of trip must be greater than 0.")
        
        #validate total_budget
        if trip_preferences.total_budget <= 0:
            raise ValueError("Invalid budget: Budget must be greater than 0.")
                
        #validate interests
        for i in range(len(trip_preferences.interests)):
            trip_preferences.interests[i] = trip_preferences.interests[i].strip().lower()
        while "" in trip_preferences.interests:
            trip_preferences.interests.remove("")
        if not trip_preferences.interests:
            raise ValueError("Invalid interests: Must have at least one interest.")
            
        #validate pace
        trip_preferences.pace = trip_preferences.pace.strip().lower()
        valid_pace = ['relaxed', 'moderate', 'busy']
        if trip_preferences.pace == "":
            raise ValueError("Invalid pace: Pace must not be empty.")
        if trip_preferences.pace not in valid_pace:
            raise ValueError("Invalid pace: Pace must be set as 'relaxed', 'moderate', or 'busy'.")
        
        #validate budget breakdown categories
        if trip_preferences.budget_breakdown is not None:
            trip_bb = trip_preferences.budget_breakdown
            
            #validate accomodation budget
            if trip_bb.accomodation is not None and trip_bb.accomodation < 0:
                raise ValueError("Invalid accomodation budget: Accomodation budget must be a nonnegative value.")
            
            #validate food budget
            if trip_bb.food is not None and trip_bb.food < 0:
                raise ValueError("Invalid food budget: Food budget must be a nonnegative value.")
            
            #validate transportation budget
            if trip_bb.transportation is not None and trip_bb.transportation < 0:
                raise ValueError("Invalid transportation budget: Transportation budget must be a nonnegative value.")
            
            #validate activities budget
            if trip_bb.activities is not None and trip_bb.activities < 0:
                raise ValueError("Invalid activities budget: Activities budget must be a nonnegative value.")
        
        return trip_preferences #returns cleaned trip_preferences
            