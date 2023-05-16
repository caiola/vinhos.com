"""Model Factories to use in tests"""
import factory

from api.models import Ad, User, db


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")


class AdFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Ad
        sqlalchemy_session = db.session

    title = factory.Faker("sentence")
    description = factory.Faker("text")
    uuid = factory.Faker("uuid4")
    user = factory.SubFactory(UserFactory)
