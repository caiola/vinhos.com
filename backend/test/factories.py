"""Model Factories to use in tests"""
import factory

from api.models import Account, Ad, Store, User, db
from api.models.status_type import StatusType


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session

    status = StatusType.NEW.value
    account_id = 123
    email = factory.Faker("email")
    # @TODO Enhance the code: password_hash = Meta.model.set_password("pw-hash")
    password_hash = "pw-hash"
    first_name = factory.Faker("first_name")
    middle_name = factory.Faker("middle_name")
    last_name = factory.Faker("last_name")


class AdFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Ad
        sqlalchemy_session = db.session

    title = factory.Faker("sentence")
    description = factory.Faker("text")
    uuid = factory.Faker("uuid4")
    user = factory.SubFactory(UserFactory)
