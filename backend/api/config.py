import logging
import os

import pymysql

pymysql.install_as_MySQLdb()

DEBUG = os.getenv("ENVIRONMENT") == "DEV"
APPLICATION_ROOT = os.getenv("APPLICATION_APPLICATION_ROOT", "/api")
HOST = os.getenv("APPLICATION_HOST")
PORT = int(os.getenv("APPLICATION_PORT", "3000"))
SQLALCHEMY_TRACK_MODIFICATIONS = False

MYSQL = {
    "user": os.environ["APPLICATION_MYSQL_USER"],
    "pw": os.environ["APPLICATION_MYSQL_PASSWORD"],
    "host": os.environ["APPLICATION_MYSQL_HOST"],
    "port": os.environ["APPLICATION_MYSQL_PORT"],
    "db": os.environ["APPLICATION_MYSQL_DATABASE"],
}
DB_URI = "mysql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % MYSQL

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s \
        pid:%(process)s module:%(module)s %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)
