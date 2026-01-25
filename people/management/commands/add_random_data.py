import random
import uuid
from faker import Faker
from django.core.management.base import BaseCommand
from django.db import connection 
from django.utils import timezone
from people.models import Address, AppUser, CustomerRelationship

fake = Faker('de-AT')

class Command(BaseCommand):
    help = 'Seeds the database with random data'

    def add_arguments(self, parser):
        parser.add_argument("number_of_records", type=int)

    def handle(self, *args, **options):
        connection.ensure_connection()  # forces SQLite connection
        number_of_records = options["number_of_records"]
        batch_size = 1000
        tz = timezone.get_current_timezone()
        name_fabric = {
            AppUser.FEMALE: fake.first_name_female,
            AppUser.MALE: fake.first_name_male,
            AppUser.UNSET: fake.first_name,
        }

        for _ in range(number_of_records // batch_size):
            address_list = [
                Address(
                    street=fake.street_name(),
                    street_number=fake.building_number(),
                    city_code=fake.postcode()[:5],
                    city=fake.city(),
                    country=fake.country(),
                ) for i in range(batch_size)
            ]
            Address.objects.bulk_create(address_list)

            gender = random.choice([AppUser.MALE, AppUser.FEMALE, AppUser.UNSET])
            user_list = [
                AppUser(
                    first_name = name_fabric[gender](),
                    last_name = fake.last_name(),
                    gender = gender,
                    customer_id = uuid.uuid4(),
                    phone_number = fake.phone_number(),
                    # created = fake.date_time_this_decade(),
                    address_id = address_list[i],
                    birthday = fake.date_of_birth(minimum_age=16, maximum_age=80),
                    # last_updated = fake.date_time_this_month(),
                ) for i in range(batch_size)
            ]
            AppUser.objects.bulk_create(user_list)
            relationship_list = [
                CustomerRelationship(
                    appuser_id = user_list[i],
                    points = random.randint(1,100),
                    # created = fake.date_time_this_year(),
                    last_activity = fake.date_time_this_month(tzinfo=tz),
                ) for i in range(batch_size)
            ]
            CustomerRelationship.objects.bulk_create(relationship_list)


        self.stdout.write(self.style.SUCCESS(f'Successfully added {number_of_records} data!'))
