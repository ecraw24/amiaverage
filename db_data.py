HEROKU_APP_NAME = "amiaverage"
TABLE_NAME = "skillsinfo"
import subprocess, psycopg2
from psycopg2 import sql

conn_info = subprocess.run(["heroku", "config:get", "DATABASE_URL", "-a", HEROKU_APP_NAME], stdout = subprocess.PIPE)
connuri = conn_info.stdout.decode('utf-8').strip()
conn = psycopg2.connect(connuri)
cursor = conn.cursor()
cursor.execute(sql.SQL("SELECT *  FROM {};").format(sql.Identifier(TABLE_NAME)))
count = cursor.fetchall()
print(count)
