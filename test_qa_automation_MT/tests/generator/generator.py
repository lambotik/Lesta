import random

from faker import Faker

from test_qa_automation_MT.tests.data.data import Person

faker_ru = Faker('ru_RU')
faker_en = Faker('En')
Faker.seed()


def generated_person():
    yield Person(
        player=faker_en.first_name(),
        credits=random.randint(1, 100000),
        gold=random.randint(1, 100000))
