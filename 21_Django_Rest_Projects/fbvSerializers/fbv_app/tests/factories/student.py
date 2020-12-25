import uuid

import factory
from faker import Factory
from fbv_app.models import Student
import random

faker = Factory.create()

class StudentFactory(factory.django.DjangoModelFactory):
    """
    id, name, score
    """

    class Meta:
        model = Student
        django_get_or_create = ("id", "name", "score")

    id = 2
    name = faker.name()
    score = round(random.uniform(60, 100), 2)
