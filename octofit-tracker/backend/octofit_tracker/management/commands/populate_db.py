from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data using pymongo to avoid primary key issues
        from django.conf import settings
        from pymongo import MongoClient
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'], settings.DATABASES['default']['CLIENT']['port'])
        db = client[settings.DATABASES['default']['NAME']]
        db.leaderboard.delete_many({})
        db.activity.delete_many({})
        db.workout.delete_many({})
        db.user.delete_many({})
        db.team.delete_many({})

        # Create Teams
        marvel = Team.objects.create(name="Marvel", universe="Marvel")
        dc = Team.objects.create(name="DC", universe="DC")

        # Create Users
        users = [
            User(name="Spider-Man", email="spiderman@marvel.com", team=marvel),
            User(name="Iron Man", email="ironman@marvel.com", team=marvel),
            User(name="Captain America", email="cap@marvel.com", team=marvel),
            User(name="Batman", email="batman@dc.com", team=dc),
            User(name="Superman", email="superman@dc.com", team=dc),
            User(name="Wonder Woman", email="wonderwoman@dc.com", team=dc),
        ]
        for user in users:
            user.save()

        # Create Workouts
        workouts = [
            Workout(name="Cardio Blast", description="Intense cardio workout", difficulty="Hard"),
            Workout(name="Strength Training", description="Build muscle and strength", difficulty="Medium"),
            Workout(name="Yoga Flow", description="Relaxing yoga session", difficulty="Easy"),
        ]
        for workout in workouts:
            workout.save()

        # Create Activities
        activities = [
            Activity(user=users[0], type="Running", duration=30, calories=300, date=timezone.now().date()),
            Activity(user=users[1], type="Cycling", duration=45, calories=400, date=timezone.now().date()),
            Activity(user=users[3], type="Swimming", duration=60, calories=500, date=timezone.now().date()),
        ]
        for activity in activities:
            activity.save()

        # Create Leaderboard
        leaderboard_entries = [
            Leaderboard(user=users[0], points=120, rank=1),
            Leaderboard(user=users[1], points=110, rank=2),
            Leaderboard(user=users[3], points=100, rank=3),
        ]
        for entry in leaderboard_entries:
            entry.save()

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
