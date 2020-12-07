import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

# # FAKE POPULATION SCRIPT
import random
from first_app.models import Topic,WebPage,AccessRecord
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    # Returns a tuple and we are grabbing first element which is reference to model instance
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # Get topic for the entry
        top = add_topic()

        # Create fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry
        webpage = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Create a fake access record for web page
        acc_rec = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]

if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('done populating data!')
