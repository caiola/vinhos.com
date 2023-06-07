"""Execute seeds on database"""
import pymysql
import sqlalchemy
from sqlalchemy.exc import IntegrityError

from api import db
from api.models.status import Status
from api.models.status_description import StatusDescription
from api.models.status_type import StatusType
from api.models.wine_category import WineCategory
from api.models.wine_category_dict import WineCategories
from api.models.wine_grape_variety import WineGrapeVariety
from api.models.wine_grape_variety_dict import WineGrapeVarieties
from api.models.wine_region import WineRegion
from api.models.wine_region_dict import WineRegions


def seed_tables(app):
    """Seed tables"""
    seed_table_status(app)
    seed_table_wine_category(app)
    seed_table_wine_grape_variety(app)
    seed_table_wine_region(app)


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


def seed_table_wine_category(app):
    """Create wine category records"""
    with app.app_context():
        for category in WineCategories.all():
            instance = WineCategory()
            instance.id = category["id"]
            instance.main_category_id = category["main_category_id"]
            instance.name = category["name"]

            # @TODO Slow because sqlalchemy does not allow to have INSERT IGNORE INTO and is inserting one by one (not bulk)
            try:
                db.session.add(instance)
                db.session.commit()
            except (sqlalchemy.exc.IntegrityError, pymysql.err.IntegrityError):
                db.session.rollback()


def seed_table_wine_grape_variety(app):
    """Create wine grape variety records"""
    with app.app_context():
        for grape_variety in WineGrapeVarieties.all():
            instance = WineGrapeVariety()
            instance.id = grape_variety["id"]
            instance.main_category_id = grape_variety["main_category_id"]
            instance.name = grape_variety["name"]

            # @TODO Slow because sqlalchemy does not allow to have INSERT IGNORE INTO and is inserting one by one (not bulk)
            try:
                db.session.add(instance)
                db.session.commit()
            except (sqlalchemy.exc.IntegrityError, pymysql.err.IntegrityError):
                db.session.rollback()


def seed_table_wine_region(app):
    """Create wine regions records"""
    with app.app_context():
        for region in WineRegions.all():
            instance = WineRegion()
            instance.id = region["id"]
            instance.country = region["country"]
            instance.name = region["name"]

            # @TODO Slow because sqlalchemy does not allow to have INSERT IGNORE INTO and is inserting one by one (not bulk)
            try:
                db.session.add(instance)
                db.session.commit()
            except (sqlalchemy.exc.IntegrityError, pymysql.err.IntegrityError):
                db.session.rollback()
