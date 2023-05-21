"""Execute seeds on database"""

from api import db
from api.models.status import Status
from api.models.status_description import StatusDescription
from api.models.status_type import StatusType


def seed_table_status(app):
    """Create status records"""
    with app.app_context():
        # List of status to seed
        statuses = [e.name for e in StatusType]

        for status in statuses:
            status_instance = Status()
            status_instance.id = getattr(StatusType, status)
            status_instance.name = status
            status_instance.description = getattr(StatusDescription, status)
            db.session.add(status_instance)

        db.session.commit()
