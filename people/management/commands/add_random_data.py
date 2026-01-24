from faker import Faker
from django.core.management.base import BaseCommand
from people.models import Address, AppUser, CustomerRelationship

fake = Faker()

class Command(BaseCommand):
    help = 'Seeds the database with random data'

    def add_arguments(self, parser):
        parser.add_argument("number_of_records", type=int)

    def handle(self, *args, **options):
        number_of_records = options["number_of_records"]
        for _ in range(number_of_records):
            address = Address.objects.create(
                street=fake.street_name(),
                street_number=fake.building_number(),
                city_code=fake.postcode()[:5],
                city=fake.city(),
                country=fake.country(),
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {number_of_records} data!'))
