"""Execute seeds on database"""

from api import db
from api.models.grape_variety import GrapeVariety
from api.models.status import Status
from api.models.status_description import StatusDescription
from api.models.status_type import StatusType
from api.models.grape_varieties_dict import GrapeVarieties


def seed_table_status(app):
    """Create status records"""
    with app.app_context():
        # List of status to seed
        statuses = [e.name for e in StatusType]

        for status in statuses:
            status_instance = Status()
            status_instance.id = StatusType[status].value
            status_instance.name = status
            status_instance.description = StatusDescription[status].value
            db.session.add(status_instance)

        db.session.commit()


def seed_table_grape_variety(app):
    """Create grape variety records"""
    with app.app_context():
        # List of status to seed
        grape_varieties = [e.name for e in GrapeVarieties]

        for grape_variety in grape_varieties:
            instance = GrapeVariety()
            instance.id = grape_variety.id
            instance.name = grape_variety.name
            db.session.add(instance)

        db.session.commit()
