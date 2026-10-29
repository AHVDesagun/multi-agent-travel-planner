from datetime import datetime, timedelta
from models.trip_models import (
    TripPreferences, 
    Attraction, 
    PlannedActivity, 
    DayPlan, 
    Itinerary
    )

class ItineraryBuilder:
    
    def build(self, trip_preferences:TripPreferences, attractions:list[Attraction]) -> Itinerary:
        #coordinates the overall itinerary building process
        
        daily_limit = self._get_daily_time(trip_preferences.pace)
        
        possible_attractions = self._prioritize_attractions(trip_preferences.interests, attractions)
        
        day_plans = self._create_day_plans(trip_preferences.duration_days)
        
        self._schedule_attractions(day_plans, possible_attractions, daily_limit)
        
        return Itinerary(trip_preferences.destination, day_plans)
    
    
    def _get_daily_time(self, pace:str) -> float:
        #convert the user's pace into an hour limit
        
        if pace == "relaxed":
            return 4.0
        if pace == "moderate":
            return 6.0
        if pace == "busy":
            return 8.0
        else: raise ValueError("Invalid pace: Pace must be 'relaxed', 'moderate', or 'busy'.")
    
    def _prioritize_attractions(self, interests:list[str], attractions:list[Attraction]) -> list[Attraction]:
        #matches attractions based on interests before sightseeing backups
        
        possible_attractions = []
        sightseeing_attractions = []
        
        for attraction in attractions:
            if attraction.category in interests:
                possible_attractions.append(attraction)
            elif attraction.category == "sightseeing":
                sightseeing_attractions.append(attraction)
          
        #adds sightseeing backups to end      
        if "sightseeing" not in interests:
            possible_attractions.extend(sightseeing_attractions)
                
        return possible_attractions
                
    
    def _create_day_plans(self, duration_days:int) -> list[DayPlan]:
        #creates a empty DayPlan for each day of the trip and stores in a Itinerary

        day_plans = []
        
        for i in range(1, duration_days+1):
            day_plans.append(DayPlan(i, []))
        
        return day_plans
        
        
    
    def _schedule_attractions(self, day_plans:list[DayPlan], attractions:list[Attraction], daily_limit:float) -> None:
        #fill day plans with attractions:
            
        for attraction in attractions:
            
            #if attraction exceeds the daily limit, skip
            if attraction.duration_hours > daily_limit: continue
            
            for day in day_plans:
                
                start_time=datetime.strptime("9:00 AM", "%I:%M %p")
                attraction_time = attraction.duration_hours
                
                #if activities already on that day, check if there fit activity can fit
                if day.activities != []:
                    
                    #calculate available time in the day
                    remaining_time = daily_limit
                    for activity in day.activities:
                        remaining_time -= activity.duration_hours
                        start_time+=timedelta(hours=activity.duration_hours)
                    
                    #if attraction duration exceeds remaining time, check the next available day
                    if attraction_time > remaining_time: continue
                    
                #else, time available so schedule on current day
                day.activities.append(PlannedActivity(attraction,
                                                      start_time.strftime("%I:%M %p"),
                                                      attraction_time
                                                      )
                                      )
                break