from django.core.management.base import BaseCommand
# from listings.models import Listing, Booking
from alx_travel_app.listings.models import Listing, Booking
from faker import Faker
import random

fake = Faker()


class Command(BaseCommand):
    help = 'Seed the database with sample listings and bookings'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')
        
        # Create Listings
        for _ in range(10):
            listing = Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(nb_sentences=5),
                location=fake.city(),
                price_per_night=random.randint(50, 300),
                is_available=random.choice([True, False])
            )
            
            # Create Bookings for each Listing
            for _ in range(random.randint(1, 5)):
                Booking.objects.create(
                    listing=listing,
                    guest_name=fake.name(),
                    check_in=fake.date_this_year(),
                    check_out=fake.date_this_year(),
                    total_price=random.randint(100, 1000)
                )

        self.stdout.write(self.style.SUCCESS('Seeding complete!'))
