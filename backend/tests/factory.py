from enum import Enum

import factory

from api.models import Team, User


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