from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name="Marvel", universe="Marvel")
        dc = Team.objects.create(name="DC", universe="DC")
        user1 = User.objects.create(name="Spider-Man", email="spiderman@marvel.com", team=marvel)
        user2 = User.objects.create(name="Batman", email="batman@dc.com", team=dc)
        Workout.objects.create(name="Cardio Blast", description="Intense cardio workout", difficulty="Hard")
        Activity.objects.create(user=user1, type="Running", duration=30, calories=300, date="2025-11-22")
        Leaderboard.objects.create(user=user1, points=100, rank=1)

    def test_user_email_unique(self):
        marvel = Team.objects.get(name="Marvel")
        with self.assertRaises(Exception):
            User.objects.create(name="Duplicate", email="spiderman@marvel.com", team=marvel)

    def test_team_creation(self):
        self.assertEqual(Team.objects.count(), 2)

    def test_activity_creation(self):
        self.assertEqual(Activity.objects.count(), 1)

    def test_leaderboard_creation(self):
        self.assertEqual(Leaderboard.objects.count(), 1)

    def test_workout_creation(self):
        self.assertEqual(Workout.objects.count(), 1)
