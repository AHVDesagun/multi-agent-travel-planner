# Travel Planner — Requirements

## Goal
Help users create manageable travel itineraries based on their interests, budget, trip length, and preferred pace.

## Required user inputs
- **Destination:** The city or region the user wants to visit.
- **Trip duration:** Number of days.
- **Budget:** Estimated total budget or budget category.
- **Interests:** Categories such as food, history, nature, shopping, or nightlife.
- **Preferred pace:** Relaxed, moderate, or busy.

## Expected system outputs
- A day-by-day itinerary.
- A list of recommended attractions.
- Estimated activity costs.
- Explanations for why activities were selected.
- Warnings and suggested adjustments if the itinerary is too busy or exceeds the budget.

## Core rules
- A relaxed itinerary should contain fewer major activities than a busy itinerary.
- Recommendations should match the user's interests.
- Estimated costs should be considered when selecting activities.
- The reviewer should identify overloaded days and suggest corrections.
- The system should explain important planning decisions.

## Future features
- Like, dislike, and skip interactions for attractions and hotels.
- Update recommendations using user feedback.
- A simple visual swipe interface.

## Out of scope for the first version
- Making real hotel reservations.
- Processing payments.
- Building a complex web application.
- Requiring an LLM or paid AI API.