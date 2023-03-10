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
    "user": os.getenv("APPLICATION_MYSQL_USER", "mysql"),
    "pw": os.getenv("APPLICATION_MYSQL_PW", ""),
    "host": os.getenv("APPLICATION_MYSQL_HOST", "dbdefault"),
    "port": os.getenv("APPLICATION_MYSQL_PORT", 5432),
    "db": os.getenv("APPLICATION_MYSQL_DB", "mysql"),
}
DB_URI = "mysql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % MYSQL

logging.basicConfig(
#   filename=os.getenv("SERVICE_LOG", "server.log"),
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s \
        pid:%(process)s module:%(module)s %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)
