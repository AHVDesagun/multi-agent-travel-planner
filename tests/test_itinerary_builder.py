
import unittest

from agents.itinerary_builder import ItineraryBuilder
from models.trip_models import TripPreferences, Attraction


class TestItineraryBuilder(unittest.TestCase):

    def setUp(self):
        """Create a builder and sample trip preferences for each test."""
        self.builder = ItineraryBuilder()

        self.preferences = TripPreferences(
            destination="Tokyo",
            duration_days=2,
            total_budget=1500.0,
            interests=["culture", "food"],
            pace="relaxed"
        )

    def test_attraction_too_long_for_daily_limit_is_skipped(self):
        """An attraction longer than 4 hours should not be scheduled."""
        attractions = [
            Attraction(
                name="Long Museum Tour",
                category="culture",
                area="Ueno",
                estimated_cost=1000.0,
                duration_hours=5.0
            ),
            Attraction(
                name="Short Museum Visit",
                category="culture",
                area="Asakusa",
                estimated_cost=0.0,
                duration_hours=2.0
            )
        ]

        itinerary = self.builder.build(self.preferences, attractions)

        scheduled_names = [
            activity.attraction.name
            for day in itinerary.days
            for activity in day.activities
        ]

        self.assertNotIn("Long Museum Tour", scheduled_names)
        self.assertIn("Short Museum Visit", scheduled_names)

    def test_attractions_are_scheduled_across_multiple_days(self):
        """Activities should move to another day when the current day is full."""
        attractions = [
            Attraction(
                name="Temple",
                category="culture",
                area="Asakusa",
                estimated_cost=0.0,
                duration_hours=1.5
            ),
            Attraction(
                name="Museum",
                category="culture",
                area="Ueno",
                estimated_cost=1000.0,
                duration_hours=2.0
            ),
            Attraction(
                name="Food Market",
                category="food",
                area="Tsukiji",
                estimated_cost=1500.0,
                duration_hours=1.0
            )
        ]

        itinerary = self.builder.build(self.preferences, attractions)

        # The trip should contain both requested days.
        self.assertEqual(len(itinerary.days), 2)

        # The first two activities fit on day 1 (3.5 hours total).
        self.assertEqual(
            [activity.attraction.name for activity in itinerary.days[0].activities],
            ["Temple", "Museum"]
        )

        # The third activity should be scheduled on day 2.
        self.assertEqual(
            [activity.attraction.name for activity in itinerary.days[1].activities],
            ["Food Market"]
        )

        # Each attraction should appear at most once.
        scheduled_names = [
            activity.attraction.name
            for day in itinerary.days
            for activity in day.activities
        ]

        self.assertEqual(len(scheduled_names), len(set(scheduled_names)))

        # Activities should start at 9 AM and run consecutively.
        self.assertEqual(
            itinerary.days[0].activities[0].start_time,
            "09:00 AM"
        )
        self.assertEqual(
            itinerary.days[0].activities[1].start_time,
            "10:30 AM"
        )
        self.assertEqual(
            itinerary.days[1].activities[0].start_time,
            "09:00 AM"
        )

    def test_all_attractions_too_long_leaves_days_empty(self):
        """The builder should preserve the trip days when nothing fits."""
        attractions = [
            Attraction(
                name="Long Museum Tour",
                category="culture",
                area="Ueno",
                estimated_cost=1000.0,
                duration_hours=5.0
            ),
            Attraction(
                name="Long Food Tour",
                category="food",
                area="Tsukiji",
                estimated_cost=2000.0,
                duration_hours=6.0
            )
        ]

        itinerary = self.builder.build(self.preferences, attractions)

        # The itinerary still contains two days.
        self.assertEqual(len(itinerary.days), 2)

        # Neither day should contain activities.
        for day in itinerary.days:
            self.assertEqual(day.activities, [])

    def test_sightseeing_is_used_as_a_backup(self):
        """Sightseeing attractions should follow interest matches."""
        attractions = [
            Attraction(
                name="Shibuya Crossing",
                category="sightseeing",
                area="Shibuya",
                estimated_cost=0.0,
                duration_hours=0.5
            ),
            Attraction(
                name="Temple",
                category="culture",
                area="Asakusa",
                estimated_cost=0.0,
                duration_hours=1.5
            )
        ]

        prioritized = self.builder._prioritize_attractions(
            self.preferences.interests,
            attractions
        )

        self.assertEqual(
            [attraction.name for attraction in prioritized],
            ["Temple", "Shibuya Crossing"]
        )


if __name__ == "__main__":
    unittest.main()
