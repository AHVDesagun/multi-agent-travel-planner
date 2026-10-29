
import unittest

from agents.trip_interpreter import TripInterpreter
from models.trip_models import TripPreferences, BudgetBreakdown


class TestTripInterpreter(unittest.TestCase):

    def setUp(self):
        """Create a fresh interpreter for each test."""
        self.interpreter = TripInterpreter()

    def make_preferences(self, **overrides):
        """Create valid default preferences, replacing any specified fields."""
        values = {
            "destination": "Tokyo",
            "duration_days": 4,
            "total_budget": 1500.0,
            "interests": ["food", "culture"],
            "pace": "relaxed",
            "budget_breakdown": None
        }

        values.update(overrides)
        return TripPreferences(**values)

    # -------------------------
    # Destination tests
    # -------------------------

    def test_destination_whitespace_is_removed(self):
        preferences = self.make_preferences(
            destination="  Tokyo  "
        )

        result = self.interpreter.interpret(preferences)

        self.assertEqual(result.destination, "Tokyo")

    def test_empty_destination_raises_error(self):
        for destination in ["", "   "]:
            with self.subTest(destination=destination):
                preferences = self.make_preferences(
                    destination=destination
                )

                with self.assertRaises(ValueError):
                    self.interpreter.interpret(preferences)

    # -------------------------
    # Duration tests
    # -------------------------

    def test_zero_or_negative_duration_raises_error(self):
        for duration in [0, -1]:
            with self.subTest(duration=duration):
                preferences = self.make_preferences(
                    duration_days=duration
                )

                with self.assertRaises(ValueError):
                    self.interpreter.interpret(preferences)

    # -------------------------
    # Total budget tests
    # -------------------------

    def test_zero_or_negative_total_budget_raises_error(self):
        for budget in [0, -100]:
            with self.subTest(budget=budget):
                preferences = self.make_preferences(
                    total_budget=budget
                )

                with self.assertRaises(ValueError):
                    self.interpreter.interpret(preferences)

    # -------------------------
    # Interest tests
    # -------------------------

    def test_interests_are_normalized(self):
        preferences = self.make_preferences(
            interests=["  FOOD ", "Culture  ", "  nature"]
        )

        result = self.interpreter.interpret(preferences)

        self.assertEqual(
            result.interests,
            ["food", "culture", "nature"]
        )

    def test_blank_interests_are_removed(self):
        preferences = self.make_preferences(
            interests=[" food ", "", "   ", "culture"]
        )

        result = self.interpreter.interpret(preferences)

        self.assertEqual(
            result.interests,
            ["food", "culture"]
        )

    def test_no_valid_interests_raises_error(self):
        for interests in [[], [""], [" ", "   "]]:
            with self.subTest(interests=interests):
                preferences = self.make_preferences(
                    interests=interests
                )

                with self.assertRaises(ValueError):
                    self.interpreter.interpret(preferences)

    # -------------------------
    # Pace tests
    # -------------------------

    def test_pace_is_normalized(self):
        preferences = self.make_preferences(
            pace="  MODERATE  "
        )

        result = self.interpreter.interpret(preferences)

        self.assertEqual(result.pace, "moderate")

    def test_all_valid_paces_are_accepted(self):
        for pace in ["relaxed", "moderate", "busy"]:
            with self.subTest(pace=pace):
                preferences = self.make_preferences(pace=pace)

                result = self.interpreter.interpret(preferences)

                self.assertEqual(result.pace, pace)

    def test_empty_or_invalid_pace_raises_error(self):
        for pace in ["", "   ", "fast", "slow"]:
            with self.subTest(pace=pace):
                preferences = self.make_preferences(pace=pace)

                with self.assertRaises(ValueError):
                    self.interpreter.interpret(preferences)

    # -------------------------
    # Budget breakdown tests
    # -------------------------

    def test_missing_budget_breakdown_is_allowed(self):
        preferences = self.make_preferences(
            budget_breakdown=None
        )

        result = self.interpreter.interpret(preferences)

        self.assertIsNone(result.budget_breakdown)

    def test_zero_and_unspecified_category_budgets_are_allowed(self):
        preferences = self.make_preferences(
            budget_breakdown=BudgetBreakdown(
                accomodation=0.0,
                food=None,
                transportation=0.0,
                activities=None
            )
        )

        result = self.interpreter.interpret(preferences)

        self.assertIs(result, preferences)

    def test_negative_category_budgets_raise_errors(self):
        categories = [
            "accomodation",
            "food",
            "transportation",
            "activities"
        ]

        for category in categories:
            with self.subTest(category=category):
                breakdown = BudgetBreakdown(
                    accomodation=100.0,
                    food=100.0,
                    transportation=100.0,
                    activities=100.0
                )

                setattr(breakdown, category, -1.0)

                preferences = self.make_preferences(
                    budget_breakdown=breakdown
                )

                with self.assertRaises(ValueError):
                    self.interpreter.interpret(preferences)


if __name__ == "__main__":
    unittest.main()
