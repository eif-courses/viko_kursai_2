from databases import Database
from env import MYSQL_DB_NAME, MYSQL_HOST, MYSQL_PASSWORD, MYSQL_USER

db_url = f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB_NAME}?charset=utf8'
db_connection = Database(db_url, min_size=5, max_size=20)
