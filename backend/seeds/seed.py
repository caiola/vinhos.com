"""Execute seeds on database"""
import pymysql
import sqlalchemy
from sqlalchemy.exc import IntegrityError

from api import db
from api.models.grape_variety import GrapeVariety
from api.models.status import Status
from api.models.status_description import StatusDescription
from api.models.status_type import StatusType
from api.models.grape_varieties_dict import GrapeVarieties


def seed_tables(app):
    """Seed tables"""
    seed_table_status(app)
    seed_table_grape_variety(app)


def seed_table_status(app):
    """Create status records"""
    with app.app_context():
        # List of status to seed
        statuses = [e.name for e in StatusType]

        for status in statuses:
            instance = Status()
            instance.id = StatusType[status].value
            instance.name = status
            instance.description = StatusDescription[status].value

            # @TODO Slow because sqlalchemy does not allow to have INSERT IGNORE INTO and is inserting one by one (not bulk)
            try:
                db.session.add(instance)
                db.session.commit()
            except (sqlalchemy.exc.IntegrityError, pymysql.err.IntegrityError):
                db.session.rollback()


def seed_table_grape_variety(app):
    """Create grape variety records"""
    with app.app_context():
        # List of status to seed
        #grape_varieties = [e.name for e in GrapeVarieties]

        for grape_variety in GrapeVarieties.all():
            instance = GrapeVariety()
            instance.id = grape_variety["id"]
            instance.name = grape_variety["name"]

            # @TODO Slow because sqlalchemy does not allow to have INSERT IGNORE INTO and is inserting one by one (not bulk)
            try:
                db.session.add(instance)
                db.session.commit()
            except (sqlalchemy.exc.IntegrityError, pymysql.err.IntegrityError):
                db.session.rollback()
