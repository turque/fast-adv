import string
from enum import Enum

import factory
import factory.fuzzy

from app.models import Race, Team, User


class UserFactory(factory.Factory):
    class Meta:
        model = User

    id = factory.Sequence(lambda n: n)
    name = factory.LazyAttribute(lambda obj: f'test{obj.id}')
    email = factory.LazyAttribute(lambda obj: f'{obj.name}@test.com')
    password = factory.LazyAttribute(lambda obj: f'{obj.name}@example.com')


class TeamMembers(Enum):
    SOLO = 1
    DUPLA = 2
    QUARTETO = 4


class TeamFactory(factory.Factory):
    class Meta:
        model = Team

    id = factory.Sequence(lambda n: n)
    name = factory.LazyAttribute(lambda obj: f'team{obj.id}')
    team_members = 2
    owner_id = 1


class RaceFactory(factory.Factory):
    class Meta:
        model = Race

    id = factory.Sequence(lambda n: n)
    name = factory.LazyAttribute(lambda obj: f'race{obj.id}')
    place = factory.fuzzy.FuzzyText(
        length=12, chars=string.ascii_letters, prefix=''
    )
    race_date = factory.Faker('date_object')
    distance = factory.fuzzy.FuzzyInteger(30, 500)
    url_race = factory.LazyAttribute(lambda o: '%s.com.br' % o.name)
    race_description = factory.fuzzy.FuzzyText(
        length=40, chars=string.ascii_letters, prefix=''
    )
    place_description = factory.fuzzy.FuzzyText(
        length=40, chars=string.ascii_letters, prefix=''
    )
    observations = factory.fuzzy.FuzzyText(
        length=50, chars=string.ascii_letters, prefix=''
    )
